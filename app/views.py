from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
import logging

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Неверные данные. Введите снова')
    else:
        return render(request, 'login.html')
    
def index(request):
    return render(request, 'index.html')

def my_view(request):
    # Логирование данных с запроса
    logger = logging.getLogger(__name)
    logger.debug("Запрос от пользователя: %s", request.user)
    logger.debug("GET-параметры: %s", request.GET)
    logger.debug("POST-параметры: %s", request.POST)

    # Ваш код для представления

    return HttpResponse("Данные залогированы")