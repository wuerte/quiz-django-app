from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def first_question(request):
    new_game = Game(question_quantity = 3)
    new_game.save()
    new_game_id = new_game.id
    question_1 = Question.objects.get(id=1)
    context = {
        'question_1': question_1,
        'new_game': new_game,
    }
    return render(request, 'first_question.html', context)

def question(request):
    return render(request, 'question.html')