# Generated by Django 4.1.7 on 2023-03-12 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_django_app', '0003_alter_question_correct_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
