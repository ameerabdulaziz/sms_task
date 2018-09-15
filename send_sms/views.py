import csv
from django.shortcuts import render

from .forms import MessageForm


def home_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
    else:
        form = MessageForm()
    context = {
        'form': form
    }
    return render(request, 'send_sms/home.html', context)
