# Generated by Django 4.1.7 on 2023-04-02 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_django_app', '0010_game_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='completed_game',
            field=models.BooleanField(default=False),
        ),
    ]