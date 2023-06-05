from django.shortcuts import render,redirect
from .models import Ammo,Calibre
from random import randint,shuffle
# Create your views here.

def guessammo(request):
    ammos = Ammo.objects.all()
    
    numero_ammos= len(ammos)
    
    random = randint(0,numero_ammos-1)
    
    guess = ammos[random]
    url = guess.imagen.url[1:]
    
    respuestas = [guess]
    for i in range(0,3):
        while True:
            random = randint(0,numero_ammos)
            respuesta = ammos[random]
            if respuesta != guess:
                respuestas.append(respuesta)
                break
        
        
    
    shuffle(respuestas)
    
    context={'guess':guess,'url':url,'ammos':ammos,'respuestas':respuestas}

    return render(request,'guessammo/index.html',context)

def guessed(request):
    
    return redirect('guessammo')

def failed(request):
    
    return redirect('guessammo')
