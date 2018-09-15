import csv
from django.shortcuts import render

from .forms import MessageForm


def get_customers_cellphones(csv_file):
    data = csv_file.read().decode('utf-8').splitlines()
    reader = csv.reader(data)
    next(reader)
    customers_cellphones = []
    for row in reader:
        customers_cellphones.append(row[1])
    return customers_cellphones


def home_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            print(get_customers_cellphones(request.FILES['file']))
    else:
        form = MessageForm()
    return render(request, 'send_sms/home.html', {'form': form})
