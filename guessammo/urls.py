from django.urls import path
from .views import guessammo,guessAmmoAutoComplete
from django.conf.urls.static import static
from django.conf import settings
from .models import Ammo



urlpatterns = [
    
    path('',guessammo,name='guessammo'),
    path('ac',guessAmmoAutoComplete,name='gac')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
