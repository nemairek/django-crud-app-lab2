
from django.urls import path
from .import views

urlpatterns = [
path('', views.home, name='home' ),
path('about/', views.about, name='about' ),
path('digimons/', views.digimon_index, name='digimon_index' ),
path('digimons/<int:digimon_id>/', views.digimon_detail, name='digimon_detail'),
path('digimons/create/', views.DigimonCreate.as_view(), name='digimon_create'),
path('digimons/<int:pk>/update/', views.DigimonUpdate.as_view(), name='digimon_update'),
path('digimons/<int:pk>/delete/', views.DigimonDelete.as_view(), name='digimon_delete'),
path('moves/create/', views.MoveCreate.as_view(), name='move-create'),
]