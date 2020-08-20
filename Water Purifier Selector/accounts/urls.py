from django.urls import path
from . import views
# URLS mei import krna hai hume path m and ek views

urlpatterns = [path("register",views.register,name="register")]
