# from django.contrib import admin
# from django.urls import path, include

from django.urls import path
from .import views

urlpatterns = [
path('', views.home, name='home' ),
path('about/', views.about, name='about' ),
path('digimons/', views.digimon_index, name='digimon_index' ),
path('digimonss/<int:digimon_id>/', views.digimon_detail, name='digimon-detail'),

]