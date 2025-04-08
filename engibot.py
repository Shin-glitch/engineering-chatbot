import google.generativeai as genai

# Paste your Gemini API key here
genai.configure(api_key="AIzaSyC9Gc-ZRAiaSgLtEuu9MWjmjEvzwh0A3NI")

# Load the Gemini model
model = genai.GenerativeModel('gemini-1.5-pro-latest')
 

def ask_engineering_bot(question):
    response = model.generate_content(question)
    return response.text

print("👨‍🏫 Welcome to EngiBot (Gemini Edition)! Ask me any engineering question. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("👋 Bye! Keep engineering.")
        break

    try:
        response = ask_engineering_bot(user_input)
        print("EngiBot:", response)
    except Exception as e:
        print("⚠️ Error:", e)
