import functools
import logging
import traceback

from django.conf import settings
from django.contrib.auth import logout
from django.db import transaction
from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed

log = logging.getLogger('Core')


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
                log.critical("ERROR", exc_info=True)

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
