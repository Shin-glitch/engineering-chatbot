# EngiBot - Simple Chatbot for Engineering Queries

**EngiBot** is a smart web application that helps users understand basic engineering concepts by answering queries in a beginner-friendly and accurate way.

It uses Google’s **Gemini 1.5 Flash** model to process and generate responses through prompt engineering, dynamic TL;DRs, and prompt chaining with recent history.

---

## 🔧 Features

- 📘 Designed to answer engineering queries clearly
- ⚡ Uses Gemini 1.5 Flash LLM API via `google-generativeai`
- 🔁 Supports prompt chaining using last 3 user-bot interactions
- 🧠 Adds a TL;DR summary when responses are too long
- 📝 Saves interaction history to a local `history.json` file
- 🧹 Clear chat history anytime with a button click and has a clean UI with darkmode toggle

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Shin-glitch/engineering-chatbot.git
cd engineering-chatbot

```

### 2. Install Dependencies

Make sure Python 3 is installed. Then:

```bash
pip install -r requirements.txt
```

### 3. Set Your Gemini API Key

Open the `app.py` file and replace this line with your API key:

```python
genai.configure(api_key="AIzaSyC9Gc-ZRAiaSgLtEuu9MWjmjEvzwh0A3NI")
```

### 4. Run the Flask App

```bash
python app.py
```

### 5. Access the App in Your Browser

Go to [http://localhost:5000](http://localhost:5000)

---

## 🧠 Technologies Used

- Python (Flask)
- Google Generative AI API (`google-generativeai`)
- Gemini 1.5 Flash model
- HTML, CSS, JavaScript
- JSON for storing chat history

---

## 📸 Screenshots

![alt text](image-6.png)
![alt text](image-5.png)
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)

---

## 📄 License

This project is for academic and educational use only. Built as part of PE Project 2.

---

## 👤 Author

**Sadiq Shaikh**  
First-Year B.Tech-CSE(AI/ML)
