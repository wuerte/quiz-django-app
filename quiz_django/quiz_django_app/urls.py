from django.urls import path
from . import views

urlpatterns = [
    path('quiz_django_app/', views.index, name='index'),
]
