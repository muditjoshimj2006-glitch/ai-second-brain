# 🧠 AI Second Brain

An AI-powered Personal Knowledge Management System that allows users to upload PDF documents, automatically extract text, and generate concise AI-powered summaries using Google's Gemini API.

---

## 🚀 Features

- 📄 Upload PDF documents
- 📖 Extract text using PyPDF
- 🤖 AI-powered document analysis
- 📝 Generate clean and professional summaries
- ⚡ REST API built with FastAPI
- 📚 Interactive Swagger Documentation

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Google Gemini API
- PyPDF
- Uvicorn
- Python Dotenv

---

## 📂 Project Structure

```
ai_second_brain/
│
├── app/
│   ├── routers/
│   ├── services/
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   └── ...
│
├── uploads/
├── requirements.txt
├── .env (Not Included)
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-second-brain.git
```

Move into the project

```bash
cd ai-second-brain
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
API_KEY=YOUR_GEMINI_API_KEY
DATABASE_URL=sqlite:///second_brain.db
SECRET_KEY=YOUR_SECRET_KEY
ALGO=HS256
```

---

## ▶️ Run Project

```bash
uvicorn app.main:app --reload
```

---

## 📚 API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 📸 Workflow

```
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Google Gemini
      │
      ▼
Generate Summary
      │
      ▼
JSON Response
```

---

## 🎯 Future Improvements

- User Authentication (JWT)
- Save Notes to Database
- Search Notes
- Chat with Uploaded PDFs
- AI Q&A
- Document History
- Multi-file Upload

---

##  License

<<<<<<< HEAD
This project is licensed under the MIT License.
=======
This project is licensed under the MIT License.
>>>>>>> 207436d61b81495e5fa9d7c42a154082f2de0d23
