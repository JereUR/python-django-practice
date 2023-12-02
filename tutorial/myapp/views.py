from django.shortcuts import render


def index(request):
    context = {
        'data': 'Data Send',
        'text': 'Data Recieved'
    }

    return render(request, 'index.html', context)
