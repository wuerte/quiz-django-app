# Generated by Django 4.1.7 on 2023-03-12 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_quantity', models.IntegerField()),
                ('actual_question', models.IntegerField(default=1)),
                ('total_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_answer', models.IntegerField()),
                ('answer1', models.CharField(max_length=255)),
                ('answer2', models.CharField(max_length=255)),
                ('answer3', models.CharField(max_length=255)),
                ('answer4', models.CharField(max_length=255)),
            ],
        ),
    ]
