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
![2025-06-10_01-18-45](https://github.com/user-attachments/assets/0e3e9e94-2212-486c-bb95-2f0882a9b31c)

### 2. Анализ отзывов
Вставляешь набор отзывов — получаешь краткое резюме на естественном языке.
**Пример промта:**
Проанализируй отзывы пользователей и выдели основные сильные и слабые стороны продукта.
Отзывы:
{список отзывов}
![2025-06-10_01-21-00](https://github.com/user-attachments/assets/8f416fff-ec25-4724-bca3-71c2bfa9c26e)

## 📂 Установка

```bash
git clone <репозиторий>
cd ai_tools_project
python -m venv venv
source venv/bin/activate  # или venv\\Scripts\\activate на Windows
pip install -r requirements.txt

▶ Запуск
```bash
python manage.py migrate
python manage.py runserver
