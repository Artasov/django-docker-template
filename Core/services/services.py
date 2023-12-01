import functools
import hashlib
import hmac
import json
import os
import time
import traceback
import urllib
from typing import Optional, Tuple, List

from django.conf import settings
from django.contrib.auth import logout
from django.db import transaction
from django.shortcuts import render, redirect

from APP_mailing.services.services import send_text_email
from Core.error_messages import USER_EMAIL_NOT_EXISTS, USER_USERNAME_NOT_EXISTS
from Core.models import User
import urllib.parse, urllib.request
from django.http import HttpResponseNotAllowed


def allowed_only(allowed_methods):
    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            if request.method in allowed_methods:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponseNotAllowed(allowed_methods)

        return wrapped_view

    return decorator


def base_view(fn):
    """transaction.atomic() и хук исключений самого высокого уровня"""

    @functools.wraps(fn)
    def inner(request, *args, **kwargs):
        if settings.DEBUG:
            with transaction.atomic():
                return fn(request, *args, **kwargs)
        else:
            try:
                with transaction.atomic():
                    return fn(request, *args, **kwargs)
            except Exception as e:
                send_text_email(
                    subject='Ошибка на сервере',
                    to_email=settings.DEVELOPER_EMAIL,
                    text=f"error_message: {str(e)}\n"
                         f"traceback:\n{traceback.format_exc()}"
                )
                return render_invalid(request, str(e))

    return inner


def forbidden_with_login(fn, redirect_field_name: str = None):
    """logout if user.is_authenticated, with redirect if necessary"""

    @functools.wraps(fn)
    def inner(request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            if redirect_field_name is not None:
                return redirect(redirect_field_name)
            return fn(request, *args, **kwargs)
        else:
            return fn(request, *args, **kwargs)

    return inner
