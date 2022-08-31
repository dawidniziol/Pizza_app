from django.urls import path
from . import views

app_name = 'pdrs'

urlpatterns = [
    path('newing', views.ingredient_list, name='ingredient_list'),
    path('home', views.home_page, name='home_page')

]