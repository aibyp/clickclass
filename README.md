# 📸 ClickClass – AI-Powered Smart Attendance System

<p align="center">
  <strong>Smart Attendance. Powered by AI.</strong>
  <br/>
  An intelligent attendance management system built using Python, Computer Vision and Machine Learning.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-Framework-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn" />
  <img src="https://img.shields.io/badge/Supabase-Database-green?logo=supabase" />
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow" />
</p>

---

## 🌟 About ClickClass

ClickClass is an AI-powered attendance management system that I am building to simplify traditional classroom attendance using Facial Recognition and Machine Learning.

The idea behind this project is to reduce the time teachers spend taking manual attendance and make the process more efficient through automation.

The system is being developed with separate interfaces for teachers and students, facial recognition capabilities, authentication, and database integration.

My goal is to turn this idea into a practical application that combines Artificial Intelligence, Computer Vision, and software development to solve a real-world problem.

## 🎯 Problem Statement

Traditional attendance management can be time-consuming and prone to manual errors, especially in classrooms with a large number of students.

ClickClass aims to address these challenges through an AI-based approach.

**The vision:**
- Reduce manual attendance work.
- Identify registered students using facial recognition.
- Simplify student and teacher interactions.
- Maintain organized attendance records.
- Eventually provide attendance analytics and reports.

## ✨ Features

### Developed functionality

- Separate teacher and student interfaces.
- Teacher registration and login.
- Password hashing using bcrypt.
- Student face-based authentication.
- Face detection using dlib.
- 128-dimensional facial embeddings.
- SVM-based student classification.
- Supabase database integration.
- Custom Streamlit interface.
- Initial teacher dashboard with separate tabs.

### Work in progress

- Complete subject creation and management.
- Automated classroom attendance marking.
- Multiple-face recognition in classroom images.
- Attendance history and tracking.
- Subject-wise attendance management.
- Attendance percentage calculations.
- Teacher analytics and reporting.

## 🧠 How It Works

The intended attendance workflow is:

1. A teacher logs into the application.
2. The teacher selects a subject.
3. A classroom image is captured or uploaded.
4. The system detects faces using dlib.
5. Facial embeddings are extracted.
6. An SVM classifier identifies registered students.
7. Recognized students are used to generate attendance records.
8. Teachers can eventually view attendance history and reports.

*The complete automated attendance workflow is still under development.*

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Streamlit | User interface |
| dlib | Face detection and facial processing |
| face_recognition_models | Facial recognition models |
| Scikit-learn | SVM classification |
| NumPy | Numerical computations |
| Pandas | Data processing |
| Supabase | Database and backend integration |
| bcrypt | Password hashing |
| Pillow | Image processing |
| Segno | QR code functionality |
| Git | Version control |
| GitHub | Source code hosting |

## 🏗️ Project Architecture

The application is organized into separate modules to keep the code maintainable and easier to extend.

```text
clickclass/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── README.md
├── DEVELOPMENT_JOURNAL.md
│
└── src/
    ├── components/
    │   ├── header.py
    │   └── footer.py
    │
    ├── database/
    │   ├── config.py
    │   └── db.py
    │
    ├── pipelines/
    │   └── face_pipeline.py
    │
    ├── screens/
    │   ├── home_screen.py
    │   ├── teacher_screen.py
    │   └── student_screen.py
    │
    └── ui/
        └── base_layout.py
```

*This represents the main project structure and may evolve during development.*

## ⚙️ Installation and Setup

Follow these steps to run ClickClass locally.

### 1. Clone the repository

```bash
git clone https://github.com/aibyp/clickclass.git
```

### 2. Navigate to the project directory

```bash
cd clickclass
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Supabase

Set up your Supabase project and provide the required credentials through your local configuration or environment variables.

Never upload secret keys, passwords, or database credentials to GitHub.

### 7. Run the application

```bash
streamlit run app.py
```

## 🔐 Security

- Passwords are hashed using bcrypt.
- Database credentials should be stored securely.
- Secret keys and environment files should not be committed to the repository.
- Facial recognition and authentication workflows are being developed and tested.

## 🗺️ Future Roadmap

My upcoming goals for ClickClass:

- [ ] Complete teacher dashboard.
- [ ] Complete subject management.
- [ ] Implement automated attendance marking.
- [ ] Improve multi-face recognition.
- [ ] Handle unknown and unregistered faces.
- [ ] Implement attendance history.
- [ ] Develop attendance analytics.
- [ ] Add attendance percentage calculations.
- [ ] Improve application reliability and performance.

## 📖 Development Journey

Every project has a story behind the code.

ClickClass started as an idea in August 2026 and has gradually evolved through experimentation, implementation, debugging, and continuous learning.

I maintain a separate development journal to document the milestones, technical challenges, features, and lessons learned throughout the process.

**➡️ [Explore the ClickClass Development Journal](DEVELOPMENT_JOURNAL.md)**

## 👩‍💻 About the Developer

**Preethi Kondaveeti**

B.Tech CSE – Artificial Intelligence and Machine Learning.

I'm passionate about Artificial Intelligence, Machine Learning, Computer Vision, and building applications that solve real-world problems.

ClickClass is one of my hands-on projects where I'm exploring how AI and software engineering can come together to create practical solutions.

## ⭐ Support the Project

If you find ClickClass interesting, feel free to explore the repository, follow its development, and share your feedback.

**GitHub Repository:** [aibyp/clickclass](https://github.com/aibyp/clickclass)

---

<p align="center">
  <strong>Built with curiosity, code, and continuous learning. ❤️</strong>
  <br/>
  <sub>ClickClass · 2026</sub>
</p>