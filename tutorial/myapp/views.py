from django.shortcuts import render
from .models import Service


def index(request):
    return render(request, 'index.html')


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})


def static(request):
    return render(request, 'static.html')


def arsha(request):
    service1 = Service()
    service1.id = 0
    service1.name = 'Sale'
    service1.details = 'We are one of the main sellers in the sector, with unbeatable statistics.'

    service2 = Service()
    service2.id = 1
    service2.name = 'Notifications'
    service2.details = 'If there is any change in the system, you will be notified instantly in your email account.'

    service3 = Service()
    service3.id = 2
    service3.name = '24hs Support'
    service3.details = 'We have a support service available 24 hours a day, 7 days a week, 365 days at year.'

    services = [service1, service2, service3]

    return render(request, 'arsha.html', {'services': services})
