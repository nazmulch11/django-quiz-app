from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import ListView, DetailView, FormView, View
from django.urls import reverse_lazy
from .models import QuestionSet, Question, Option, AnswerSubmission, Result
from django.db.models import Count, Avg

class RegisterView(FormView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('quiz_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

class QuizListView(LoginRequiredMixin, ListView):
    model = QuestionSet
    template_name = 'quiz_list.html'
    context_object_name = 'quizzes'

class QuizDetailView(LoginRequiredMixin, DetailView):
    model = QuestionSet
    template_name = 'quiz_show.html'
    context_object_name = 'quiz'
    pk_url_kwarg = 'quiz_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions'] = Question.objects.filter(quizset=self.object)
        return context

    def dispatch(self, request, *args, **kwargs):
        quiz = self.get_object()
        existing_result = Result.objects.filter(quizset=quiz, user=request.user).first()
        if existing_result:
            messages.warning(request, 'You have already attempted this quiz.')
            return redirect('quiz_results', submission_id=existing_result.id)
        return super().dispatch(request, *args, **kwargs)

class SubmitQuizView(LoginRequiredMixin, View):
    def post(self, request, quiz_id):
        quiz = get_object_or_404(QuestionSet, pk=quiz_id)
        questions = Question.objects.filter(quizset=quiz)
        total_score = 0

        for question in questions:
            selected_option_id = request.POST.get(f'question_{question.id}')
            if selected_option_id:
                selected_option = get_object_or_404(Option, pk=selected_option_id)

                submission = AnswerSubmission.objects.create(
                    question=question,
                    option=selected_option,
                    user=request.user,
                    submitted_time=timezone.now()
                )

                if selected_option.is_correct:
                    total_score += question.points
                else:
                    total_score -= question.negative_points

        result = Result.objects.create(
            quizset=quiz,
            user=request.user,
            score=total_score,
            submitted_time=timezone.now()
        )

        return redirect('quiz_results', submission_id=result.id)

    def get(self, request, quiz_id):
        return redirect('quiz_detail', quiz_id=quiz_id)

class QuizResultsView(LoginRequiredMixin, DetailView):
    model = Result
    template_name = 'quiz_results.html'
    context_object_name = 'result'
    pk_url_kwarg = 'submission_id'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submissions'] = AnswerSubmission.objects.filter(
            user=self.request.user,
            question__quizset=self.object.quizset
        ).select_related('question', 'option')
        return context
