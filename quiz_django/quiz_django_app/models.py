from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import random


class Question(models.Model):
    correct_answer = models.IntegerField(validators=[MinValueValidator(0.99), MaxValueValidator(4.01)])
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
    

class Game(models.Model):
    question_quantity = models.IntegerField(help_text = "value specified by user, how many question are in this game")
    actual_question = models.IntegerField(help_text = "id of actual question")
    question_counter = models.IntegerField(default=1, help_text = "counts number of questions answered in this game")
    total_score = models.IntegerField(default=0)
    # question_used = models.CommaSeparatedIntegerField(max_length=200)
    questions_used= models.ManyToManyField(Question)
    nickname = models.CharField(max_length=255, null=True)
    percentage = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    completed_game = models.BooleanField(default=False)