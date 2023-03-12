from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Game(models.Model):
    question_quantity = models.IntegerField()
    actual_question = models.IntegerField(default=1)
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