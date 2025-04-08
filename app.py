from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
import json

app = Flask(__name__)

# Set your Gemini API key
genai.configure(api_key="AIzaSyC9Gc-ZRAiaSgLtEuu9MWjmjEvzwh0A3NI")

# Use the flash model for faster response
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# JSON file to store chat history
HISTORY_FILE = "history.json"

# Helper function to load chat history
def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Helper function to save chat history
def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["question"]
    history = load_history()

    # Build chat history for context (only last few interactions)
    formatted_history = []
    for qna in history[-3:]:  # Use last 3 turns for context
        if qna.get("user"):
            formatted_history.append({"role": "user", "parts": qna["user"]})
        if qna.get("bot"):
            formatted_history.append({"role": "model", "parts": qna["bot"]})

    # Static prompt to define the assistant’s behavior
    static_prompt = {
        "role": "user",
        "parts": "You are EngiBot, a helpful AI assistant that answers engineering-related questions in a clear, concise, and beginner-friendly way. Stick to engineering topics and avoid non-technical discussions."
    }

    try:
        # Start chat session with prompt + limited history
        chat = model.start_chat(history=[static_prompt, *formatted_history])
        chat.send_message(user_input)
        response_text = chat.last.text.strip()

        # If the response is too long, ask for TL;DR
        if len(response_text) > 1000:
            summary_prompt = f"Please provide a 1–2 line TL;DR of the following:\n\n{response_text}"
            chat.send_message(summary_prompt)
            tldr = chat.last.text.strip()
            response_text += f"\n\n🔍 **TL;DR:** {tldr}"

    except Exception as e:
        response_text = f"Oops! Something went wrong: {e}"

    # Save current interaction to history
    history.append({
        "user": user_input,
        "bot": response_text
    })
    save_history(history)

    return jsonify({"response": response_text})

@app.route("/clear", methods=["POST"])
def clear():
    save_history([])  # clear the JSON file
    return jsonify({"status": "Chat history cleared."})

if __name__ == "__main__":
    app.run(debug=True)
