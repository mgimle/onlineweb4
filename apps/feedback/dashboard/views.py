from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render

from django.shortcuts import render
from guardian.decorators import permission_required

from apps.feedback.models import Feedback
from apps.feedback.dashboard.forms import FeedbackForm, FeedbackQuestionForm

from apps.dashboard.tools import check_access_or_403, get_base_context

@login_required
@permission_required('app.view_feedback', return_403=True)
def feedback_index(request):

    context = get_base_context(request)

    context['results'] = Feedback.objects.all()

    return render(request, 'feedback/dashboard/feedback_index.html', context)

@login_required
@permission_required('app.view_feedback', return_403=True)
def feedback_create (request):
    feedbackForm = FeedbackForm()
    questionForm = FeedbackQuestionForm()

    if request.method == 'POST':
        feedbackForm = FeedbackForm(request.POST)
        questionForm = FeedbackQuestionForm(request.POST)
        if feedbackForm.is_valid() and questionForm.is_valid():
            feedbackInstance = feedbackForm.save(commit=False)
            questionInstance = questionForm.save(commit=False)
            feedbackInstance.author = request.user
            feedbackInstance.save()
            questionInstance.feedback = feedbackInstance
            questionInstance.save()

            messages.success(request, 'Spørreskjema ble opprettet.')
            return redirect(feedback_detail, feedback_id=feedbackInstance.pk)
        else:
            messages.error(request, 'Noen av de påkrevde feltene inneholder feil.')

    context = get_base_context(request)
    context['feedbackForm'] = feedbackForm
    context['questionForm'] = questionForm

    return render(request, 'feedback/dashboard/feedback_new.html', context)

@permission_required('feedback.view_feedback')
def feedback_detail(request, feedback_id):
    check_access_or_403(request)

    feedback = get_object_or_404(Feedback, pk=feedback_id)

    context = get_base_context(request)
    context['feedback'] = feedback

    return render(request, 'feedback/dashboard/feedback_detail.html', context)
