# -*- encoding: utf-8 -*-
from django import forms

from apps.feedback.models import Feedback, TextQuestion, RatingQuestion, MultipleChoiceQuestion, Choice, \
    MultipleChoiceRelation


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
        fields = (
            'order',
            'label',
            'display',
        )


class FeedbackQuestionHTMLForm(forms.Form):
    text_order = forms.IntegerField(label='Rekkefølge', initial=10)
    text_label = forms.CharField(label='Spørsmål', max_length=256)
    text_display = forms.BooleanField(label='Vis til bedrift', initial=True)


class FeedbackRatingForm(forms.ModelForm):
    class Meta(object):
        model = RatingQuestion
        fields = (
            'order',
            'label',
            'display',
        )


class FeedbackRatingHTMLForm(forms.Form):
    rating_order = forms.IntegerField(label='Rekkefølge', initial=20)
    rating_label = forms.CharField(label='Spørsmål', max_length=256)
    rating_display = forms.BooleanField(label='Vis til bedrift', initial=True)


class FeedbackMultipleChoiceRelationForm(forms.ModelForm):
    class Meta(object):
        model = MultipleChoiceRelation
        fields = (
            'multiple_choice_relation',
            'order',
            'display',
        )


class FeedbackMultipleChoiceRelationHTMLForm(forms.Form):
    mc_relation = forms.ModelChoiceField(queryset=MultipleChoiceQuestion.objects.all())
    mc_relation_order = forms.IntegerField(label='Rekkefølge', initial=30)
    mc_relation_display = forms.BooleanField(label='Vis til bedrift', initial=True)


class FeedbackMultipleChoiceForm(forms.ModelForm):
    class Meta(object):
        model = MultipleChoiceQuestion
        fields = (
            'label',
        )


class FeedbackChoiceForm(forms.ModelForm):
    class Meta(object):
        model = Choice
        fields = (
            'choice',
        )
