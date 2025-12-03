import sqlite3
import datetime
from flask import Flask, render_template, g, request, redirect, url_for

app = Flask(__name__)
DATABASE = "babson_rmp.db"

# ---------- Database Helpers ----------

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    """Create tables if they don't exist and seed sample professors."""
    db = get_db()

    db.execute("""
        CREATE TABLE IF NOT EXISTS professors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT
        )
    """)

    db.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            professor_id INTEGER NOT NULL,
            email TEXT NOT NULL,
            course TEXT,
            rating INTEGER NOT NULL,
            text TEXT,
            upvotes INTEGER DEFAULT 0,
            downvotes INTEGER DEFAULT 0,
            created_at TEXT,
            FOREIGN KEY (professor_id) REFERENCES professors(id)
        )
    """)

    count = db.execute("SELECT COUNT(*) AS c FROM professors").fetchone()["c"]

    if count == 0:
        sample = [
            ("Professor X", "Mathematics & CS"),
            ("Professor Y", "Analytics"),
            ("Professor Z", "Entrepreneurship"),
        ]
        db.executemany(
            "INSERT INTO professors (name, department) VALUES (?, ?)",
            sample
        )
        db.commit()

# NEW FIX:
_db_initialized = False

@app.before_request
def before_request():
    global _db_initialized
    if not _db_initialized:
        init_db()
        _db_initialized = True


# ---------- Routes ----------

@app.route("/")
def index():
    db = get_db()
    q = request.args.get("q", "").strip()

    base_query = """
        SELECT
            p.id,
            p.name,
            p.department,
            COUNT(r.id) AS review_count,
            AVG(r.rating) AS avg_rating
        FROM professors p
        LEFT JOIN reviews r ON p.id = r.professor_id
    """

    params = []
    conditions = []

    if q:
        conditions.append("p.name LIKE ?")
        params.append(f"%{q}%")

    if conditions:
        base_query += " WHERE " + " AND ".join(conditions)

    base_query += " GROUP BY p.id ORDER BY p.name"

    professors = db.execute(base_query, params).fetchall()

    return render_template("index.html", professors=professors, q=q)


@app.route("/professors/new", methods=["GET", "POST"])
def add_professor():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        department = request.form.get("department", "").strip()

        if not name:
            return render_template("add_professor.html",
                                   error="Professor name is required.",
                                   name=name,
                                   department=department)

        db = get_db()

        existing = db.execute(
            "SELECT id FROM professors WHERE LOWER(name) = LOWER(?)",
            (name,)
        ).fetchone()

        if existing:
            return render_template(
                "add_professor.html",
                error="A professor with that name already exists.",
                name=name,
                department=department,
            )

        cur = db.execute(
            "INSERT INTO professors (name, department) VALUES (?, ?)",
            (name, department)
        )
        db.commit()
        new_prof_id = cur.lastrowid

        return redirect(url_for("professor_detail", prof_id=new_prof_id))

    return render_template("add_professor.html")



@app.route("/professors/<int:prof_id>")
def professor_detail(prof_id):
    db = get_db()

    professor = db.execute(
        "SELECT * FROM professors WHERE id = ?",
        (prof_id,)
    ).fetchone()

    if professor is None:
        return "Professor not found", 404

    sort = request.args.get("sort", "newest")

    if sort == "highest":
        order_clause = "rating DESC, created_at DESC"
    elif sort == "helpful":
        order_clause = "(upvotes - downvotes) DESC, created_at DESC"
    else:
        order_clause = "created_at DESC"

    reviews = db.execute(
        f"""
        SELECT * FROM reviews
        WHERE professor_id = ?
        ORDER BY {order_clause}
        """,
        (prof_id,)
    ).fetchall()

    stats = db.execute(
        """
        SELECT COUNT(*) AS count, AVG(rating) AS avg_rating
        FROM reviews
        WHERE professor_id = ?
        """,
        (prof_id,)
    ).fetchone()

    review_count = stats["count"]
    avg_rating = round(stats["avg_rating"], 1) if stats["avg_rating"] is not None else None

    return render_template(
        "professor.html",
        professor=professor,
        reviews=reviews,
        review_count=review_count,
        avg_rating=avg_rating,
        sort=sort,
    )

from flask import request, redirect, url_for
import datetime

@app.route("/professors/<int:prof_id>/review", methods=["POST"])
def add_review(prof_id):
    db = get_db()

    email = request.form.get("email", "").strip()
    course = request.form.get("course", "").strip()
    rating = request.form.get("rating").strip()
    text = request.form.get("text", "").strip()

    # convert rating to int
    try:
        rating = int(rating)
    except ValueError:
        rating = 0

    # basic validation
    if not email.endswith("@babson.edu") or not (1 <= rating <= 5):
        return redirect(url_for("professor_detail", prof_id=prof_id))

    # insert review
    db.execute(
        """
        INSERT INTO reviews (professor_id, email, course, rating, text, upvotes, downvotes, created_at)
        VALUES (?, ?, ?, ?, ?, 0, 0, ?)
        """,
        (
            prof_id,
            email,
            course,
            rating,
            text,
            datetime.datetime.utcnow().isoformat(timespec="seconds")
        ),
    )

    db.commit()

    return redirect(url_for("professor_detail", prof_id=prof_id))

@app.route("/reviews/<int:review_id>/vote", methods=["POST"])
def vote_review(review_id):
    db = get_db()
    vote_type = request.form.get("vote")

    if vote_type == "up":
        db.execute(
            "UPDATE reviews SET upvotes = upvotes + 1 WHERE id = ?",
            (review_id,)
        )
    elif vote_type == "down":
        db.execute(
            "UPDATE reviews SET downvotes = downvotes + 1 WHERE id = ?",
            (review_id,)
        )

    db.commit()

    # redirect back to the professor page
    prof = db.execute(
        "SELECT professor_id FROM reviews WHERE id = ?",
        (review_id,)
    ).fetchone()

    return redirect(url_for("professor_detail", prof_id=prof["professor_id"]))


if __name__ == "__main__":
    app.run(debug=True)
