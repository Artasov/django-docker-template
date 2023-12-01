from django.shortcuts import render, redirect
from Core.models import User
from Core.services.services import base_view


@base_view
def example(request):
    user = User.objects.first()
    return render(request, 'Core/example.html', {'user': user})

