from django.urls import path
from .views import *

urlpatterns = [
 path('', login_view, name='login'),
  path('principal', principal, name='principal'),
  path('cerrar_secion', cerrar_secion, name='cerrar_secion'),
  path('register_user', register_user, name='register_user'),
  path('user_', user_, name='user_'),
  path('colaboradores', colaboradores, name='colaboradores'),
  path('develops', develops, name='develops'),
  path('calculos', calculos, name='calculos'),
]

