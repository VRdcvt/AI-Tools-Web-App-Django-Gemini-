# AI Tools Web App (Django + Gemini)

Веб-приложение на Django, демонстрирующее работу с языковыми моделями (LLM) для решения прикладных задач:
- генерация описания объявления на основе параметров
- суммирование отзывов пользователей

## 🔧 Используемые технологии

- Python 3.10+
- Django 5+
- Gemini API (или OpenAI при замене)
- HTML (Django Templates)
- Bootstrap (для базовой вёрстки)
- `.env` файл для ключей

---

## 🚀 Возможности

### 1. Генератор описаний
Выбираешь категорию, состояние и название — получаешь сгенерированный текст объявления с маркетинговым уклоном.

**Пример промта:**
Сгенерируй привлекательное описание объявления для товара:
Название: {title}
Категория: {category}
Состояние: {condition}
Скриншот:
![2025-06-10_01-18-45](https://github.com/user-attachments/assets/19685047-0b1e-47e8-b9b6-5912082ade2d)


### 2. Анализ отзывов
Вставляешь набор отзывов — получаешь краткое резюме на естественном языке.

**Пример промта:**
Проанализируй отзывы пользователей и выдели основные сильные и слабые стороны продукта.
Отзывы:
{список отзывов}
Скриншот:
![2025-06-10_01-21-00](https://github.com/user-attachments/assets/3d652a7a-32ee-4873-bc54-e4a5d82984b3)


## 📂 Установка

```bash
git clone https://github.com/VRdcvt/AI-Tools-Web-App-Django-Gemini-.git
cd ai_tools_project
python -m venv venv
source venv/bin/activate  # или venv\\Scripts\\activate на Windows
pip install -r requirements.txt
```
Переименуй файл .env.example в .env и добавь в него ключ Gemini или OpenAI.

## ▶ Запуск
```bash
python manage.py migrate
python manage.py runserver
```
