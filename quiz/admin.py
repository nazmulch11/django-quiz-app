from django.contrib import admin
from .models import Subject, QuestionSet, Question, Option, AnswerSubmission, Result

# Register your models here.
admin.site.register(Subject)
admin.site.register(QuestionSet)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(AnswerSubmission)
admin.site.register(Result)