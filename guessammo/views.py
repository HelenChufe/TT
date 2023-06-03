from django.shortcuts import render,redirect
from .models import Ammo
from random import randint,shuffle
# Create your views here.

def guessammo(request):
    ammos = Ammo.objects.all()
    numero_ammos=0
    for i in ammos:
        numero_ammos += 1
        
    guess = Ammo.objects.get(id = randint(0,numero_ammos))
    respuestas = [guess]
    for i in range(0,3):
        respuestas.append(Ammo.objects.get(id = randint(0,numero_ammos)))
    
    shuffle(respuestas)
    
    usadas = []
    context={'guess':guess,'ammos':ammos,'respuestas':respuestas,'usadas':usadas}

    return render(request,'index.html',context)

def guessed(request):
    
    return redirect('guessammo')

def failed(request):
    
    return redirect('guessammo')
