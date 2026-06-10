from django.shortcuts import render, redirect, get_object_or_404
from dashboard import models
from datetime import datetime



from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render, redirect
from django.contrib import messages


from django.http import JsonResponse
# Create your views here.

def criarGrupo(request):
    if request.method == 'POST':
        # Busque os dados no banco
        streamings = models.Streaming.objects.all()
        planos = models.Plano.objects.all()

        context = {
            'streamings': streamings,
            'planos': planos
        }
        
    #users = list(models.Users.objects.values('id', 'name', 'email'))
    
    #return JsonResponse({'users':users})
def listUsers(request):
    #if request.method == 'GET':
        #users = models.Users.objects.all
        #return render(request, 'create_users.html',{'users':users})
    users = list(models.Users.objects.values('id', 'name', 'email'))
    
    return JsonResponse({'users':users})


def logUsers(request):
    if request.method == 'POST':
        email_ou_username = request.POST.get('nome')
        senha_digitada = request.POST.get('senha')
        print(f"Email ou Username: {email_ou_username}, Senha: {senha_digitada}")

        #chegando None......
        # O authenticate busca o usuário e compara a senha digitada com o HASH salvo no banco
        user = authenticate(request, username=email_ou_username, password=senha_digitada,)

        if user is not None:
            # O login() cria o cookie seguro no navegador e inicia a sessão ativa
            django_login(request, user)
            print("Usuário e Senha corretos.")

            return redirect('dashboard')
        else:
            print("Usuário ou senha incorretos.")
            messages.error(request, 'E-mail ou senha incorretos.')
            return render(request, 'login.html')

    
def cadUsers(request):
    if request.method == 'POST':
        
        name = request.POST.get("nome")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        #validação
        #..... model:
        user = models.Participante(name=name, email = email,senha = senha)
        user.set_password(senha)
        #persistencia
        user.save()
        return redirect("login")
    
def updateUser(request,id):
    user = get_object_or_404(models.Users, id = id) 
    if request.method == 'POST':
        
        name = request.POST.get("name")
        email = request.POST.get("email")
        #validação
        #..... model...atualizando:
        user.name=name
        user.email = email
        #persistencia
        user.save()
        return redirect("index")

def deleteUser(request,id):
    user = get_object_or_404(models.Users, id = id) 
    user.delete()
    return redirect("index")


#redirects
def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def cadastro(request):
    return render(request, 'cadastro.html')
def dashboard(request):
    return render(request, 'dashboard.html')