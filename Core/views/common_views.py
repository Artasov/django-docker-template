from django.shortcuts import render, redirect

from Core.services.services import base_view


@base_view
def example(request):
    return render(request, 'Core/example.html')
