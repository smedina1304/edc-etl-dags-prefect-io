<p align="center">
   <img src="https://images.ctfassets.net/gm98wzqotmnx/3Ufcb7yYqcXBDlAhJ30gce/c237bb3254190795b30bf734f3cbc1d4/prefect-logo-full-gradient.svg" width="200" style="max-width: 200px;">
</p>

# dags-prefect-io
## Objetivo:
Este projeto tem como base o *[PREFECT CORE](https://www.prefect.io/core)* (open-source workflow). Estaremos buscando atender o processamento de Dataflows distribuidos pelo engine do prefect executando de forma direta na linha de comando via `python` ou em docker containers, viabilizando o processamento distribuido, utilizando o ambiente em nuvem do *[prefect.io](https://www.prefect.io/)* como orquestrador e dashboard dos processos.

<br>

Link para referência de documentação do PREFECT CORE: 
- https://www.prefect.io/core
- https://docs.prefect.io/core/

<br>

## 1- Preparação do Ambiente de Desenvolvimento:
O ambiente de desenvolvimento será composto:
- Linguagem Python 3.8 (ou superior)
- VS Code (IDE)
- Plugins (requeridos): 
   - Python extension for VS Code.
   - Pylance

<br>

1.1- Criação do ambiente de virtual Python para download das libs do Prefect.
<br>
Obs: todos os comandos ou ações abaixo deveram ser executadas no diretório base do projeto "dags-perfect-io".
<br>
<br>

1.2- Criando o ambiente virtual chamado **`"venv"`**:
<br>

```shell
   > python -m venv venv
```
<br>

Obs: No windows para funcionamento do **`"venv"`** pode ser necessário executar o seguinte comando via Powershell:
<br>

```shell
   > Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
<br>

1.3- Ativando o ambiente virtual **`"venv"`**:
<br>
<br>

No Windows via Powershell utilizar "`activate.bat`".
<br>

```shell
   > .\venv\Scripts\Activate.ps1
```
<br>

No Windows via CMD utilizar "`activate.bat`".
<br>

```shell
   > .\venv\Scripts\activate.bat
```

<br>
No `Linux` ou `MAC` utiliar "`activate`".
<br>

```console
   > source .venv/bin/activate
```
<br>

Para verificar que está funcionando e o ambiente foi ativado, deve aparecer o nome do ambiente destacado com prefixo do seu prompt de comandos, conforme abaixo:
<br>

```shell
   (venv)
```
<br>

Para desativar o ambiente virtual **`"venv"`**:
<br>

```console
   > deactivate
```
<br>

`ATENÇÃO:` Este comando deve ser usado apenas quando não mais for necessário execução no ambiente no ambiente virtual.

<br>
<br>

1.4- Instalação do pacote do Prefect no **`"venv"`**, detalhamento no link de documentação do produto https://docs.prefect.io/core/getting_started/installation.html 
<br>

```shell
   > pip install prefect
```
<br>
<br>
Dependencias Opcionais:<br>

O Prefect vem com várias dependências opcionais, que podem ser instaladas usando a sintaxe `"extras"`, seguir as instruções no site se necessário alguma instalação adicional.
<br>

```shell
   > pip install "prefect[extra_1, extra_2]"
```
<br>
<br>

`Obervação:` todos os pacotes necessário para executar as DAGs contidas neste projeto estão em `requirements.txt`. Para executar a instalação segue o comanto abaixo.
<br>

```shell
   > pip install -r requirements.txt
```
<br>
<br>

## 2- Conta no Prefect Cloud:

2.1- Criação de uma conta no ambiente em nuvem do Prefect. Importante os dados contidos nas intruções abaixo foram atualizadas com base em julho/2021, caso alguma difierença for observada seguir as instruções existentes no site do produto.
<br>

2.2- Acessar https://www.prefect.io/ e selecionar a opção `"GET STARTED"`:<br>
<br>
<p align="left">
   <img src="docs\images\prefect-getstarted-01.png" width="400" style="max-width: 400px;">
</p>
<br>

2.3- Buscar na tela a opção `"START FOR FREE"`
<br>
<p align="left">
   <img src="docs\images\prefect-getstarted-02.png" width="400" style="max-width: 400px;">
</p>
<br>

2.4- Informar uma conta de email para conexão, ou a conta do Google ou GitHub:
<br>
<p align="left">
   <img src="docs\images\prefect-getstarted-03.png" width="200" style="max-width: 200px;">
</p>
<br>
Não é necessário entrar com informações de cartão de credito. Após a informação da conta de acesso, será necessário confirmar um nome para conta e uma url para compartilhamento entre um grupo. Estes pontos não serão relevantes e abordados neste tutorial, assim confirme as informações para validar o acesso e seguir para o Dashboard.
<br>
<br>

Ocorrendo tudo ok, será apresentada a tela abaixo, acesse o dashboard para verificar o seu ambiente:
<br><br>
<p align="left">
   <img src="docs\images\prefect-getstarted-04.png" width="400" style="max-width: 400px;">
</p>
<br>

## 3- Parametrizações do Prefect no ambiente:

3.1- Definindo as configurações para o Prefect utilizar o "`Backend de Orquestração`" em Nuvem. O Prefect suporta dois tipos de backend, Cloud(Nuvem do próprio Prefect) e Server(Sua Infraestrutura), com o objetivo é a utilização em nuvem seguiremos com esta opção. Instruções no Link: https://docs.prefect.io/orchestration/tutorial/overview.html#select-an-orchestration-backend
<br>
<br>

3.2- Devemos rodar o seguinte comando no **`"venv"`** do nosso projeto para direcionar para nuvem:
<br>

```shell
   > prefect backend cloud
```
<br>
Assim que executado o comando deve ser retornado a sequinte mensagem:
<br>

```shell
   Backend switched to cloud
```
<br>
<br>

3.3- Definindo o API key e configurando no ambiente:

- Acessar a sua conta em: https://cloud.prefect.io.

- Navegue até [API Keys page](https://cloud.prefect.io/user/keys). No menu do usuário no canto superior direito, vá para `Account Settings -> API Keys -> Create An API Key`.

- Copie a chave criada, e guarde em lugar seguro.

- Entrar com o comando do `Prefect CLI`.
<br>

```shell
   > prefect auth login --key <YOUR-KEY>
```
<br>
Assim que executado o comando deve ser retornado a sequinte mensagem, confirmando a configuração com sua conta no Prefect Cloud:
<br>

```console
   Logged in to Prefect Cloud tenant 'XXXXX Account' (xxxxxx-xxxx-xxxxx)
```
<br>


Obs: Para este tutorial foi gerado uma chave com validade apenas para ilustrar este tutorial, porem a mesma foi inativada logo depois. Então é necessário você gere a chave com o seu usuário e a utilize para rodar este exemplo.
<br>
<p align="left">
   <img src="docs\images\prefect-API-Key-01.png" width="200" style="max-width: 200px;">
</p>

<br>
<br>

3.4- Para consulta de suas chaves no ambiente do Prefect, pode ser utilizado o comando abaixo:
<br>

```shell
   > prefect auth list-keys
```
<br>
Para mais detalhes sobre as chaves consultar a documentação oficial em: https://docs.prefect.io/orchestration/concepts/api_keys.html#using-api-keys
<br>
<br>

## 4- Executando o Primeiro Teste:

4.1- Primeiro Teste para validar toda preparação e configuração do ambiente.
<br>

4.2- Verifique o código de exemplo em `*'dags\flow-test-hello\test-hello.py'*`.
<br>
<br>

4.3- Observe que no final do código existe uma instrução de registro, especificando um projeto. É necessário que seja criado o projeto `*'My Tests'*` para que o `*Agent*` registre o Flow no Prefect e o mesmo possa ser monitorado.
<br>
- Criando o projeto via comando no terminal:
<br>

```python
prefect create project 'My Tests'
```
<br>
Sendo executando com sucesso o comando deverá retornar a seguinte mensagem:
<br>

```console
My Tests created
```

<br>
<br>

- Criando o Projeto via Dashboard Prefect Cloud:
<br>
- Acesse o seu ambiente no Prefect Cloud: https://cloud.prefect.io.

- No lado Direito, próximo ao canto superior, clique em: `All Project -> New Project`.
   <br>
   <p align="left">
      <img src="docs\images\prefect-New-Project-01.png" width="200" style="max-width: 200px;">
   </p>

   - Entre com o nome do projeto *'My Tests'* e confirme.
   <br>
   <p align="left">
      <img src="docs\images\prefect-New-Project-02.png" width="200" style="max-width: 200px;">
   </p>

- Selecione o projeto para visualizar os Flow que forem ou estiverem registados, no mesmo caminho da criação, porem agora selecionando o Projeto Desejado.
   <br>
   <p align="left">
      <img src="docs\images\prefect-New-Project-03.png" width="200" style="max-width: 200px;">
   </p>
<br>
<br>

4.4- Executando o Flow `*'dags\flow-test-hello\test-hello.py'*`.
<br>

- No terminal, acesse a pasta do Flow `*'dags\flow-test-hello'*` e execute a chamada via Python:
<br>

```python
cd .\dags\flow-test-hello
python test-hello.py
```
<br>
Sendo executando com sucesso o comando deverá retornar uma mensagem similar:
   <br>
   <p align="left">
      <img src="docs\images\prefect-Run-Test-01.png" width="500" style="max-width: 500px;">
   </p>
<br>

- No Prefect Cloud, na Dashbord Agent, poderá verifica o registro do seu processo. Navegue no seu Dashbord para verificar as informações disponibilizadas e conhecer os recursos:
<br>
<p align="left">
   <img src="docs\images\prefect-Run-Test-02.png" width="200" style="max-width: 200px;">
</p>
<br>

- Localize a opção `FLOWS` no Menu abaixo ao Nome do Projeto e acesse, em seguida localize na lista o flow `'flow-test-hello'`, e acesse:
<br>
<p align="left">
   <img src="docs\images\prefect-Run-Test-03.png" width="200" style="max-width: 200px;">
</p>
<br>

- Para Executar de forma manual utilize o `QUICK RUN`:
<br>
<p align="left">
   <img src="docs\images\prefect-Run-Test-04.png" width="70" style="max-width: 70px;">
</p>
<br>

- Após executar verifique e navegue no Dashboard para analisar as informações registradas:
<br>
<p align="left">
   <img src="docs\images\prefect-Run-Test-05.png" width="500" style="max-width: 500px;">
</p>
<br>  

- Para analisar o `LOG` da execução, acesse `RUNS -> [Name ID \ Start Datetime ] -> LOGS`. Como foi utilizado a opção `QUICK RUN` o Prefect define de forma aleatório um ID (Name) como label da execução, para este exemplo foi `rose-sloth`, este nome pode ser alterado no dashboar passando os parametros para executar ou pelo próprio códido, para detalhes busque na documentação:
<br>
<p align="left">
   <img src="docs\images\prefect-Run-Test-06.png" width="500" style="max-width: 500px;">
</p>
<br>

Acima a mensagem escrita no `LOG`, foi definida pela instrução no código pela task `say_hello()`:
<br>

```python
@task
def say_hello():
   logger = prefect.context.get("logger")
   logger.info("Test Hello, Cloud!")
```
<br>
<br>

## 5- Executando em um Container Docker:
<br>

**`ATENÇÃO - É PRE-REQUISITO QUE ESTE INSTALADO OS RECURSOS DE DOCKER NA MÁQUINA ONDE ESTES PROCEDIMENTOS FOREM SER REALIZADOS. VERIFIQUE ANTES DE INICIAR!`**

<br>

5.1- Inicialmente é necessário criar um arquivo de configuração do seu container docker com base em uma imagem, normalmente verifica-se os pré-requisitos necessário para a aplicação com base no sistema operacional. Neste caso foi selecionada a imagem `python:3.8-slim-buster`, que já disponibiliza a instalação do python 3.8 em um sistema baseado em linux, ficando assim a necessidade de configurar a instalação dos pacotes necessários e o programas para serem executados.
<br>

Iniciamos com a criação de um arquivo `Dockerfile` conforme abaixo:
<br>

```dockerfile
   # Definição da Imagem, para detalhes ver: https://aka.ms/vscode-docker-python
   FROM python:3.8-slim-buster

   # Desabilita a geração dos arquivos .pyc no contêiner pelo Python
   ENV PYTHONDONTWRITEBYTECODE=1

   # Desativa o armazenamento em buffer para facilitar o registro do contêiner
   ENV PYTHONUNBUFFERED=1

   # Variaveis de Ambiente para parametrização de chamada da DAG
   ENV PREFECT_AUTH_KEY $PREFECT_AUTH_KEY
   ENV DAG_PATH $DAG_PATH
   ENV DAG_NAME $DAG_NAME

   # Instalação dos pacotes requeridos
   COPY requirements.txt .
   RUN pip3 install --no-cache -r requirements.txt

   # Copia e define as permissão para o script que irá executar a chamada da DAG via Python
   COPY run_in_docker.sh .
   RUN chmod 755 run_in_docker.sh

   # Define o diretorio de trabalho e a copia dos scripts
   WORKDIR /app
   COPY dags/ /app/dags
   COPY data/ /app/data

   # Cria um usuário não root com um UID explícito e adiciona permissão para acessar a 
   # pasta do aplicativo
   # Mais detelhes consultar: https://aka.ms/vscode-docker-python-configure-containers
   RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
   USER appuser

   # Execute Script
   CMD ["/run_in_docker.sh"]
```

<br>
<br>

5.2- Após a criação do Dockerfile e toda a estrutura de dados e programas que serão executados, é necessário realizar o `Build` da imagem para tornar utilizavel com um container. Para realizar esta atividade executar o comando `docker build` conforme sintax abaixo:
<br>

```shell
   > docker build -f Dockerfile -t smedina1304/myprefectdags:v1.3 .
```

<br>
Onde:

- `docker build` -> É a instrução o docker realizar a construção da imagem com base no arquivo de configuração.

- `-f Dockerfile` -> O parametro `-f` identifica qual é o arquido com as instruções de construção do container, normalmente utilizado quando o arquivo tem o nome diferente de `Dockerfile`, porem para este exempo o parametro foi deixado explicito para exemplificação do uso, mas para este caso não seria necessário.

- `-t smedina1304/myprefectdags:v1.3` -> O parametro `-t` indica qual é a TAG de identificação da imagem do container, onde as informações que a compõem são: `[ID REPOSITORIO]/[ID CONTAINER]:[VERSAO]`, sendo `/` e `:` separadores. O [ID REPOSITORIO] é a identificação de onde o container será armazenado, por exemplo no `Docker Hub` ou `AWS`, porem se for apenas uma imagem local não será necessário. O [ID CONTAINER] é o nome de identificação do container e deve sempre ser informado. A [VERSAO] também chamado de `TAG` é onde se identifica a versão, também utilizado para fins de armazenamento. Atenção é necessário que todas as letras estejam em minusculo para todos os elementos informados no parametro `-t`.

- `.` --> Esta é o parametro que indica onde é o diretório base do processo de construção do container e neste caso indica o diretório corrente.

<br>

Ao executar o comando o processo deve executar os downloads das partições necessárias para montar a imagem e iniciar a construção. Também todos os comandos definidos no `Dockerfile` são executados de demonstrados na tela para acompanhamento. Para verificar se a imagem foi montada execute o comando conforme abaixo:

<br>

```shell
   > docker images
```

O retorno de ser semelhante ao abaixo:

```shell
   REPOSITORY                  TAG       IMAGE ID       CREATED          SIZE
   smedina1304/myprefectdags   v1.3      1fcc69fb574b   16 minutes ago   270MB   
```

<br>

5.2- Com a imagem criada e disponível no repositório local, o próximo passo é testar o funcionamento, mas antes vamos entendar alguns parametros definidos no `Dockerfile`:
<br>

Localize do arquivo os parametros abaixo:

```dockerfile
# Variaveis de Ambiente para parametrização de chamada da DAG
   ENV PREFECT_AUTH_KEY $PREFECT_AUTH_KEY
   ENV DAG_PATH $DAG_PATH
   ENV DAG_NAME $DAG_NAME
```

Estas 3 variáveis de ambiente foram incluidas nas imagem para possibilitar a configuração dinâmica do ambiente no container no momento do startup, são elas:

- `PREFECT_AUTH_KEY` -> Utilizada para autenticação no ambiente Cloud do Prefect utilizando a `API Key` gerada na configuração do ambiente em cloud (verificar item 3.3 deste documento).

- `DAG_PATH` -> Utilizado para informar o caminho da pasta (`path`) onde está o programa (`DAG`) que será executada.

- `DAG_NAME` -> Utilizado para informar o nome do programa (`DAG`) que será executada.

Estas variáveis de ambientes, serão utilizadas pelo script shell `run_in_docker.sh`, conforme abaixo:

```shell
   #!/bin/bash

   ## Exibe as variaveis DAG_PATH e DAG_NAME na console
   echo "-> RUN IN DOCKER..."
   echo "DAG_PATH: " $DAG_PATH
   echo "DAG_NAME: " $DAG_NAME

   ## Define o 'Time Zone' para o Brasil verifique o mais
   ## adequado para o seu cenário 
   echo "-> SETUP: TZ = UTC"
   #export TZ=America/Sao_Paulo
   export TZ=UTC

   ## Configura o pacote Prefect instalado no Python do container
   ## para utilizar o ambiente em Cloud
   echo "-> Prefect Backend Cloud..."
   prefect backend cloud

   ## Executa o processo de autenticação na Cloud Prefect
   ## utilizando a API KEY
   echo "-> Login..."
   prefect auth login --key $PREFECT_AUTH_KEY

   ## Acessa a pasta da DAG que será executada
   cd $DAG_PATH

   ## Display da pasta atual e executa a DAG definida na variavel DAG_NAME
   echo "Iniciando DAG"
   pwd
   python3 $DAG_NAME
```
<br>

Com o entendimento dos parametros configurados via variáveis de ambiente descritos acima, para podermos executar o container localmente devemos utilizar o comando abaixo.

```shell
   > docker run -t -i -e PREFECT_AUTH_KEY='<KEY>' -e DAG_PATH='/app/dags/flow-test-hello' -e DAG_NAME='test-hello.py' --rm --name prefect smedina1304/myprefectdags:v1.3
```

Onde:

- `docker run` -> É o comando para executar o container no ambiente.

- `-t` -> Mostra a saida TTY.

- `-i` -> Disponibiliza STDIN para interação com o container.

- `-e` -> Define as variáveis de ambiente.
   - `PREFECT_AUTH_KEY='<KEY>'` -> valor da API Key do Cloud Prefect, que deve ser informada no lugar de `<KEY>`.
   - `DAG_PATH='/app/dags/flow-test-hello'` -> valor com o `path` onde será executado o programa (`DAG`) para o prefect.
   - `DAG_NAME='test-hello.py'` -> valor com o `nome` do programa (`DAG`) que será executada.

- `--rm` -> Informar ao docker que o container deve ser removido assim que finalizado.

- `--name prefect` -> Nome que será atribuido ao container em execução, no caso `prefect`. 

- `smedina1304/myprefectdags:v1.3` -> É a identificação da imagem que será utilizada para executar o container.

<br>

Ao executar o comando com os parametros *`-t -i`* será apresentado similar ao seguinte output:

```shell
   -> RUN IN DOCKER...
   DAG_PATH:  /app/dags/flow-test-hello
   DAG_NAME:  test-hello.py
   -> SETUP: TZ = UTC
   -> Prefect Backend Cloud...
   Backend switched to cloud
   -> Login...
   Logged in to Prefect Cloud tenant 'SMedina Account' (smedina1304-team-s-account)
   Iniciando DAG
   /app/dags/flow-test-hello
   Flow URL: https://cloud.prefect.io/smedina1304-team-s-account/flow/ddbc922e-c398-87d58b852025
   └── ID: 11d0b127-9a83-81b162b0237b
   └── Project: My Tests
   └── Labels: ['4ef5edf02069']
   [2021-09-21 17:06:38,435] INFO - agent | Registering agent...
   [2021-09-21 17:06:38,717] INFO - agent | Registration successful!

   ____            __           _        _                    _
   |  _ \ _ __ ___ / _| ___  ___| |_     / \   __ _  ___ _ __ | |_
   | |_) | '__/ _ \ |_ / _ \/ __| __|   / _ \ / _` |/ _ \ '_ \| __|
   |  __/| | |  __/  _|  __/ (__| |_   / ___ \ (_| |  __/ | | | |_
   |_|   |_|  \___|_|  \___|\___|\__| /_/   \_\__, |\___|_| |_|\__|
                                             |___/

   [2021-09-21 17:06:39,003] INFO - agent | Starting LocalAgent with labels ['4ef5edf02069']
   [2021-09-21 17:06:39,003] INFO - agent | Agent documentation can be found at https://docs.prefect.io/orchestration/
   [2021-09-21 17:06:39,004] INFO - agent | Waiting for flow runs...
```


