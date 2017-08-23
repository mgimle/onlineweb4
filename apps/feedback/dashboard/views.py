import logging
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from guardian.decorators import permission_required

from apps.feedback.models import Feedback
from apps.feedback.dashboard.forms import FeedbackForm, FeedbackQuestionForm, FeedbackQuestionHTMLForm, \
    FeedbackRatingForm, FeedbackRatingHTMLForm

from apps.dashboard.tools import check_access_or_403, get_base_context


@login_required
@permission_required('app.view_feedback', return_403=True)
def feedback_index(request):

    context = get_base_context(request)

    context['results'] = Feedback.objects.all()

    return render(request, 'feedback/dashboard/feedback_index.html', context)


@login_required
@permission_required('app.view_feedback', return_403=True)
def feedback_create(request):
    logger = logging.getLogger(__name__)
    feedback_form = FeedbackForm()
    text_question_form = FeedbackQuestionHTMLForm()
    rating_question_form = FeedbackRatingHTMLForm()

    if request.method == 'POST':
        logger.warning(request.POST)
        feedback_form = FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_instance = feedback_form.save(commit=False)
            feedback_instance.author = request.user
            feedback_instance.save()
        else:
            messages.error(request, 'Noen felt i beskrivelsen inneholder feil')
            return

        save_multiple(request, feedback_instance, "text", logger)
        save_multiple(request, feedback_instance, "rating", logger)

        messages.success(request, 'Spørreskjema ble opprettet.')
        return redirect(feedback_detail, feedback_id=feedback_instance.pk)

    context = get_base_context(request)
    context['feedback_form'] = feedback_form
    context['text_question_form'] = text_question_form
    context['rating_question_form'] = rating_question_form

    return render(request, 'feedback/dashboard/feedback_new.html', context)


@login_required
@permission_required('app.view_feedback', return_403=True)
def feedback_create_mc(request):
    logger = logging.getLogger(__name__)
    logger.warning("yay")

    context = get_base_context(request)

    return render(request, 'feedback/dashboard/feedback_new_mc.html', context)


@permission_required('feedback.view_feedback')
def feedback_detail(request, feedback_id):
    check_access_or_403(request)

    feedback = get_object_or_404(Feedback, pk=feedback_id)

    context = get_base_context(request)
    context['feedback'] = feedback

    return render(request, 'feedback/dashboard/feedback_detail.html', context)


def save_multiple(request, feedback_instance, form_type, logger):
    # This function translates the HTML names of form fields to the db field name
    order_list = request.POST.getlist(form_type+'_order')
    label_list = request.POST.getlist(form_type+'_label')
    display_list = request.POST.getlist(form_type+'_display')

    logger.warning(request.POST)
    for i in range(len(label_list)):
        question_form_dict = {'order': order_list[i], 'label': label_list[i]}
        if str(i) in display_list:
            question_form_dict['display'] = 'true'
        if form_type == 'text':
            question_form = FeedbackQuestionForm(question_form_dict)
        elif form_type == 'rating':
            question_form = FeedbackRatingForm(question_form_dict)
        else:
            logger.warning('invalid form type')
            return

        logger.warning(question_form_dict)
        if question_form.is_valid():
            logger.warning("rating form valid")
            instance = question_form.save(commit=False)
            instance.feedback = feedback_instance
            instance.save()
        else:
            messages.error(request, 'Et eller flere score spm. felt inneholder feil.')
