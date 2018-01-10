# -*- coding: utf-8 -*-

from django.conf.urls import url

from apps.sso import endpoints, views

urlpatterns = [
    url(r'^$', views.index, name='sso_index'),
    url(r'^session_user/', endpoints.get_user_details_from_session, name='sso_session_user'),
    url(r'^oath2_user/', endpoints.get_user_details_bearer_token, name='sso_oath2_user'),
    url(r'^o/authorize/$', views.AuthorizationView.as_view(), name='oauth2_provider_authorize'),
    url(r'^o/token/$', views.TokenView.as_view(), name='oauth2_provider_token'),
    url(r'^o/revoke/$', views.RevokeTokenView.as_view(), name='oauth2_provider_revoke_token'),
]
