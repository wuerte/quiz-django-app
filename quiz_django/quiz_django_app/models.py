from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import random


class Game(models.Model):
    question_quantity = models.IntegerField(help_text = "value specified by user, how many question are in this game")
    actual_question = models.IntegerField(help_text = "id of actual question")
    question_counter = models.IntegerField(default=1)
    total_score = models.IntegerField(default=0)


class Question(models.Model):
    correct_answer = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    question_description = models.CharField(max_length=255, null=True)
    answer_1 = models.CharField(max_length=255)
    answer_2 = models.CharField(max_length=255)
    answer_3 = models.CharField(max_length=255)
    answer_4 = models.CharField(max_length=255)

    def __str__(self):
        return "question nr: " + str(self.id)
       
    @classmethod
    def generate_random_question(self):
        all_questions = Question.objects.all()
        all_questions_number = len(all_questions)
        random_question_id = random.randint(1, all_questions_number)
        question = Question.objects.get(id=random_question_id)
        return question