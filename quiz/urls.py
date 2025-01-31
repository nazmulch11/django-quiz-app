"""
URL configuration for quizproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),
    # path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    # path('quiz/<int:quiz_id>/submit/', views.submit_quiz, name='submit_quiz'),
    # path('results/<int:submission_id>/', views.quiz_results, name='quiz_results'),
    # path('progress/', views.user_progress, name='user_progress'),
]