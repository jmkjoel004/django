from django.shortcuts import render
from django.http import HttpResponse

def bgevent(request):
    return render(request, 'front.html', {'event_message': "Join us for the Big Event!"})

