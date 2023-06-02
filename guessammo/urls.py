from django.urls import path
from .views import guessammo
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',guessammo,name='guessammo')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
