from django.urls import path
from . import views  # Views ko import karein

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL
]
