# Generated by Django 5.0.4 on 2024-04-27 20:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseSchedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('end_time', models.TimeField()),
                ('class_days', models.CharField(max_length=32)),
                ('start_time', models.TimeField()),
                ('room_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('secret_password', models.CharField(max_length=128)),
                ('full_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('code', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=200)),
                ('capacity', models.PositiveIntegerField()),
                ('course_description', models.TextField()),
                ('instructor_name', models.CharField(max_length=100)),
                ('prerequisites', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Courses.course')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.courseschedule')),
            ],
        ),
        migrations.CreateModel(
            name='StudentRegistration',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.student')),
            ],
        ),
    ]
