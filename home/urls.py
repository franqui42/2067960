from django.urls import path
from.views import *

urlpatterns = [
    path('about/',vista_about, name='about_view'),
    path('contacto/',vista_contacto, name='cotacto_view'),
    path('servicios/',vista_servicios, name='servicios_view'),
]