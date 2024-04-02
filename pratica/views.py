from django.shortcuts import render, redirect
from django.http.response import HttpResponse 
from .tasks import tarefa_simples, tarefa_com_parametro 
from django.contrib.messages import constants 
from django.contrib.auth.models import User  
from django.contrib import messages 
from django.contrib import auth



def home(request):
    tarefa_simples.delay()
    return HttpResponse('<h2> Acesso ao ambiente! </h2>')



def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')  
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not senha == confirmar_senha:  
            messages.add_message(request, constants.ERROR, 'Os campos não coincidem!')
            return redirect('/pratica/cadastro') 
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'O usuário já existe!')
            return redirect('/pratica/cadastro')
   
            
        try:
            User.objects.create_user( 
                username=username,
                email=email,
                password=senha
            )
            # Agendar o envio do e-mail   
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado!!')
            tarefa_com_parametro.delay(username)
            return redirect('/pratica/logar')
        except Exception as e:
            messages.add_message(request, constants.ERROR, 'Erro no servidor: {}'.format(str(e)))
            return redirect('/pratica/cadastro')
        
  

def logar(request):
    if request.method == 'GET': 
        print(request.user)
        return render(request, 'login.html') #**renderizando, o render recebe pelo menos 2 parâmetros
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, senha=senha)
        #print(user)

        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Usuário logado!!')
            tarefa_com_parametro.delay(user)
            return HttpResponse('<h2> Tarefa de login efetuada! </h2>')
            return redirect('/pratica/cadastro')    #*** por enquanto volta pra tela de cadastro
        else:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos!!')
            return redirect('/pratica/logar')


    
       
   
def logout(request):
    tarefa_simples.delay() #**tarefa simples, sem  parâmetros
    auth.logout(request)
    messages.add_message(request, constants.INFO, 'Tarefa de logout registrada!!!')
    return redirect('/pratica/logar')
 
   
