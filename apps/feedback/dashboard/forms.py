# -*- encoding: utf-8 -*-
from django import forms

from apps.feedback.models import Feedback, MultipleChoiceQuestion, TextQuestion

class FeedbackForm(forms.ModelForm):
    class Meta(object):
        model = Feedback
        fields = [
            'description',
            'display_field_of_study',
            'display_info',
        ]

class FeedbackQuestionForm(forms.ModelForm):
    class Meta(object):
        model = TextQuestion
        fields = [
            'order',
            'label',
            'display',
        ]
