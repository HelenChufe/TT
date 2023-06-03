from django.urls import path
from .views import guessammo,guessed,failed
from django.conf.urls.static import static
from django.conf import settings
from .models import Ammo



urlpatterns = [
    path('',guessammo,name='guessammo'),
    path('guessed',guessed,name='guessed'),
    path('failed',failed,name='failed'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
