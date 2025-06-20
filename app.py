from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def chat_with_ollama(prompt, model="llama3"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(url, json=payload)
        return response.json()["response"]
    except Exception as e:
        return f"Error: {e}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']
    bot_reply = chat_with_ollama(user_input)
    return jsonify({'response': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
