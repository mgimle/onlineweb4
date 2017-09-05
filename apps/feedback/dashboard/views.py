import logging
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from guardian.decorators import permission_required

from apps.feedback.models import Feedback

import apps.feedback.dashboard.forms as feedbackForms

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
    feedback_form = feedbackForms.FeedbackForm()
    text_question_form = feedbackForms.FeedbackQuestionHTMLForm()
    rating_question_form = feedbackForms.FeedbackRatingHTMLForm()
    multiple_choice_form = feedbackForms.FeedbackMultipleChoiceRelationHTMLForm()

    if request.method == 'POST':
        logger.warning(request.POST)
        feedback_form = feedbackForms.FeedbackForm(request.POST)
        if feedback_form.is_valid():
            feedback_instance = feedback_form.save(commit=False)
            feedback_instance.author = request.user
            feedback_instance.save()
        else:
            messages.error(request, 'Noen felt i beskrivelsen inneholder feil.')
            return

        save_multiple(request, feedback_instance, "text", logger)
        save_multiple(request, feedback_instance, "rating", logger)
        save_multiple(request, feedback_instance, "mc_relation", logger)

        messages.success(request, 'Spørreskjema ble opprettet.')
        return redirect(feedback_index, feedback_id=feedback_instance.pk)

    context = get_base_context(request)
    context['feedback_form'] = feedback_form
    context['text_question_form'] = text_question_form
    context['rating_question_form'] = rating_question_form
    context['multiple_choice_form'] = multiple_choice_form

    return render(request, 'feedback/dashboard/feedback_new.html', context)


@login_required
@permission_required('app.view_feedback', return_403=True)
def feedback_create_mc(request):
    multiple_choice_form = feedbackForms.FeedbackMultipleChoiceForm()
    choice_form = feedbackForms.FeedbackChoiceForm()

    if request.method == 'POST':
        multiple_choice_form = feedbackForms.FeedbackMultipleChoiceForm(request.POST)
        if multiple_choice_form.is_valid():
            multiple_choice_instance = multiple_choice_form.save(commit=False)
            multiple_choice_instance.save()
        else:
            messages.error('Noen felt i beskrivelsen inneholder feil.')

        choice_list = request.POST.getlist('choice')
        for choice in choice_list:
            choice_form = feedbackForms.FeedbackChoiceForm({'choice': choice})
            if choice_form.is_valid():
                choice_instance = choice_form.save(commit=False)
                choice_instance.question = multiple_choice_instance
                choice_instance.save()
            else:
                messages.error('Et eller flere alternativ inneholder feil')
                return

        messages.success(request, 'Flervalgsspørsmål ble opprettet')
        return redirect(feedback_index)

    context = get_base_context(request)
    context['mc_form'] = multiple_choice_form
    context['choice_form'] = choice_form

    return render(request, 'feedback/dashboard/feedback_new_mc.html', context)


@permission_required('feedback.view_feedback')
def feedback_edit(request, feedback_id):
    check_access_or_403(request)

    feedback_object = get_object_or_404(Feedback, pk=feedback_id)
    text_questions = feedback_object.questions
    #rating_questions = feedback_object.ratingquestions
    #mc_questions = feedback_object.multiple_choice_question

    context = get_base_context(request)
    context['text_questions'] = text_questions
    #context['rating_question'] = rating_questions
    #context['mc_questions'] = mc_questions
    context['feedback'] = feedback_object

    return render(request, 'feedback/dashboard/feedback_edit.html', context)


def save_multiple(request, feedback_instance, form_type, logger):
    # This function translates the HTML names of form fields to the db field name
    order_list = request.POST.getlist(form_type+'_order')
    if form_type == 'mc_relation':
        field_name = 'multiple_choice_relation'
        label_list = request.POST.getlist(form_type)
    else:
        field_name = 'label'
        label_list = request.POST.getlist(form_type+'_label')
    display_list = request.POST.getlist(form_type+'_display')

    logger.warning(request.POST)
    for i in range(len(label_list)):
        question_form_dict = {'order': order_list[i], field_name: label_list[i]}
        if str(i) in display_list:
            question_form_dict['display'] = 'true'
        if form_type == 'text':
            question_form = feedbackForms.FeedbackQuestionForm(question_form_dict)
        elif form_type == 'rating':
            question_form = feedbackForms.FeedbackRatingForm(question_form_dict)
        elif form_type == 'mc_relation':
            question_form = feedbackForms.FeedbackMultipleChoiceRelationForm(question_form_dict)
        else:
            logger.warning('invalid form type')
            return

        logger.warning(question_form_dict)
        if question_form.is_valid():
            logger.warning(form_type + " form valid")
            instance = question_form.save(commit=False)
            instance.feedback = feedback_instance
            instance.save()
        else:
            messages.error(request, 'Et eller flere score spm. felt inneholder feil.')
            return
