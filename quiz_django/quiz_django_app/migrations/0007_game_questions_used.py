# Generated by Django 4.1.7 on 2023-03-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_django_app', '0006_alter_game_question_counter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='questions_used',
            field=models.ManyToManyField(to='quiz_django_app.question'),
        ),
    ]