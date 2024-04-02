from django.urls import path
from . import views           

urlpatterns = [
    path('home/', views.home, name='home'), ##Para apresentação
    path('cadastro/', views.cadastro, name="cadastro"), 
    path('logar/', views.logar, name="logar"),
    path('logout/', views.logout, name="logout"),   
]
