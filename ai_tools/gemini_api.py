import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_ad_description(title, category, condition):
    prompt = f"Напиши привлекательное объявление для товара с названием '{title}', категорией '{category}' и состоянием '{condition}'."
    response = model.generate_content(prompt)
    return response.text.strip()

def summarize_feedbacks(feedbacks):
    joined_feedbacks = "\n".join(feedbacks)
    prompt = f"Вот отзывы пользователей:\n{joined_feedbacks}\nСделай краткую сводку их мнений."
    response = model.generate_content(prompt)
    return response.text.strip()
