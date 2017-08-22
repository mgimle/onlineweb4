import logging
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from guardian.decorators import permission_required

from apps.feedback.models import Feedback
from apps.feedback.dashboard.forms import FeedbackForm, FeedbackQuestionForm, FeedbackRatingForm
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
    logger = logging.getLogger(__name__)
    feedback_form = FeedbackForm()
    text_question_form = FeedbackQuestionForm()
    rating_question_form = FeedbackRatingForm()

    if request.method == 'POST':
        logger.warning(request.POST)
        logger.warning()
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_instance = feedback_form.save(commit=False)
            feedback_instance.author = request.user
            feedback_instance.save()
        else:
            messages.error(request, 'Noen felt inneholder feil')

        # Change request (django QueryDict) to python lists
        order_list = request.POST.getlist('order')
        label_list = request.POST.getlist('label')
        display_list = request.POST.getlist('display')

        # Iterate through all the questions added
        for i in range(len(label_list)):
            text_question_formDict = {'order': order_list[i], 'label': label_list[i]}
            logger.warning(i)

            # Check if question had 'display' checkbox checked
            if str(i) in display_list:
                text_question_formDict['display'] = 'true'
            text_question_form = FeedbackQuestionForm(text_question_formDict)

            if text_question_form.is_valid():
                question_instance = text_question_form.save(commit=False)
                question_instance.feedback = feedback_instance
                question_instance.save()
            else:
                messages.error(request, 'Noen av de påkrevde feltene inneholder feil.')

        messages.success(request, 'Spørreskjema ble opprettet.')
        return redirect(feedback_detail, feedback_id=feedback_instance.pk)

    context = get_base_context(request)
    context['feedback_form'] = feedback_form
    context['text_question_form'] = text_question_form
    context['rating_question_form'] = rating_question_form

    return render(request, 'feedback/dashboard/feedback_new.html', context)

@permission_required('feedback.view_feedback')
def feedback_detail(request, feedback_id):
    check_access_or_403(request)

    feedback = get_object_or_404(Feedback, pk=feedback_id)

    context = get_base_context(request)
    context['feedback'] = feedback

    return render(request, 'feedback/dashboard/feedback_detail.html', context)
