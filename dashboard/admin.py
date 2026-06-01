from django.contrib import admin

# Register your models here.

from dashboard import models

@admin.register(models.Streaming)

class StreamingAdmin(admin.ModelAdmin):
    list_display = 'id','name','url','categoria'

@admin.register(models.Plano)

class PlanoAdmin(admin.ModelAdmin):
    list_display = 'id','name','preco_mensal','qualidade_video','ativo','quantidade_telas','anuncio'