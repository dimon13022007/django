from django.shortcuts import render
from .models import UserAction

def index(request):
    #Алгоритм аналізу користувача
    UserAction.objects.create(user=request.user, action='Посещение главной страницы')

    return render(request, 'main/rrk.html')

def about(request):
    return render(request, 'main/cost.html')

def contact(request):
    return render(request, 'main/kids.html')

def payments(request):
    UserAction.objects.create(user=request.user, action='Посещение страницы оплаты')

    return render(request, 'main/payment1.html')

def payments2(request):
    UserAction.objects.create(user=request.user, action='Посещение второй страницы оплаты')

    return render(request, 'main/payment2.html')

def contacts(request):
    return render(request, 'main/rm.html')