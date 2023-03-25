from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
import random


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def first_question(request):
    
    question_1 = Question.generate_random_question()

    new_game = Game(question_quantity = 3, actual_question = question_1.id)
    new_game.save()

    context = {
        'question_1': question_1,
        'game': new_game,
    }
    return render(request, 'first_question.html', context)

def question(request, game_id):

    all_questions_number = Question.get_all_questions()
    random_question_id = random.randint(1, all_questions_number)
    question = Question.objects.get(id=random_question_id)
    
    game = Game.objects.get(id=game_id)
    game.actual_question += 1
    game.save()

    #add question id to arguments of methods, pass it in question.html and add scoring mechanism below
    answer = request.POST['answer']


    context = {
        'question_number': question,
        'game': game,
    }

    return render(request, 'question.html', context)