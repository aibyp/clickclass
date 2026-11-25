# 📸 ClickClass — AI-Powered Smart Attendance System

<p align="center">
  <strong>Smarter Classrooms. Automated Attendance. Powered by AI.</strong>
  <br/>
  An intelligent classroom attendance management system that uses Facial Recognition and Machine Learning to simplify and automate attendance tracking.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-Framework-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn" />
  <img src="https://img.shields.io/badge/dlib-Face%20Recognition-green" />
  <img src="https://img.shields.io/badge/Supabase-Backend-3ECF8E?logo=supabase" />
  <img src="https://img.shields.io/badge/Status-Implemented-success" />
</p>

---

## 🌟 About ClickClass

**ClickClass** is an AI-powered classroom attendance management system designed to replace traditional manual attendance methods with automated facial recognition.

The application enables teachers to upload classroom photographs, identify registered students using facial recognition and automatically generate attendance records.

It provides dedicated portals for teachers and students, integrating Artificial Intelligence, Machine Learning, Computer Vision and database management into a unified application.

Rather than requiring teachers to call out individual student names, ClickClass analyses classroom images and identifies students based on their registered facial data.

### 🎯 Our Mission

To make classroom attendance faster, smarter and more efficient through AI-driven automation.

## 🎯 Problem Statement

Traditional classroom attendance methods have several limitations:

- Manual attendance consumes valuable classroom time.
- Calling out student names becomes inefficient in larger classrooms.
- Maintaining attendance records manually can introduce errors.
- Managing attendance across multiple subjects can become complicated.
- Students and teachers often lack a unified system for tracking attendance.

**ClickClass addresses these challenges through an automated facial recognition-based attendance system.**

## ✨ Features

### 👨‍🏫 Teacher Portal

- Teacher registration and login.
- Secure password hashing using bcrypt.
- Personalized teacher dashboard.
- Create and manage multiple subjects.
- Generate and share unique subject codes.
- Upload multiple classroom photographs.
- AI-powered classroom face analysis.
- Automatic identification of registered students.
- Present and Absent classification.
- Attendance results for classroom sessions.
- Subject-wise attendance records.
- View enrolled student counts and class statistics.

### 👩‍🎓 Student Portal

- Face-based student registration.
- Facial authentication for returning students.
- Automatic student profile creation.
- Personalized student dashboard.
- Enroll in subjects using shared subject codes.
- View enrolled subjects.
- Track total classes and attended classes.
- View attendance information.
- Unenroll from subjects.

### 🧠 AI & Machine Learning

- Face detection using dlib.
- 128-dimensional facial embedding extraction.
- Facial feature representation.
- Linear Support Vector Machine (SVM) classifier.
- Student identification using trained facial embeddings.
- Face-distance-based verification.
- Multi-face detection in classroom photographs.
- Automatic recognition of registered students.

### 🗄️ Database Management

- Supabase integration.
- PostgreSQL-backed data storage.
- Teacher profile management.
- Student profile management.
- Subject management.
- Student-subject enrollment records.
- Attendance log storage.
- Retrieval of teacher and student attendance information.

---

## 🧠 How ClickClass Works

The application follows a structured workflow connecting student registration, facial recognition, classroom analysis and attendance management.

### 1. Student Registration

1. A student opens the Student Portal.
2. The student captures their photograph using the camera.
3. The system detects the face using dlib.
4. A 128-dimensional facial embedding is extracted.
5. The student's name and facial embedding are stored in Supabase.
6. The classifier is refreshed to include the newly registered student.

### 2. Student Authentication

1. The student opens the Student Portal.
2. The student captures a photograph using the camera.
3. The system extracts facial embeddings.
4. The trained classifier predicts the student's identity.
5. The predicted identity is verified using facial distance.
6. If recognized, the student is redirected to their dashboard.

### 3. Teacher Attendance Workflow

1. The teacher logs into the Teacher Portal.
2. The teacher selects a subject.
3. Classroom photographs are uploaded.
4. The application processes each photograph.
5. The face recognition pipeline detects and identifies students.
6. Recognized students are matched against the subject enrollment list.
7. Each enrolled student is classified as Present or Absent.
8. The teacher reviews the attendance results.
9. Attendance records are stored in Supabase.

### 4. Attendance Tracking

- Teachers can view attendance records associated with their subjects.
- Students can view their enrolled subjects and attendance statistics.
- Attendance information is retrieved from the database.
- Subject-wise attendance information is organized for easier tracking.

---

## 🔬 AI/ML Architecture

The facial recognition pipeline is the core intelligence behind ClickClass.

It is implemented in:

`src/pipelines/face_pipeline.py`

### Facial Recognition Pipeline

**Step 1 — Face Detection**

The dlib frontal face detector identifies faces in the input image.

**Step 2 — Facial Landmark Detection**

The dlib shape predictor identifies facial landmarks required for facial representation.

**Step 3 — Feature Extraction**

The dlib face recognition model generates a 128-dimensional facial descriptor for each detected face.

**Step 4 — Model Training**

The facial embeddings stored in the student database are used to train a Support Vector Machine classifier.

The implementation uses:

- Algorithm: Support Vector Machine
- Classifier: `sklearn.svm.SVC`
- Kernel: Linear
- Probability estimation: Enabled
- Class weighting: Balanced

**Step 5 — Student Identification**

The trained classifier predicts the identity associated with a detected face.

**Step 6 — Face Verification**

The predicted student's stored facial embedding is compared against the newly extracted embedding using Euclidean distance.

The current implementation uses a resemblance threshold of `0.6`.

**Step 7 — Attendance Generation**

Recognized student IDs are compared with the subject enrollment records to determine attendance status.

### AI Pipeline Overview

```text
       Input Classroom Image
                 |
                 v
          Face Detection
              (dlib)
                 |
                 v
       Facial Landmark Detection
                 |
                 v
       128D Facial Embeddings
                 |
                 v
       Trained SVM Classifier
                 |
                 v
       Predicted Student ID
                 |
                 v
       Euclidean Distance Check
                 |
                 v
        Identity Verification
                 |
                 v
       Subject Enrollment Check
                 |
                 v
       Present / Absent Status
                 |
                 v
        Supabase Attendance Logs
```

---

## 🏗️ System Architecture

ClickClass follows a modular architecture that separates the user interface, AI pipeline and database operations.

```text
                 CLICKCLASS
                      |
                      v
              Streamlit Application
                      |
             Application Routing
                      |
          +-----------+-----------+
          |                       |
          v                       v
     Teacher Portal          Student Portal
          |                       |
          v                       v
   Subject Management       Face Authentication
   Classroom Analysis      Student Registration
   Attendance Records      Subject Enrollment
          |                       |
          +-----------+-----------+
                      |
                      v
              Face Recognition
                   Pipeline
                      |
             +--------+--------+
             |                 |
             v                 v
        Face Detection    SVM Classifier
             |                 |
             +--------+--------+
                      |
                      v
              Supabase Backend
                      |
                      v
              PostgreSQL Database
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application development |
| Streamlit | Interactive application interface |
| dlib | Face detection and facial processing |
| face_recognition_models | Facial landmark and recognition models |
| Scikit-learn | SVM-based classification |
| NumPy | Numerical computations and embeddings |
| Pandas | Attendance data processing |
| Supabase | Backend and database integration |
| PostgreSQL | Structured data storage |
| bcrypt | Password hashing |
| Pillow | Image processing |
| Segno | QR code generation dependency |

### Development Tools

- Visual Studio Code
- Git
- GitHub
- Python Virtual Environment

---

## 📁 Project Structure

```text
clickclass/
│
├── app.py
│
├── requirements.txt
│
├── README.md
├── DEVELOPMENT_JOURNAL.md
│
└── src/
    │
    ├── components/
    │   ├── header.py
    │   ├── footer.py
    │   ├── subject_card.py
    │   ├── dialog_create_subject.py
    │   ├── dialog_share_subject.py
    │   ├── dialog_add_photo.py
    │   ├── dialog_attendance_results.py
    │   ├── dialog_enroll.py
    │   └── dialog_auto_enroll.py
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

---

## ⚙️ Installation and Setup

Follow these instructions to run ClickClass locally.

### Prerequisites

- Python installed on your system.
- Git installed.
- A Supabase account and configured project.
- Camera access for student registration and authentication.

### 1. Clone the Repository

```bash
git clone https://github.com/aibyp/clickclass.git
```

### 2. Navigate to the Project Directory

```bash
cd clickclass
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

**Note:** The project uses `dlib-bin` and `face_recognition_models`. Dependency installation may require compatible Python versions and platform-specific build support.

### 6. Configure Supabase

1. Create a Supabase project.
2. Configure the database tables required by the application.
3. Configure the Supabase connection in `src/database/config.py`.
4. Add the required credentials securely.

Never commit private API keys, database credentials or passwords to GitHub.

### 7. Run ClickClass

```bash
streamlit run app.py
```

The application will start locally. Open the URL displayed in your terminal to access ClickClass.

---

## 🔐 Security Considerations

ClickClass incorporates security-related mechanisms such as:

- bcrypt password hashing for teacher accounts.
- Database-backed authentication.
- Separate teacher and student interfaces.
- Facial identity verification.
- Secure credential handling recommendations.

**Important:** Facial recognition is a biometric identification mechanism, not a complete liveness-detection system. Additional safeguards and privacy controls should be considered before production deployment.

---

## 🚀 Future Enhancements

Potential areas for further development include:

- Advanced facial recognition under varying lighting conditions.
- Improved recognition accuracy and model evaluation.
- Facial liveness detection to reduce spoofing risks.
- More detailed attendance analytics and visualizations.
- Downloadable attendance reports.
- Improved biometric data protection and management.
- Enhanced scalability for larger institutions.
- Automated testing and deployment workflows.

---

## 📖 Development Journey

ClickClass started as an idea in August 2026 and evolved into a complete implementation through experimentation, development, debugging and continuous improvement.

The project provided hands-on experience in:

- Applying Machine Learning to real-world problems.
- Building facial recognition pipelines.
- Integrating AI models into interactive applications.
- Designing database-backed applications.
- Developing teacher and student workflows.
- Working with Git and GitHub for collaborative development.

I maintain a separate development journal to document the milestones, implementation decisions, technical challenges and lessons learned.

**[Explore the ClickClass Development Journal](DEVELOPMENT_JOURNAL.md)**

---

## 👩‍💻 Developer

**Preethi Kondaveeti**

B.Tech — Computer Science and Engineering  
Specialization: Artificial Intelligence and Machine Learning

Interested in Artificial Intelligence, Machine Learning, Computer Vision and building practical AI-powered applications.

- GitHub: [@aibyp](https://github.com/aibyp)
- Project: [ClickClass](https://github.com/aibyp/clickclass)

---

## ⭐ Support the Project

If you find ClickClass interesting:

- Explore the source code.
- Star the repository.
- Share feedback and suggestions.
- Contribute ideas for future improvements.

**Repository:** https://github.com/aibyp/clickclass

---

<p align="center">
  <strong>CLICKCLASS — Making Attendance Smarter, One Classroom at a Time. 📸</strong>
  <br/>
  <sub>Built with Python, AI, Machine Learning and a passion for solving real-world problems.</sub>
</p>
