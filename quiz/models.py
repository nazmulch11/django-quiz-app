from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class QuestionSet(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    quiz_name = models.CharField(max_length=100)
    time = models.DateTimeField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.quiz_name

class Question(models.Model):
    quizset = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)
    question = models.TextField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    time_to_start = models.DateTimeField()
    duration = models.DateTimeField()
    points = models.IntegerField()
    negative_points = models.IntegerField()

    def __str__(self):
        return self.question

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.TextField()
    is_correct = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.option

class AnswerSubmission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submitted_time = models.DateTimeField()

    def __str__(self):
        return f"{self.question} - {self.option}"

class Result(models.Model):
    quizset = models.ForeignKey(QuestionSet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    submitted_time = models.DateTimeField()

    def __str__(self):
        return f"{self.quizset} - {self.user.username} - {self.score}"