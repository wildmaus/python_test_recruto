from django.urls import path
from .views import *

urlpatterns = [
    path('rand/', get_rand, name="rand"),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
]
