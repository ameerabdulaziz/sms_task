import csv
from django.shortcuts import render, redirect

from twilio.rest import Client

from .forms import MessageForm


def get_customers_cellphones(csv_file):
    data = csv_file.read().decode('utf-8').splitlines()
    reader = csv.reader(data)
    next(reader)
    customers_cellphones = []
    for row in reader:
        customers_cellphones.append(row[1])
    return customers_cellphones


def send_message_to_customers(phones, message_body):
    message_sids = []
    for phone in phones:
        account_sid = 'AC4b174ed56fd13054ac1ff1172df80083'
        auth_token = 'a10edaf2835481d9b825ff10a8ec3776'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='+18508057647',
            body=message_body,
            to=phone
        )
        message_sids.append(message.sid)
    return message_sids


def home_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            customers_cellphones = get_customers_cellphones(request.FILES['file'])
            message_body = form.cleaned_data.get('message')
            print(send_message_to_customers(customers_cellphones, message_body))
            return redirect('send_sms:home')
    else:
        form = MessageForm()
    return render(request, 'send_sms/home.html', {'form': form})
