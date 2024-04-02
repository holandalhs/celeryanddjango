# celeryanddjango
###Projeto: Sistema de Cadastro de Usuário Assíncrono com Django e Celery

Descrição:
    O projeto consiste em um sistema de cadastro de usuário desenvolvido utilizando Python, Django e Celery. A principal funcionalidade é permitir que os usuários se cadastrem de forma assíncrona, utilizando tasks com Celery para processar operações em segundo plano. 

Funcionalidades Implementadas:
    Formulário de Cadastro de Usuário
    Tasks com Celery para execução assíncrona de operações

Objetivos Alcançados:
    Integração entre Django e Celery para processamento assíncrono
    Melhoria na experiência do usuário ao cadastrar-se no sistema
    Prática de implementação de tratativas de erro para garantir a robustez da aplicação

Tecnologias Utilizadas:
    Python
    Django
    Celery
    HTML
    CSS

Como Executar o Projeto:
    Clone o repositório do projeto.
    Instale as dependências: pip install -r requirements.txt.
    Execute as migrações do banco de dados: python manage.py migrate.
    Inicie o servidor Django: python manage.py runserver.
    Acesse a aplicação em seu navegador e utilize o formulário de cadastro de usuário.
