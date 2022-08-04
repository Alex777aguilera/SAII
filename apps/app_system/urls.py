from django.urls import path
from .views import *

urlpatterns = [
 path('', login_view, name='login'),
  path('principal', principal, name='principal'),
]
