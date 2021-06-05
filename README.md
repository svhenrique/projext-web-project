# projext-web-project

## Sobre o Projeto
### Gerenciador de Ambientes Para Votação

Aplicação que simula um ambiente de votação. Será possível criar diferentes ambientes, com diferentes coisas para votar por algum motivo e, nesses ambientes, terá um tempo definido até o encerramento da votação e contagem de resultados.

## Features 

- Você poderá criar um ambiente (câmara) de votação com vários objetos, sendo que os objetos podem ser pessoas, coisas, etc.
- Podem existir diversos ambientes simultaneamente.
    - Objetos só podem pertencer a um ambiente de votação.
- Um ambiente terá o motivo da votação.
- Sobre o tempo para terminar a votação.
    - Se esse tempo terminar deve-se mostrar o resultado dos votos quando uma requisição para o mesmo for feita.
    - Caso o tempo não tenha terminado, mostrará o andamento da votação e a opção de votar.
- As votações só poderão ser criadas por um superuser.
    
## Tecnologias usadas
<p align='center'>
    <a href="https://www.python.org/">
        <img src='https://img.shields.io/badge/python-3776AB?logo=python&logoColor=white&style=for-the-badge' />
    </a>
    <a href="https://www.djangoproject.com/">
        <img src='https://img.shields.io/badge/django-092E20?logo=django&logoColor=white&style=for-the-badge' />
    </a>
</p>

## Configuração do ambiente 

É necessária a instalação da linguagem Python. É possível baixa-la aqui:

- https://www.python.org/downloads/

Passo a passo da instalação da linguagem pode ser encontrado aqui:

- https://wiki.python.org/moin/BeginnersGuide/Download

É recomendável que se use um ambiente virtual para utilização da aplicação. Mas antes, é preciso baixar a biblioteca virtualenv e para fazer isso, basta executar o comando:


```bash
pip install virtualenv
```

Para criar um ambiente virtual no python, fazemos:

```bash
virtualenv venv
```

Após criar o ambiente virtual, se você estiver no prompt de comando (shell, terminal, cmd, etc), é preciso ativar o venv (ambiente virtual) criado, para isso utilizamos o comando:

```bash
venv/bin/activate
```

## Instalando dependências

Para instalar dependências, basta usar o comando:
```bash
pip install -r requirements.txt
```

## Executando o projeto

Após a instalação das dependências, é preciso executar o seguinte comando, que é:

```bash
python manage.py migrate
```

Com as migrações feitas no banco de dados, já pode-se iniciar o servidor com o comando:

```bash
python manage.py runserver
```
