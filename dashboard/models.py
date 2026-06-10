from django.db import models

# Create your models here.
class User(models.Model):
    #o jeito Django de classes abstratas 
    username = models.CharField(max_length=45)
    email = models.EmailField()
    senha = models.CharField(max_length=128)

    
    class Meta:
        abstract = True
    def deletar_conta(self):
        self.delete()
        
class Streaming(models.Model):
    name = models.CharField(max_length=45)
    url = models.CharField(max_length=255,default="https://teste.com")
    categoria = models.CharField(max_length=128,default="Video")

    def __str__(self):
        return self.name
    
class Plano(models.Model):
    name = models.CharField(max_length=45)
    preco_mensal = models.FloatField()
    qualidade_video = models.CharField(max_length=30)
    ativo = models.BooleanField()
    quantidade_telas = models.IntegerField()
    anuncio = models.BooleanField()

class Participante(User):
    data_cadastro= models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True) 

class Grupo(models.Model):
    name = models.CharField(max_length=45)
    descricao = models.CharField(max_length=255)
    plano = models.ForeignKey(Plano, on_delete=models.CASCADE)
    streaming = models.ForeignKey(Streaming, on_delete=models.CASCADE)


    
