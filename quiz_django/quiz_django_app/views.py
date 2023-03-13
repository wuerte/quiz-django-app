from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def first_question(request):
    question_1 = Question.objects.get(id=1)
    context = {
        'question_1': question_1,
    }
    return render(request, 'first_question.html', context)