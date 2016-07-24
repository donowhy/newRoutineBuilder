# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 02:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='auxExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isCompound', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exerciseName', models.CharField(max_length=30)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='exerciseCompare2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genderMale', models.BooleanField()),
                ('bodyWeight', models.IntegerField(max_length=10)),
                ('beginner', models.IntegerField(max_length=10)),
                ('novice', models.IntegerField(max_length=10)),
                ('intermediate', models.IntegerField(max_length=10)),
                ('advanced', models.IntegerField(max_length=10)),
                ('elite', models.IntegerField(max_length=10)),
                ('exerciseActual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.exercise')),
            ],
        ),
        migrations.CreateModel(
            name='exerciseForRoutine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exerciseSets', models.IntegerField(max_length=10)),
                ('exerciseReps', models.IntegerField(max_length=10)),
                ('exerciseFrequency', models.IntegerField(max_length=10)),
                ('beginner', models.IntegerField(max_length=10)),
                ('novice', models.IntegerField(max_length=10)),
                ('intermediate', models.IntegerField(max_length=10)),
                ('advanced', models.IntegerField(max_length=10)),
                ('elite', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='generatedRoutineExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sets', models.IntegerField(max_length=3)),
                ('reps', models.IntegerField(max_length=3)),
                ('notes', models.CharField(max_length=75)),
                ('routineDay', models.CharField(choices=[('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thursday', 'thursday'), ('friday', 'friday')], default='monday', max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='muscle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muscleName', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='muscleGroupMajor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exerciseActual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.exercise')),
                ('muscleActual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.muscle')),
            ],
        ),
        migrations.CreateModel(
            name='muscleGroupMinor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exerciseActual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.exercise')),
                ('muscleActual', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.muscle')),
            ],
        ),
        migrations.CreateModel(
            name='muscleStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muscleStrength', models.FloatField(max_length=10)),
                ('muscleScore', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routineName', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('upVote', models.IntegerField(max_length=10)),
                ('downVote', models.IntegerField(max_length=10)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='routineEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BenchWeight', models.IntegerField(max_length=10)),
                ('BenchReps', models.IntegerField(max_length=10)),
                ('SquatWeight', models.IntegerField(max_length=10)),
                ('SquatReps', models.IntegerField(max_length=10)),
                ('DeadWeight', models.IntegerField(max_length=10)),
                ('DeadReps', models.IntegerField(max_length=10)),
                ('PullupWeight', models.IntegerField(max_length=10)),
                ('PullupReps', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Stats2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BenchWeight', models.IntegerField(max_length=10)),
                ('BenchReps', models.IntegerField(max_length=10)),
                ('SquatWeight', models.IntegerField(max_length=10)),
                ('SquatReps', models.IntegerField(max_length=10)),
                ('DeadWeight', models.IntegerField(max_length=10)),
                ('DeadReps', models.IntegerField(max_length=10)),
                ('PullupWeight', models.IntegerField(max_length=10)),
                ('PullupReps', models.IntegerField(max_length=10)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='musclestats',
            name='entryForm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.routineEntry'),
        ),
        migrations.AddField(
            model_name='musclestats',
            name='muscleActual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.muscle'),
        ),
        migrations.AddField(
            model_name='generatedroutineexercise',
            name='entryForm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.routineEntry'),
        ),
        migrations.AddField(
            model_name='generatedroutineexercise',
            name='exerciseActual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.exercise'),
        ),
        migrations.AddField(
            model_name='exerciseforroutine',
            name='actualRoutine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.routine'),
        ),
        migrations.AddField(
            model_name='exerciseforroutine',
            name='exerciseName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.exercise'),
        ),
        migrations.AddField(
            model_name='auxexercise',
            name='exerciseActual',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.exercise'),
        ),
    ]
