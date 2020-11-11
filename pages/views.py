from django.shortcuts import render


def home(request):
    return render(request, 'pages/index.html')


def features(request):
    return render(request, 'pages/features.html')
