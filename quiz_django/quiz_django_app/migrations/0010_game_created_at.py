# Generated by Django 4.1.7 on 2023-03-30 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_django_app', '0009_game_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]