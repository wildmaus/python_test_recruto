from django.urls import path
from .views import *

urlpatterns = [
    path('rand/', rand_view, name="rand"),
    path('register/', register_view, name="register"),
]
