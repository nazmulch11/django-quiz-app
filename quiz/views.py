from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import QuestionSet
from django.db.models import Count, Avg

# Create your views here.

# def index(request):
#     return render(request, 'quiz_show.html')

def quiz_list(request):
    """Display a list of all available quizzes"""
    quizzes = QuestionSet.objects.annotate()
    print(quizzes)
    return render(request, 'quiz_list.html', {'quizzes': quizzes})
