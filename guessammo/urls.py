from django.urls import path
from .views import guessammo,guessed
from django.conf.urls.static import static
from django.conf import settings
from .models import Ammo



urlpatterns = [
    path('',guessammo,name='guessammo'),
    path('guessed/<str:roun>/<int:result>/',guessed,name='guessed')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
