import os
from openai import OpenAI

client = OpenAI()

def generate_ad_description(title, category, condition):
    prompt = f"Напиши привлекательное объявление для товара с названием '{title}', категорией '{category}' и состоянием '{condition}'."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты — маркетолог и копирайтер."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=150,
    )
    return response.choices[0].message.content.strip()

def summarize_feedbacks(feedbacks):
    prompt = "Вот отзывы пользователей:\n" + "\n".join(feedbacks) + "\nСделай краткую сводку их мнений."
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Ты — аналитик пользовательских отзывов."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=150,
    )
    return response.choices[0].message.content.strip()

