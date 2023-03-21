from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
import random


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

def question(request, game_id):
    all_questions_number = Question.get_all_questions()
    random_question_id = random.randint(1, all_questions_number)
    actual_question = Question.objects.get(id=random_question_id)

    game = Game.objects.get(id=game_id)

    context = {
        'question_number': actual_question,
        'game': game
    }

    return render(request, 'question.html', context)