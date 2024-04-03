# Changelog
## Versão 2.5
  - Nova funcionalidade adicionada: Envio de e-mail de boas-vindas para novos usuários.
  - Foi criado um novo decorador chamado @celery_shared_task para agendar o envio do e-mail.
  - O e-mail de boas-vindas contém o nome do usuário e uma mensagem personalizada.
  
## Versão 2.0
  - Funcionalidades de cadastros, login e logout de usuários implementadas no arquivo views.py.
  - Foram utilizados os decoradores @celery_shared_task para agendar tarefas assíncronas.
  - As funções de cadastro, login e logout foram integradas com o Celery para execução assíncrona.
