from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from django.urls import reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import UploadCSVForm
import csv
import pandas as pd
from django.db.models import QuerySet
import random
import logging

logger = logging.getLogger(__name__)


def index(request):
    logout(request)
    recent_games = Game.objects.filter(completed_game=True).order_by('-created_at')[:10]
    context = { 'recent_games': recent_games }
    return render(request, 'index.html', context)


def first_question(request): 
    nickanme = request.POST['nickname']
    age = request.POST['age']
    gender = request.POST['gender']
    question_1 = Question.generate_random_question()
    new_game = Game(question_quantity = 5, actual_question = question_1.id, nickname=nickanme, age=age, gender=gender)
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
        game.percentage = percentage
        game.completed_game = True
        game.save()
        context = {
            'game': game,
            'percentage': percentage,
        }
        return render(request, 'summary.html', context)
    

def classification(request):
    classification_list = Game.objects.all().order_by('-total_score')[:20]
    context = {
        'classification_list': classification_list,
    }
    return render(request, 'classification.html', context)


def cancel_game(request, game_id):
    cancelled_game = Game.objects.get(id=game_id)
    cancelled_game.delete()
    return HttpResponseRedirect(reverse('index'))

@login_required
def maintenance(request): 
    return render(request, 'maintenance.html')


def add_record_question(request):
    question_description = request.POST['question_description']
    correct_answer = request.POST['correct_answer']
    answer_1 = request.POST['answer_1']
    answer_2 = request.POST['answer_2']
    answer_3 = request.POST['answer_3']
    answer_4 = request.POST['answer_4']

    new_question = Question(question_description=question_description, correct_answer=correct_answer, answer_1=answer_1, answer_2=answer_2, answer_3=answer_3, answer_4=answer_4)
    new_question.save()

    return HttpResponseRedirect(reverse('maintenance'))


def upload_csv(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded_file)
            
            for row in reader:
                question = Question(
                    correct_answer=row['correct_answer'],
                    question_description=row['question_description'],
                    answer_1=row['answer_1'],
                    answer_2=row['answer_2'],
                    answer_3=row['answer_3'],
                    answer_4=row['answer_4']
                )
                question.save()

            return render(request, 'success.html')
    else:
        form = UploadCSVForm()

    return render(request, 'upload_csv.html', {'form': form})


def analytics(request):
    return render(request, 'analytics.html')


def all_games(request):
    all_games = Game.objects.all().values()
    df = pd.DataFrame.from_records(all_games)
    table = df.to_html()
    new_table = table.replace("class=\"dataframe\"","class=\"table table-light table-bordered table-hover table-sm\"")
    # logger.info(f"LOGGER    df: {df}")
    logger.info(f"LOGGER    table: {new_table[:100]}")
    context = {'df': df,
               'table': new_table
               
               }
    return render(request, 'all_games.html', context)