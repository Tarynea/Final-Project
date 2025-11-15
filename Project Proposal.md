Project Proposal
Idea 1: Verified “Rate My Professor” Style Platform for Babson
1. The Big Idea: This project is inspired by Rate My Professor but aims to make the system
more credible and reliable by requiring users to verify that they are actual Babson
students through their Babson email. Reviews will still remain anonymous publicly, but
email verification will prevent spam, fake reviews, or biased entries. Students will be able
to submit reviews, read ratings for professors, and interact with others’ reviews by
upvoting, downvoting, or commenting. The upvoting will ensure that just one bad review
does not negatively affect the overall rating. The minimum viable product will allow
users to submit verified reviews and display them by professor. The stretch goal is to add
comments, credibility scores, and trend visualizations.
2. Learning Objectives: Our shared goal is to learn how to build a system that handles user
generated content safely and organizes it in a meaningful way. Individually, Tamanna
wants to focus on authentication logic and building the backend routes, while Tarynea
wants to work on storing, displaying, and sorting reviews with a user-friendly interface.
Together, we hope to become more comfortable with web development basics and
structured data.
3. Implementation Plan: We plan to build this using a simple Python web framework such
as Flask or FastAPI. The first step will be creating a data structure for professors and
reviews. Next, we will implement a basic verification system by requiring users to log in
with a Babson email format. After that, we will create routes for adding reviews,
displaying reviews, and handling upvotes or downvotes. If time allows, we will add
features like comments or sorting reviews by relevance.
4. Project Schedule: In the first week we will set up the backend structure and choose our
database format and focus on implementing review submissions and displaying them.
Week two will be dedicated to adding verification logic and voting features and involve
building or improving the interface and adding optional features like comments. Week
three will be reserved for debugging, improving performance, and preparing our final
project materials.
5. Collaboration Plan: Tamanna will concentrate on backend development, including
authentication, routing, and data validation. Tarynea will focus on database structure,
displaying reviews, and the user-facing side of the platform. We will use GitHub for
version control, review each other’s work before merging, and have regular planning
meetings to stay aligned. This structure keeps our workflow simple and consistent while
dividing responsibilities clearly.
6. Risks and Limitations: The primary risk is that real authentication systems are complex,
so we may need to simulate verification instead of creating a fully secure login system.
Another limitation is that moderating user-generated content can be difficult, especially if
comments are included. The project could also expand quickly, so staying disciplined
with the MVP will be important to finish on time.
7. Additional Course Content: We may need additional support on backend web
development, routing, and handling user-generated data. Guidance on simple database
management, form handling, and basic authentication concepts would also be helpful as
we build out the platform.




Idea 2: Mandala Art Grid Generator
1. The Big Idea: The main idea of this project is to build a Python tool that automatically
generates precise mandala grids for artists. Mandala art requires perfect symmetry, and a
single measuring error can ruin hours of work, so this tool will save time and frustration
by letting users customize grid styles such as circle based, petal based, or geometric
layouts. The minimum viable product will generate a basic circular grid with adjustable
petal counts and allow the user to export it as an image or PDF. The stretch goal is to
offer multiple grid templates, sliders to control size and layers, and possibly a simple
interface to preview or project the design.
2. Learning Objectives: Since we are a two-member team, our shared goal is to learn how to
use Python graphics libraries to generate geometric patterns programmatically and to
practice exporting high quality visual files. Individually, Tamanna aims to deepen their
understanding of geometry algorithms for pattern creation, while Tarynea wants to
explore user-friendly design and learn how to build a simple interface/visualization tool.
3. Implementation Plan: We will begin by researching the most suitable Python libraries for
drawing shapes and exporting images (libraries that might be useful for creating the grid
structure, and reportlab could help with generating PDFs). The first step will be
generating concentric circles and radial lines, then allowing the user to adjust the number
of petals and grid density. If we are unsure about certain tools, we will build small
prototypes to test them before committing to one. Once the core generator works, we will
focus on exporting files.
4. Project Schedule: During the first week we plan to finalize our feature list and build the
basic grid generator with circles and lines and add customization features like petal count,
spacing, and layered grids. The second week will be focused on export functions so users
can download their designs as PDFs or PNGs. The third week will be reserved for
polishing, optional interface work, and user testing, as well as debugging, documentation,
and preparing our presentation.
5. Collaboration Plan: Tamanna will take the lead on implementing geometric logic and the
pattern generator, while Tarynea will focus on exporting, interface design, and overall
usability. We will use GitHub branches to manage our work and meet regularly to merge
updates and make sure the tool feels cohesive. Our style will be similar to a lightweight
agile approach, keeping small daily goals so we always know what the next step is.
6. Risks and Limitations: The biggest risk is that generating precise and customizable
patterns may take more time than expected, especially when dealing with multiple grid
styles. Another limitation is that exporting high-resolution PDFs or images can be tricky
depending on library support. If we run into time constraints, the user interface might
have to be simplified or removed entirely in favor of a command line MVP.
7. Additional Course Content: We may need additional guidance on graphical libraries, PDF
generation, and optional graphical user interface development. Topics related to image
creation and modular code structure would also be helpful as we build and refine the tool.




Idea 3: Heartbreak Recovery Tracker
1. The Big Idea: This project aims to create a Heartbreak Recovery Tracker, a tool designed
to help people navigate emotional recovery after breakups, friendship endings, or other
forms of loss. The tool would allow users to log their mood each day, track a no-contact
streak, reflect through short prompts, and see their progress over time. The minimum
viable product will be a command-line tool where the user enters their daily mood and
streak status and receives simple summaries. The stretch goal is to include charts for
mood trends, reflection prompts, and a more polished interface.
2. Learning Objectives: As a team, we want to learn how to collect and store user input,
manage simple datasets, and turn emotional progress into something measurable through
programming. Individually, Tamanna will focus on the logic for storing data, calculating
streaks, and computing mood averages, while Tarynea will work on data visualization,
user prompts, and making the overall interaction feel intuitive and supportive.
3. Implementation Plan: Our first step will be creating a basic input system that lets users
enter a mood rating and no-contact progress each day. We will store this information
maybe in a simple CSV file for easy access. After that, we will implement calculations
like average mood, streak length, and a short daily summary. In the next phase, we will
build visualizations using matplotlib to show emotional trends. We may also prototype
reflection prompts to help users process their emotions. If time allows, we will consider
creating a small interface or structured menu system.
4. Project Schedule: In week one we will focus on setting up the data structure and input
system and building the logic for calculating mood averages and streaks. During week
two, we will work on creating charts that show progress visually and improving prompts,
usability, and interactions. Week three will focus on debugging, final polishing, and
preparing our project presentation.
5. Collaboration Plan: With only two members, we will divide tasks but also collaborate on
complex features. Tamanna will handle most of the data storage and calculation logic,
and Tarynea will focus on visualizations, prompts, and overall flow. We will
communicate through shared GitHub repositories, meet regularly for merges, and make
sure our code styles stay consistent. This structure ensures we stay efficient while also
supporting each other during challenging parts.
6. Risks and Limitations: The biggest risk is scope expansion: emotional tools can easily
turn into full apps with notifications or UI features, which we may not have time to
implement. Data visualization can also take longer than expected, especially if we want it
to be aesthetically pleasing. Also, we want to make it clear that the tool will remain
focused on awareness, not any sort of treatment.
7. Additional Course Content: Topics that may support this project include file handling,
reading and writing structured data, and potentially exploring basic interface design.
Error handling for user input will also be helpful.