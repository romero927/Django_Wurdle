from django.urls import path
from . import views

urlpatterns = [
    path('', views.game, name='game'),
    path('make_guess/', views.make_guess, name='make_guess'),
    path('new_game/', views.new_game, name='new_game'),
]