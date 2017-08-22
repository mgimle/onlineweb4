# -*- encoding: utf-8 -*-
from django import forms

from apps.feedback.models import Feedback, TextQuestion, RatingQuestion, MultipleChoiceQuestion

TEXT_QUESTION_NAME_MAP = {
    'order': 'text_order',
    'label': 'text_label',
    'display': 'text_display',
}

RATING_QUESTION_NAME_MAP = {
    'order': 'rating_order',
    'label': 'rating_label',
    'display': 'rating_display'
}


class FeedbackForm(forms.ModelForm):
    class Meta(object):
        model = Feedback
        fields = [
            'description',
            'display_field_of_study',
            'display_info',
        ]


class FeedbackQuestionForm(forms.ModelForm):
    def add_prefix(self, field_name):
            # Looks up html name for field in *_NAME_MAP
            # The HTML name is needed to differentiate between
            # rating and text field names
            field_name = TEXT_QUESTION_NAME_MAP.get(field_name, field_name)
            return super(FeedbackQuestionForm, self).add_prefix(field_name)

    class Meta(object):
        model = TextQuestion
        fields = (
            'order',
            'label',
            'display',
        )


class FeedbackRatingForm(forms.ModelForm):
    def add_prefix(self, field_name):
        field_name = RATING_QUESTION_NAME_MAP.get(field_name, field_name)
        return super(FeedbackRatingForm, self).add_prefix(field_name)

    class Meta(object):
        model = RatingQuestion
        fields = (
            'order',
            'label',
            'display',
        )
