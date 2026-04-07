import google.generativeai as genai

genai.configure(api_key="AIzaSyARIxVoQ2Ezdab3LQzB6sJZq2hvMnyPMs0")

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_question(topic):

    prompt = f"""
You are a technical interviewer.

Generate ONE interview question based on this topic:

Topic: {topic}

Return only the question.
"""

    response = model.generate_content(prompt)

    return response.text.strip()


def evaluate_answer(question, answer):

    prompt = f"""
You are an AI interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate and provide:

Score out of 10
Strengths
Weaknesses
Suggestions
"""

    response = model.generate_content(prompt)

    return response.text