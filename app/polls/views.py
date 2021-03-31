from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'polls/index.html', context)