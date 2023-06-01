from django.urls import path
from .views import guessammo

urlpatterns = [
    path('',guessammo,name='guessammo')
]
