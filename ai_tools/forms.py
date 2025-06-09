from django import forms

class DescriptionForm(forms.Form):
    title = forms.CharField(label='Название товара')
    category = forms.CharField(label='Категория')
    condition = forms.CharField(label='Состояние')

class FeedbackForm(forms.Form):
    feedbacks = forms.CharField(widget=forms.Textarea, label='Отзывы (через новую строку)')
