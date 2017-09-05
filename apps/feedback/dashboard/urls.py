# -*- coding: utf-8 -*-

from django.conf.urls import url

from apps.feedback.dashboard import views

urlpatterns = [
    url(r'^$', views.feedback_index, name='dashboard_feedback_index'),
    url(r'^new/$', views.feedback_create, name='dashboard_feedback_create'),
    url(r'^new_mc/$', views.feedback_create_mc, name="dashboard_feedback_create_mc"),
    url(r'^edit/(?P<feedback_id>\d+)/$', views.feedback_edit, name='dashboard_feedback_edit'),
]
