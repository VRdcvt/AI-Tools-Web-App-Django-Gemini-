from django.shortcuts import render
from .forms import DescriptionForm, FeedbackForm
from . import gemini_api as fake_gpt  # ✅ подключаем Gemini как "fake_gpt"

def generate_description(request):
    description = None
    if request.method == 'POST':
        form = DescriptionForm(request.POST)
        if form.is_valid():
            description = fake_gpt.generate_ad_description(  # ✅ вызываем из gemini_api
                form.cleaned_data['title'],
                form.cleaned_data['category'],
                form.cleaned_data['condition']
            )
    else:
        form = DescriptionForm()
    return render(request, 'ai_tools/generate_description.html', {'form': form, 'description': description})

def summarize_feedback(request):
    summary = None
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedbacks = form.cleaned_data['feedbacks'].split('\n')
            summary = fake_gpt.summarize_feedbacks(feedbacks)  # ✅ вызываем из gemini_api
    else:
        form = FeedbackForm()
    return render(request, 'ai_tools/summarize_feedback.html', {'form': form, 'summary': summary})

