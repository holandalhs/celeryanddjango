# celeryanddjango
# Projeto: Sistema de Cadastro de Usuário Assíncrono com Django e Celery

## Descrição
O projeto consiste em um sistema de cadastro de usuário desenvolvido utilizando Python, Django e Celery. A principal funcionalidade é permitir que os usuários se cadastrem de forma assíncrona, utilizando tasks com Celery para processar operações em segundo plano. Além disso, o sistema conta com o envio de e-mails de boas-vindas, execução de tarefas simples e tarefas com parâmetros específicos que leva 10 segundos, agendadas para serem executadas após o cadastro do usuário.

## Funcionalidades Implementadas
1. **Formulário de Cadastro de Usuário**: Utilizamos o framework Django para criar um formulário de cadastro de usuário, que armazena as informações do novo usuário no banco de dados.

2. **Tasks com Celery para execução assíncrona de operações**:
   - `enviar_email_boas_vindas`: Esta task é responsável por enviar um e-mail de boas-vindas para o novo usuário cadastrado. A task é agendada para ser executada 10 segundos após o cadastro do usuário.
   - `tarefa_simples`: Uma task simples que simula uma tarefa de 5 segundos.
   - `tarefa_com_parametro`: Outra task que executa uma tarefa com parâmetros específicos, agendada após o cadastro do usuário.

3. **Tratativas de Erro**:
   - Implementamos tratativas de erro para lidar com possíveis exceções durante o cadastro do usuário, tais como:
     - Erro de validação de dados no formulário de cadastro.
     - Erro de conexão com o banco de dados.
     - Erro no envio do e-mail de boas-vindas.
     - Outros erros inesperados durante o processamento das tasks com Celery.

## Objetivos Alcançados
- Integração entre Django e Celery para processamento assíncrono.
- Melhoria na experiência do usuário ao cadastrar-se no sistema.
- Prática de implementação de tratativas de erro para garantir a robustez da aplicação.

## Tecnologias Utilizadas
- Python
- Django
- Celery
- HTML
- CSS

## Como Executar o Projeto
1. Clone o repositório do projeto.
2. Instale as dependências: `pip install -r requirements.txt`.
3. Execute as migrações do banco de dados: `python manage.py migrate`.
4. Inicie o servidor Django: `python manage.py runserver`.
5. Acesse a aplicação em seu navegador e utilize o formulário de cadastro de usuário.

## Observações Finais
O projeto integra de forma eficiente tarefas assíncronas com Celery no processo de cadastro de usuário, resultando em uma experiência ágil e estável para os usuários, ao mesmo tempo que lida de maneira adequada com possíveis exceções, garantindo a confiabilidade do sistema. Essa integração entre Django e Celery possibilita a execução de processos demorados em segundo plano, melhorando a experiência do usuário e seguindo uma prática comum em aplicações web para lidar com operações assíncronas.

Para mais detalhes e informações sobre o projeto, consulte o README.md e o CHANGELOG.md; e sinta-se à vontade para entrar em contato em caso de dúvidas.
