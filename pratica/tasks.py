from celery import shared_task as celery_shared_task  
# Renomeando a importação local para evitar conflito
from time import sleep
from django.core.mail import send_mail
from django.contrib.auth.models import User



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
    user = User.objects.get(pk=user_id) #*id do usuário
    send_mail('Bem-vindo!',f'Olá {user.username}, seja bem-vindo ao nosso site!', #*identifico-o pelo nome
              'holandalhs@gmail.com',
              [user.email],
              fail_silently=False,
    )

'''Agora, sempre que um novo usuário for cadastrado, é agendada a tarefa de enviar
o e-mail de boas-vindas. Por exemplo, no momento do cadastro do usuário!'''

