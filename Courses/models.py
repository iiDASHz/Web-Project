from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    secret_password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=50)
    email_address = models.EmailField(unique=True)

class Course(models.Model):
    code = models.CharField(primary_key=True, max_length=20)
    course_name = models.CharField(max_length=200)
    capacity = models.PositiveIntegerField()
    schedule = models.ForeignKey('CourseSchedule', on_delete=models.CASCADE)
    course_description = models.TextField()
    prerequisites = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    instructor_name = models.CharField(max_length=100)

class StudentRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class CourseSchedule(models.Model):
    id = models.AutoField(primary_key=True)
    end_time = models.TimeField()
    class_days = models.CharField(max_length=32)
    start_time = models.TimeField()
    room_number = models.CharField(max_length=20)
