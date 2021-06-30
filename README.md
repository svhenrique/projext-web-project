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
    - Caso o tempo não tenha terminado, mostrara o andamento da votação e a opção de votar.
- As votações só poderão ser criadas por um superuser.
    
## Configuração do ambiente 

### Clonando repositório

Para clonar o repositório é possível baixa-lo completamente do github e extrair em uma pasta de projeto ou utilizar o comando:

```bash
git clone https://github.com/svhenrique/projext-web-project.git
```

Para utilizar o comando anterior é necessário ter o Git instalado no computador.

### Configurando ambiente 

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

## Configurando .env

Crie um arquivo de texto e nomeio para ".env", ou utilize o env.example (lembre-se de renomear para ".env"), e salve na pasta raiz do projeto. Após isso, adicione esses comandos ao arquivo criado:

```bash
SECRET_KEY=COLOQUE_SUA_SECRET_KEY
DEBUG=True
```

Do lado direito, em "COLOQUE_SUA_SECRET_KEY", ponha um hash de SECRET_KEY gerado pelo Django. 

### Algumas maneiras de conseguir o hash

- Iniciando um novo projeto django com:

```bash
django-admin startproject projeto 
```

Copia o hash guardado na variável SECRET_KEY no arquivo settings.py (fazer processo de coleta de SECRET_KEY em outra pasta e em outro ambiente virtual para assegurar o encapsulamento da aplicação) e cola na SECRET_KEY do .env.

- Usando a função get_random_secret_key():

Com o Django instalado, execute o comando

```bash
python manage.py shell
```

no shell, importe a função get_random_secret_key com o comando

```bash
from django.core.management.utils import get_random_secret_key
```

e utilize a função usando

```bash
get_random_secret_key()
```

copie o valor retornado e cole na SECRET_KEY do .env.

- Utilizando Websites:

Existem sites que geram SECRET_KEY do Django. Abra o link abaixo https://djecrety.ir/ e
clique em "Generate", copie o valor gerado e cole na SECRET_KEY do .env.

## Executando o projeto

Após a instalação das dependências, é preciso executar o seguinte comando, que é:

```bash
python manage.py migrate
```

Com as migrações feitas no banco de dados, é possível iniciar o servidor com o comando:

```bash
python manage.py runserver
```
