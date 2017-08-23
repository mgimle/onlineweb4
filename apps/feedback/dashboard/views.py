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
def feedback_create (request):
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

        # Change request (django QueryDict) to python lists
        text_order_list = request.POST.getlist('text_order')
        text_label_list = request.POST.getlist('text_label')
        text_display_list = request.POST.getlist('text_display')

        # Iterate through all the text questions added
        for i in range(len(text_label_list)):
            text_question_form_dict = {'order': text_order_list[i], 'label': text_label_list[i]}

            # Check if question had 'display' checkbox checked
            if str(i) in text_display_list:
                text_question_form_dict['display'] = 'true'
            text_question_form = FeedbackQuestionForm(text_question_form_dict)

            if text_question_form.is_valid():
                question_instance = text_question_form.save(commit=False)
                question_instance.feedback = feedback_instance
                question_instance.save()
            else:
                messages.error(request, 'Et eller flere tekst spm. felt inneholder feil.')

        rating_order_list = request.POST.getlist('rating_order')
        rating_label_list = request.POST.getlist('rating_label')
        rating_display_list = request.POST.getlist('rating_display')

        logger.warning(request.POST)
        for i in range(len(rating_label_list)):
            rating_question_form_dict = {'order': rating_order_list[i], 'label': rating_label_list[i]}
            if str(i) in rating_display_list:
                rating_question_form_dict['display'] = 'true'
            rating_question_form = FeedbackRatingForm(rating_question_form_dict)

            logger.warning(rating_question_form_dict)
            if rating_question_form.is_valid():
                logger.warning("rating form valid")
                rating_instance = rating_question_form.save(commit=False)
                rating_instance.feedback = feedback_instance
                rating_instance.save()
            else:
                messages.error(request, 'Et eller flere score spm. felt inneholder feil.')

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
