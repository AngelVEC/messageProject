from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Parent (models.Model):
    parentId = models.AutoField()
    parentFirstName = models.CharField(max_length=255)
    parentLastName = models.CharField(max_length=255)
    parentPhoneNumber = models.CharField(max_length=255)
    parentAddress = models.CharField(max_length=255)

    def __str__(self):
        return self.parentId

class Program (models.Model):
    programId = models.AutoField()
    programName = models.CharField(max_length=255, unique=True)
    programLevel = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.programId

class Course (models.Model):
    courseId = models.AutoField()
    courseName = models.CharField(max_length=255, unique=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return self.courseId

class Enrollment (models.Model):
    enrollmentId = models.AutoField()
    enrollmentFees = models.CharField(max_length=255)
    enrollmentMarks = models.CharField(max_length=3)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.enrollmentId

class Student (models.Model):
    studentFirstName = models.CharField(max_length=255)
    studentLastName = models.CharField(max_length=255)
    studentPhoneNumber = models.CharField(max_length=255)
    studentAddress = models.CharField(max_length=255)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)

    def __str__(self):
        return self.studentFirstName + " " + self.studentLastName

class Lecturer (models.Model):
    lecturerId = models.AutoField()
    lecturerFirstName = models.CharField(max_length=255)
    lecturerLastName = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.lecturerFirstName + " " + self.lecturerLastName