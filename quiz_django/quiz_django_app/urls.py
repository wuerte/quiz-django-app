from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.index, name='index'),
    path('quiz/first_question', views.first_question, name='first_question'),
    path('quiz/question/<int:game_id>', views.question, name='question'),
    path('quiz/classification', views.classification, name='classification'),
    path('quiz/cancel_game/<int:game_id>', views.cancel_game, name='cancel_game'),
]
