from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.index, name='index'),
    path('quiz/question', views.question, name='question'),
]
