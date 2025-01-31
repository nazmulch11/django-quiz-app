from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('', views.QuizListView.as_view(), name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.QuizDetailView.as_view(), name='quiz_detail'),
    path('quiz/<int:quiz_id>/submit/', views.SubmitQuizView.as_view(), name='submit_quiz'),
    path('results/<int:submission_id>/', views.QuizResultsView.as_view(), name='quiz_results'),
]