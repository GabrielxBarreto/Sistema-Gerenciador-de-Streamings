from django.contrib import admin
from django.urls import path , include
from dashboard import views
urlpatterns = [
    
    path('api/users',view=views.listUsers, name='api/users'),
    path('api/users/cadUsers',view=views.cadUsers, name='api/users/cadUsers'),
    path('api/users/logUsers',view=views.logUsers, name='api/users/logUsers'),
    #passagem de parâmetro no python Django
    #path('api/users/updateUsers/<int:id>',view=views.updateUser, name='api/users/updateUser'),
    #path('api/users/deleteUser/<int:id>',view=views.deleteUser, name='api/users/deleteUser'),
    
    path('',view=views.index, name='index'),
    path('dashboard/',view=views.dashboard, name='dashboard'),

    path('index/',view=views.index, name='index'),
    path('login/',view=views.login, name='login'),
    path('cadastro/',view=views.cadastro, name='cadastro'),
    path('criarGrupos/',view=views.criarGrupo, name='criarGrupos')





]