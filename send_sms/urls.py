from django.urls import path, include

from .views import home_view

app_name = 'send_sms'

urlpatterns = [
    path('', home_view, name='home'),
]
