from celery import shared_task as celery_shared_task  
# Renomeando a importação local para evitar conflito
from time import sleep




@celery_shared_task  # Usando a importação renomeada
def tarefa_simples():
    sleep(5)  # Simulação de uma tarefa simples que leva 5 segundos
    return 'Tarefa simples concluída!'

@celery_shared_task  # Usando a importação renomeada
def tarefa_com_parametro(parametro):
    sleep(10)  # Simulação de uma tarefa com parâmetro que leva 10 segundos
    return f'Tarefa com parâmetro concluída! Referente ao usuário {parametro}'



