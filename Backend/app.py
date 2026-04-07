from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

genai.configure(api_key="Gemini key")

model = genai.GenerativeModel("gemini-2.5-flash")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate_question", methods=["POST"])
def generate_question():

    data = request.json
    topic = data["topic"]

    prompt = f"""
Generate one technical interview question about {topic}.
Return only the question.
"""

    response = model.generate_content(prompt)

    return jsonify({"question": response.text})


@app.route("/evaluate", methods=["POST"])
def evaluate():

    data = request.json
    question = data["question"]
    answer = data["answer"]

    prompt = f"""
You are an interview evaluator.

Question:
{question}

Candidate Answer:
{answer}

Give:
Score out of 10
Strengths
Weaknesses
Suggestions
"""

    response = model.generate_content(prompt)

    return jsonify({"feedback": response.text})


if __name__ == "__main__":
    app.run(debug=True)
