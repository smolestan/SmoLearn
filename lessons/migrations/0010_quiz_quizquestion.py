# Generated by Django 2.2.1 on 2019-05-30 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0009_homework_date_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Course')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Lesson')),
            ],
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_content', models.CharField(max_length=64)),
                ('quiz_correct_answer', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=64)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Course')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.Quiz')),
            ],
        ),
    ]
