from django.db import models

class Game(models.Model):
    question_quantity = models.IntegerField()
    actual_question = models.IntegerField(default=1)
    total_score = models.IntegerField(default=0)


class Question(models.Model):
    correct_answer = models.IntegerField()
    answer1 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    answer3 = models.CharField(max_length=255)
    answer4 = models.CharField(max_length=255)

    def __str__(self):
        return "question nr: " + str(self.id)