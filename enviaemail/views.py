from django.shortcuts import render
from django.http import HttpResponse 
from django.core.mail import send_mail 


# Create your views here.
def envia_email(request):
    send_mail('Assunto', 'Esse é o e-mail de boas vindas!', 'siqueira.email.practice@gmail.com', ['curso.siqueira@gmail.com'])
    return HttpResponse('Bem vindo!')