# -*- coding: utf8 -*-
#
# Created by 'myth' on 6/27/15

from django.http import JsonResponse
from oauth2_provider.decorators import protected_resource
from oauth2_provider.models import AccessToken
from apps.authentication.models import OnlineUser as User


def get_user_details(user):
    return {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.get_email().email,
        'member': user.is_member,
        'staff': user.is_staff,
        'superuser': user.is_superuser,
        'nickname': user.nickname,
        'rfid': user.rfid,
        'image': user.get_image_url(),
        'field_of_study': user.get_field_of_study_display(),
    }


def get_user_details_from_session(request):
    """
    Basic user information provided based on session
    :param request: The Django Request object
    :return: An HTTP response
    """
    try:
        user_data = get_user_details(request.user)

        return JsonResponse(status=200, data=user_data)
    except AccessToken.DoesNotExist:
        return JsonResponse(status=403, data={'error': 'Unauthorized'})


@protected_resource([
    'authentication.onlineuser.username.read',
    'authentication.onlineuser.first_name.read',
    'authentication.onlineuser.last_name.read',
    'authentication.onlineuser.email.read',
    'authentication.onlineuser.is_member.read',
    'authentication.onlineuser.is_staff.read',
    'authentication.onlineuser.is_superuser.read',
    'authentication.onlineuser.field_of_study.read',
    'authentication.onlineuser.nickname.read',
    'authentication.onlineuser.rfid.read'
])
def get_user_details_bearer_token(request):
    """
    Basic user information provided based on the Bearer Token provided by an SSO application
    :param request: The Django Request object
    :return: An HTTP response
    """

    try:
        bearer = request.META.get('HTTP_AUTHORIZATION', '')
        bearer = bearer.split(' ')
        if len(bearer) != 2:
            return JsonResponse(status=403, data={'error': 'Unauthorized'})

        bearer = bearer[1]
        user_data = get_user_details(AccessToken.objects.get(token=bearer).user)

        return JsonResponse(status=200, data=user_data)
    except AccessToken.DoesNotExist:
        return JsonResponse(status=403, data={'error': 'Unauthorized'})
