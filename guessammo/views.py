from django.shortcuts import render,redirect
from .models import Ammo,Calibre
from random import shuffle
from django.db.models import Count


def guessammo(request):
    redirect('main')
    redirect('guessammo')
    random_ammo = Ammo.objects.order_by('?').first()
    random_ammos = Ammo.objects.exclude(id=random_ammo.id).order_by('?')[:3]
    
    respuestas = list(random_ammos) + [random_ammo]
    
    shuffle(respuestas)
    
    context = {'guess': random_ammo,
                'respuestas': respuestas,}
    return render(request, 'guessammo/index.html', context)

def guessAmmoAutoComplete(request):
        ammos = Ammo.objects.all()
        random_ammo = Ammo.objects.order_by('?').first()
        
        context= {'ammos':ammos, 'guess':random_ammo,}
        return render(request,'guessammo/autocomplete.html',context)
