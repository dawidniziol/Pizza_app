from django.urls import path

from . import views
urlpatterns = [
    path('newing', views.ingredient_list, name='ingredient_list')
]