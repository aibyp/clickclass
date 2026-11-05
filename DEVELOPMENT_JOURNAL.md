# ✳ CLICKCLASS — THE DEVELOPMENT DIARY

### from an idea to something real.

`BUILDING IN PUBLIC` · `LEARNING BY BUILDING` · `2026`

---

> Every project has a story behind the code.
>
> This is mine.

Welcome to my little corner of the ClickClass journey.

ClickClass started as an idea in August 2026. What began as a thought about making classroom attendance smarter slowly turned into a hands-on journey through Python, Computer Vision, Machine Learning, databases, authentication, debugging and application development.

This journal is where I document it all.

Not just the finished features, but also the experiments, the errors, the late debugging sessions, the small wins and everything in between.

**No perfect journey. Just progress.**

---

# 00 — THE ORIGIN STORY

<sub>AUGUST 2026 · THE FIRST IDEA</sub>

### ✧ It started with a question.

Why should teachers spend so much time taking attendance manually when technology could make the process simpler?

I wanted to build something that applied Artificial Intelligence to a problem that exists in everyday classrooms.

That thought became ClickClass.

The initial vision was to develop an AI-powered attendance management system that could identify students through facial recognition and eventually automate classroom attendance.

I didn't have the complete architecture figured out. I didn't know every technology I would need.

But I knew what I wanted to build.

**The mission:** Turn a simple classroom problem into an intelligent application.

`STATUS: IDEA → PROJECT`

---

# 01 — THE FIRST COMMIT

<sub>21 OCTOBER 2026 · e647521</sub>

### ⚙️ Setting the stage.

Every good application needs a foundation.

I started setting up the development environment and installing the required dependencies.

**What happened:**
- Set up the Python development environment.
- Started configuring the project dependencies.
- Prepared the initial development structure.

**A little realization:**

Before building the actual product, I needed to make sure the foundation was right.

`MILESTONE 01 — DEVELOPMENT BEGINS`

---

# 02 — GIVING THE IDEA A FACE

<sub>25 OCTOBER 2026 · 4442a9b</sub>

### 🏠 The first interface.

It was time to move beyond the terminal and start building something visible.

I started developing the ClickClass home screen using Streamlit.

**What I worked on:**
- Built the initial home screen.
- Started structuring the user interface.
- Established the initial application layout.

Seeing the project take shape as an actual application made the whole idea feel much more real.

**A small screen, a big step forward.**

`MILESTONE 02 — FIRST UI`

---

# 03 — THE INTELLIGENCE BEHIND THE PROJECT

<sub>28 OCTOBER 2026 · 412323b</sub>

### 🧠 Making ClickClass recognize faces.

This was one of the biggest technical milestones so far.

I started developing the facial recognition pipeline that would become the core of ClickClass.

**The technical work:**

- Integrated dlib for facial processing.
- Worked with 128-dimensional facial embeddings.
- Explored how facial features can be represented numerically.
- Integrated Support Vector Machine (SVM) using Scikit-learn.
- Worked on loading facial recognition models.
- Started connecting the ML pipeline with student identification.

**What I learned:**

A face is more than an image. It can be represented through numerical features that a Machine Learning model can use for classification.

I also started understanding how Computer Vision and traditional Machine Learning can work together.

**The moment:** ClickClass was getting its intelligence. ✨

`MILESTONE 03 — ML PIPELINE`

---

# 04 — RECOGNIZING THE RIGHT PEOPLE

<sub>29 OCTOBER 2026 · 21e54e0</sub>

### 🔐 Student authentication.

Building the recognition pipeline was only one part of the challenge.

The next step was integrating it into the actual student experience.

**What I worked on:**
- Developed student authentication functionality.
- Integrated camera-based face authentication.
- Connected the facial recognition pipeline with student identification.
- Worked on recognizing registered students.

**What I learned:**

Building a model and integrating it into a real application are two different challenges.

The model, user interface and backend need to communicate properly for the complete experience to work.

`MILESTONE 04 — STUDENT AUTHENTICATION`

---

# 05 — THE TEACHER'S SPACE

<sub>30 OCTOBER 2026 · 7eb6dd3</sub>

### 👩🏻‍🏫 Building the teacher dashboard.

ClickClass wasn't just about identifying students.

Teachers needed their own space to interact with the system and eventually manage attendance.

**What I worked on:**
- Developed the initial teacher dashboard.
- Created separate dashboard tabs.
- Organized the teacher-side interface.
- Continued building the teacher experience.

**The bigger picture:**

I started shaping ClickClass into an application with two distinct user experiences: one for students and another for teachers.

`MILESTONE 05 — TEACHER DASHBOARD`

---

# 06 — THE WORK BEHIND THE SCENES

<sub>05 NOVEMBER 2026 · CURRENT DEVELOPMENT</sub>

### 🛠️ Refining, debugging and organizing.

Not every development milestone is about launching a new feature.

Sometimes it's about going back, fixing things and making the existing application better.

**What I worked on:**
- Continued developing the teacher dashboard.
- Worked on subject creation and management.
- Updated database-related functionality.
- Modified the teacher screen.
- Worked on Git, GitHub and synchronizing local changes.
- Started organizing project documentation.

**A lesson worth remembering:**

Writing code is only part of software development. Maintaining it, managing versions and keeping everything organized matter just as much.

`MILESTONE 06 — PROJECT REFINEMENT`

---

# 07 — THE TOOLBOX

### 🧰 Technologies I'm working with.

| Technology | My use in ClickClass |
|---|---|
| Python | Core development |
| Streamlit | Application interface |
| dlib | Facial processing |
| face_recognition_models | Facial recognition models |
| Scikit-learn | SVM classification |
| NumPy | Numerical operations |
| Pandas | Data handling |
| Supabase | Database integration |
| bcrypt | Password hashing |
| Pillow | Image processing |
| Segno | QR code functionality |
| Git & GitHub | Version control |

---

# 08 — THE NEXT CHAPTER

### 🔮 Things I want to build.

ClickClass is still a work in progress. Here's what I'm looking forward to implementing:

- [ ] Complete teacher dashboard functionality.
- [ ] Finish subject creation and management.
- [ ] Implement automated attendance marking.
- [ ] Support multiple faces in classroom images.
- [ ] Improve unknown-face detection.
- [ ] Develop attendance history.
- [ ] Implement subject-wise attendance.
- [ ] Calculate attendance percentages.
- [ ] Build attendance analytics and reports.
- [ ] Improve application performance and reliability.

**The vision is bigger than the current implementation. And that's the exciting part.**

---

# 09 — THE LITTLE WINS

### 🏆 Progress worth celebrating.

| Milestone | Date |
|---|---|
| 💡 Initial idea | August 2026 |
| ⚙️ Environment setup | October 21 |
| 🏠 First home screen | October 25 |
| 🧠 ML pipeline | October 28 |
| 🔐 Student authentication | October 29 |
| 👩🏻‍🏫 Teacher dashboard | October 30 |
| 🛠️ Project refinement | November 5 |

I'll keep adding milestones as the project grows.

---

# 10 — A NOTE TO MY FUTURE SELF

Dear future me,

Remember when ClickClass was just an idea?

Remember when you were figuring out how facial embeddings worked, connecting the ML pipeline, dealing with errors and trying to make different parts of the application communicate?

This is where it started.

There will be more bugs, more features, more things to learn and probably a few moments when nothing works the way it should.

But that's software development.

I don't want to rush through this journey just to reach the final product. I want to understand what I'm building and enjoy the process of getting better.

Someday, when ClickClass is complete, I want to come back to this page and see how far I've come.

**Until then, one feature at a time. One bug at a time. One commit at a time.**

With curiosity and a little too much debugging,

**Preethi.** ♡

---

<sub>✳ CLICKCLASS · BUILT WITH CURIOSITY, CODE & COFFEE.</sub>

<sub>Created by Preethi Kondaveeti · Last updated: 05 November 2026</sub>

[Explore the repository →](https://github.com/aibyp/clickclass)