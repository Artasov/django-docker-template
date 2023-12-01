from django.shortcuts import render, redirect, get_object_or_404
from Core.models import User

from Core.services.services import base_view
from Core.tasks import test_task


@base_view
def example(request):
    try:
        user = get_object_or_404(User, id=1)
    except User.DoesNotExist:
        user = None
    result = test_task.delay(1, 2)
    return render(request, 'Core/example.html', {'user': user})
