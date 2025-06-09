from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_description, name='generate_description'),
    path('summarize/', views.summarize_feedback, name='summarize_feedback'),
]
