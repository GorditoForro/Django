from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
import locale

# Create your views here.

# Pages

def singup(request):
    return render(request, 'singup.html')

def singin(request):
    return render(request, 'singin.html')

def home(request):
    return render(request, 'home.html')

def task1(request):
    return render(request, 'task1.html')

def task2(request):
    return render(request, 'task2.html')

def task3(request):
    return render(request, 'task3.html')

def task4(request):
    return render(request, 'task4.html')

def task5(request):
    return render(request, 'task5.html')
# Singup


def singup(request):
    if request.method == 'GET':
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST
                    ['password1'])
                user.save()
                login(request, user)
                return redirect('task1')
            except IntegrityError:
                return render(request, 'singup.html', {
                    'form': UserCreationForm,
                    "error": 'Username already exists'
                })
        return render(request, 'singup.html', {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })

# Singout


def singout(request):
    logout(request)
    return redirect('singin')


# Singin

def singin(request):
    if request.method == 'GET':
        return render(request, 'singin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST
                            ['password'])
        if user is None:
            return render(request, 'singin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('task1')

#Factor comun

def task2(request):
    factor_comun = None
    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        number3 = int(request.POST.get('number3'))
        factor_comun = calcular_factor_comun_logica(number1, number2, number3)
    return render(request, 'task2.html', {'factor_comun': factor_comun})

def calcular_factor_comun_logica(a, b, c):
    menor = min(a, b, c)
    factor_comun = 1
    for i in range(1, menor + 1):
        if a % i == 0 and b % i == 0 and c % i == 0:
            factor_comun = i
    return factor_comun

#Diferencia de cuadrados

def task3(request):
    diferencia_de_cuadrados = None
    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        diferencia_de_cuadrados = calcular_diferencia_cuadrados_logica(number1, number2)
    return render(request, 'task3.html', {'diferencia_de_cuadrados': diferencia_de_cuadrados})

def calcular_diferencia_cuadrados_logica(a, b):
    diferencia_cuadrados = a**2 - b**2
    raiz_a = a**0.5
    raiz_b = b**0.5
    factorizacion = f"({raiz_a}+{raiz_b})({raiz_a}-{raiz_b})"
    return f"La diferencia de cuadrados es {diferencia_cuadrados}, que se factoriza como {factorizacion}."

#Trinomio cuadrado perfecto

def task4(request):
    trinomio_cuadrado_perfecto = None
    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        trinomio_cuadrado_perfecto = calcular_trinomio_cuadrado_perfecto_logica(number1, number2)
    return render(request, 'task4.html', {'trinomio_cuadrado_perfecto': trinomio_cuadrado_perfecto})

def calcular_trinomio_cuadrado_perfecto_logica(a, b):
    trinomio_cuadrado = a*2 + 2 * a * b + b*2
    binomio_cuadrado = (a + b)**2
    return f"El trinomio cuadrado perfecto es {trinomio_cuadrado}, que se factoriza como {binomio_cuadrado}."

#Diferencia de cubos 

def task5(request):
    diferencia_de_cubos = None
    if request.method == 'POST':
        number1 = int(request.POST.get('number1'))
        number2 = int(request.POST.get('number2'))
        diferencia_de_cubos = calcular_diferencia_cubos_logica(number1, number2)
    return render(request, 'task5.html', {'diferencia_de_cubos': diferencia_de_cubos})

def calcular_diferencia_cubos_logica(a, b):
    diferencia_de_cubos = a**3 - b**3
    factor_comun = a - b
    suma_cubos = a**2 + a*b + b**2
    return f"La diferencia de cubos es {diferencia_de_cubos}, que se factoriza como ({factor_comun})({suma_cubos})."