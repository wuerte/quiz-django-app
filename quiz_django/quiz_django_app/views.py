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

    new_game = Game(question_quantity = 5, actual_question = question_1.id)
    
    new_game.save()
    new_game.questions_used.add(question_1)
    new_game.save()

    

    context = {
        'question_1': question_1,
        'game': new_game,
    }
    return render(request, 'first_question.html', context)


def question(request, game_id):

    game = Game.objects.get(id=game_id)
    game.question_counter += 1
    
    #checking if the our answer is correct
    answer = int(request.POST['answer'])
    previous_question = Question.objects.get(id = game.actual_question)
    correct_answer = previous_question.correct_answer
    if answer == correct_answer:
        game.total_score += 1
    

    if game.question_counter <= game.question_quantity:
        while True:
            new_question = Question.generate_random_question()
            if not game.questions_used.filter(id=new_question.id).exists():    
                game.questions_used.add(new_question)
                break

        game.actual_question = new_question.id
        game.save()

        context = {
            'question': new_question,
            'game': game,
        }
        return render(request, 'question.html', context)

    else:
        percentage = ( game.total_score / game.question_quantity ) * 100
        context = {
            'game': game,
            'percentage': percentage,
        }
        return render(request, 'summary.html', context)