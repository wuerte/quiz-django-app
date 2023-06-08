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
    df_len = df.shape[0]
    table = df.to_html()
    new_table = table.replace("class=\"dataframe\"","class=\"table table-light table-bordered table-hover table-sm\"")
    # logger.info(f"LOGGER    df: {df}")
    context = {'df': df,
               'table': new_table,
               'df_len': df_len               
               }
    return render(request, 'all_games.html', context)


def general_stats(request):
    all_games = Game.objects.all().values()
    df = pd.DataFrame.from_records(all_games)
    
    df_describe = df.describe()
    table = df_describe.to_html()
    new_table = table.replace("class=\"dataframe\"","class=\"table table-light table-bordered table-hover table-sm\"")

    #age stats
    def age_prct(age_1, age_2):
        all_age = df['age'].count()
        age = df[df['age'].between(age_1, age_2)].count()[0]
        age_prct = age / all_age
        age_prct_str = f"{round(age_prct*100, 2)}%"
        return age_prct_str

    age_mean = df['age'].mean()
    all_age = df['age'].count()
    age_0_prct_str = age_prct(1,9)
    age_10_prct_str = age_prct(10,19)
    age_20_prct_str = age_prct(20,29)
    age_30_prct_str = age_prct(30,39)
    age_40_prct_str = age_prct(40,49)
    age_50_prct_str = age_prct(50,59)
    age_60_prct_str = age_prct(60,69)
    age_70_prct_str = age_prct(70,79)
    age_80_prct_str = age_prct(80,89)
    age_90_prct_str = age_prct(90,99)
 
    #gender stats
    # male = df.loc[df['gender'] == 'M'].shape[0]
    male = df[df['gender'] == 'M'].shape[0]
    female = df[df['gender'] == 'F'].shape[0]
    all_gender = df['gender'].count()
    male_prct = male / all_gender
    female_prct = female / all_gender
    male_prct_str = f"{round(male_prct*100, 2)}%"
    female_prct_str = f"{round(female_prct*100, 2)}%"
    male_age_avg = df[df['gender'] == 'M']['age'].mean()
    female_age_avg = df[df['gender'] == 'F']['age'].mean()
    male_score_avg = df[df['gender'] == 'M']['total_score'].mean()
    female_score_avg = df[df['gender'] == 'F']['total_score'].mean()
    logger.info(f"LOGGER    test1: {male_age_avg}, test2: {female_age_avg} ")

    #game stats
    score_avg = df['total_score'].mean()
    score_avg_str = f"{round(score_avg, 2)}"
    
    context = { 'new_table': new_table,
                'age_mean': age_mean,
                'female_prct': female_prct_str,
                'male_prct': male_prct_str,
                'age_0_prct_str': age_0_prct_str,
                'age_10_prct_str': age_10_prct_str,
                'age_20_prct_str': age_20_prct_str,
                'age_30_prct_str': age_30_prct_str,
                'age_40_prct_str': age_40_prct_str,
                'age_50_prct_str': age_50_prct_str,
                'age_60_prct_str': age_60_prct_str,
                'age_70_prct_str': age_70_prct_str,
                'age_80_prct_str': age_80_prct_str,
                'age_90_prct_str': age_90_prct_str,
                'male_age_avg': male_age_avg,
                'female_age_avg': female_age_avg,
                'score_avg': score_avg_str,
                'male_score_avg': male_score_avg,
                'female_score_avg': female_score_avg,
               }
    return render(request, 'general_stats.html', context)