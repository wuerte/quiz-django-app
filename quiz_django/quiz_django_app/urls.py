from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.index, name='index'),
    path('quiz/first_question', views.first_question, name='first_question'),
    path('quiz/question/<int:game_id>', views.question, name='question'),
    path('quiz/classification', views.classification, name='classification'),
    path('quiz/maintenance', views.maintenance, name='maintenance'),
    path('quiz/add_record_question', views.add_record_question, name='add_record_question'),
    path('quiz/cancel_game/<int:game_id>', views.cancel_game, name='cancel_game'),
    path('quiz/upload_csv', views.upload_csv, name="upload_csv"),
    path('quiz/analytics', views.analytics, name="analytics"),
    path('quiz/all_games', views.all_games, name="all_games"),
    path('quiz/general_stats', views.general_stats, name="general_stats"),
    path('quiz/generate_pdf', views.generate_pdf, name='generate_pdf'),
]
