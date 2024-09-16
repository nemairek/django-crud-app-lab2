
from django.urls import path
from .import views

urlpatterns = [
path('', views.Home.as_view(), name='home'),
path('about/', views.about, name='about' ),
path('digimons/', views.digimon_index, name='digimon_index' ),
path('digimons/<int:digimon_id>/', views.digimon_detail, name='digimon_detail'),
path('digimons/create/', views.DigimonCreate.as_view(), name='digimon_create'),
path('digimons/<int:pk>/update/', views.DigimonUpdate.as_view(), name='digimon_update'),
path('digimons/<int:pk>/delete/', views.DigimonDelete.as_view(), name='digimon_delete'),

path('moves/create/', views.MoveCreate.as_view(), name='move_create'),
path('moves/<int:pk>/', views.MoveDetail.as_view(), name='move_detail'),
path('moves/', views.MoveList.as_view(), name='move_index'),
path('moves/<int:pk>/update/', views.MoveUpdate.as_view(), name='move_update'),
path('moves/<int:pk>/delete/', views.MoveDelete.as_view(), name='move_delete'),
path('digimons/<int:digimon_id>/associate_move/<int:move_id>/', views.associate_move, name='associate_move'),
path('digimons/<int:digimon_id>/remove_move/<int:move_id>/', views.remove_move, name='remove_move'),
path('accounts/signup/', views.signup, name='signup'),
]