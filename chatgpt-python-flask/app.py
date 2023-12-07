import os
import openai
import requests
from flask import Flask, render_template, request, jsonify

# Initialize Flask App
app = Flask(__name__)

# Set OpenAI organization and API key directly
openai.organization = "org-ID"
API_KEY = "API-KEY"
openai.api_key = API_KEY

API_URL = "https://api.openai.com/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def interact_with_model(prompt):
    """Interacts with the fine-tuned model and returns the response."""
    data = {
        "model": "ft:gpt-3.5-turbo-0613:personal::8BjOv4eK",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(API_URL, headers=HEADERS, json=data)
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    else:
        error_message = response.json().get("error", {}).get("message", "Unknown error")
        return f"Error occurred while communicating with the API: {error_message}"

@app.route('/')
def home():
    """Render the chat interface."""
    return render_template("chat.html")

@app.route('/ask', methods=['POST'])
def ask():
    """Handle user input and get a response from the model."""
    user_input = request.form['user_input']
    response = interact_with_model(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
