# 🎓 AI-Powered Classroom Attendance System

An AI-based classroom attendance system that automatically detects and recognizes student faces from a classroom image and marks attendance in a database. The system uses **YOLOv8** for face detection, **DeepFace** for face recognition, and **Flask** for the web interface.

> ⚠️ **Note:** The current UI is minimal and intended only for testing and demonstration purposes. A complete user interface and dashboard will be added in future improvements.

---

## 🚀 Features

* 📸 Upload classroom image for attendance marking
* 🧠 Face detection using YOLOv8
* 🔍 Face recognition using DeepFace (Facenet512 model)
* 🗂 Automatic attendance marking with timestamp
* 🔄 Session-based attendance (each upload counts as a new session)
* 🚫 Duplicate prevention within same session
* 📊 Retrieve total attendance per student
* 🗄 SQLite database storage
* 🧩 Modular project structure for scalability

---

## 🏗 System Architecture

Upload Image → Face Detection (YOLOv8) → Face Recognition (DeepFace) → Attendance Database → Results Display

---

## 📁 Project Structure

```
AI-Attendance-System/
│── app.py
│── utils/
│     ├── database.py
│     ├── face_detect.py
│     └── face_recognize.py
│
├── templates/
│     ├── index.html
│     ├── result.html
│     └── total_attendance.html
│
├── static/
│     ├── css/
│     ├── uploads/
│     └── processed/
│
├── dataset/        # Student images (not included in repo)
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/yourusername/AI-Attendance-System.git
cd AI-Attendance-System
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 📥 Dataset Preparation

Store student images in the following format:

```
dataset/
    StudentName1/
        img1.jpg
        img2.jpg
    StudentName2/
        img1.jpg
```

Each folder name should represent the student identity.

---

## ▶️ Run the Application

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 📊 Attendance Logic

* Each image upload = one attendance session
* A student is marked only once per session
* Total attendance increases with each new session
* Attendance stored with date, time, and session ID

---

## 🧪 Current Limitations

* UI is basic and intended only for testing
* No authentication system yet
* No live webcam support (future work)
* Dataset must be manually maintained

---

## 🔮 Future Improvements

* Complete responsive UI dashboard
* Admin login system
* Attendance percentage calculation
* Live webcam attendance
* CSV/Excel export
* Cloud deployment
* Real-time classroom analytics

---

## 🛠 Technologies Used

* Python 3.10
* Flask
* YOLOv8 (Ultralytics)
* DeepFace
* OpenCV
* SQLite
* HTML / CSS

---

## 👨‍💻 Author

**Chandu Chendi**
Computer Science Engineering Student

---

## 📜 License

This project is for educational and research purposes.
