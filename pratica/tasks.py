from celery import shared_task as celery_shared_task  
# Renomeando a importação local para evitar conflito
from time import sleep
from django.contrib.auth.models import User
from django.http import HttpResponse 
from django.core.mail import send_mail 


@celery_shared_task  # Usando a importação renomeada
def tarefa_simples():
    sleep(5)  # Simulação de uma tarefa simples que leva 5 segundos
    return 'Tarefa simples concluída!'

@celery_shared_task  # Usando a importação renomeada
def tarefa_com_parametro(parametro):
    sleep(10)  # Simulação de uma tarefa com parâmetro que leva 10 segundos
    return f'Tarefa com parâmetro concluída! Referente ao usuário {parametro}'

@celery_shared_task
def enviar_email_boas_vindas(user_id):
    user = User.objects.get(pk=user_id)
    #send_mail('E-mail de boas vindas!', 'Olá {user.username}, seja bem-vindo ao nosso site!', 'siqueira.email.practice@gmail.com', [user.email])
    send_mail('E-mail de boas vindas!', 'Olá {username}, seja bem-vindo ao nosso site, PyCelery!'.format(username=user.username), 'siqueira.email.practice@gmail.com', [user.email])
    
    print("E-mail de boas-vindas enviado para", user.email)
    return HttpResponse('Bem vindo!')

'''Agora, sempre que um novo usuário for cadastrado, é agendada a tarefa de enviar
o e-mail de boas-vindas. Por exemplo, no momento do cadastro do usuário!'''

