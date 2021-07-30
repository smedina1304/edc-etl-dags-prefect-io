<p align="center">
   <img src="https://images.ctfassets.net/gm98wzqotmnx/3Ufcb7yYqcXBDlAhJ30gce/c237bb3254190795b30bf734f3cbc1d4/prefect-logo-full-gradient.svg" width="200" style="max-width: 200px;">
</p>

# dags-prefect-io
## Objetivo:
Este projeto tem como base o [PREFECT CORE](https://www.prefect.io/core) (open-source workflow). Estaremos buscando atender o processamento de Dataflows distribuidos pelo engine do prefect executando em docker containers, viabilizando o processamento distribuido, utilizando o ambiente em nuvem do [prefect.io](https://www.prefect.io/) como orquestrador e dashboard dos processos.

<br>

Link para referência de documentação do PREFECT CORE: 
- https://www.prefect.io/core
- https://docs.prefect.io/core/

<br>

## 1- Preparação do Ambiente de Desenvolvimento:
O ambiente de desenvolvimento será composto:
- Linguagem Python 3.9 (ou superior)
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

1.2- Criando o ambiente virtual chamado **"venv"**:
<br>

```console
python -m venv venv
```
<br>
Obs: No windows para funcionamento do "venv" pode ser necessário executar o seguinte comando via Powershell:
<br>

```console
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```
<br>
<br>

1.3- Ativando o ambiente virtual **"venv"**:
<br>

```console
.\venv\Scripts\Activate.ps1
```
<br>
Obs: via CMD utilizar "`activate.bat`", no `Linux` ou `MAC` utiliar "activate".
<br>

Para verificar que está funcionando e o ambiente foi ativado, deve aparecer o nome do ambiente destacado com prefixo do seu prompt de comandos, conforme abaixo:
<br>

```js
'(venv)' PS C:\Users\XXXX\Documents\Sources\dags-prefect-io>
```
<br>
Para desativar o ambiente virtual **"venv"**:
<br>

```console
deactivate
```
<br>
`ATENÇÃO:` Este comando deve ser usado apenas quando não mais for necessário execução no ambiente no ambiente virtual.
<br>
<br>

1.4- Instalação do pacote do Prefect no **"venv"**, detalhamento no link de documentação do produto https://docs.prefect.io/core/getting_started/installation.html 
<br>
```python
pip install prefect
```
<br>
<br>
Dependencias Opcionais:<br>
O Prefect vem com várias dependências opcionais, que podem ser instaladas usando a sintaxe "extras", seguir as instruções no site se necessário alguma instalação adicional.
<br>

```python
pip install "prefect[extra_1, extra_2]"
```
<br>
<br>

## Conta no Prefect Cloud:

2. Criação de uma conta no ambiente em nuvem do Prefect. Importante os dados contidos nas intruções abaixo foram atualizadas com base em julho/2021, caso alguma difierença for observada seguir as instruções existentes no site do produto.
<br>

   2.1. Acessar https://www.prefect.io/ e selecionar a opção "GET STARTED":<br>
   <br>
   <p align="left">
      <img src="docs\images\prefect-getstarted-01.png" width="400" style="max-width: 400px;">
   </p>
   <br>

   2.2. Buscar na tela a opção "START FOR FREE"
   <br>
   <p align="left">
      <img src="docs\images\prefect-getstarted-02.png" width="400" style="max-width: 400px;">
   </p>
   <br>

   2.2. Informar uma conta de email para conexão, ou a conta do Google ou GitHub:
   <br>
   <p align="left">
      <img src="docs\images\prefect-getstarted-03.png" width="200" style="max-width: 200px;">
   </p>
   <br>
   Não é necessário entrar com informações de cartão de credito.
   Após a informação da conta de acesso, será necessário confirmar um nome para conta e uma url para compartilhamento entre um grupo. Estes pontos não serão relevantes e abordados neste tutorial, assim confirme as informações para validar o acesso e seguir para o Dashboard.
   <br>
   Ocorrendo tudo ok, será apresentada a tela abaixo, acesse o dashboard para verificar o seu ambiente:
   <br><br>
   <p align="left">
      <img src="docs\images\prefect-getstarted-04.png" width="400" style="max-width: 400px;">
   </p>
   <br>

## Parametrizações do Prefect no ambiente:

3. Definindo as configurações para o Prefect utilizar o "`Backend de Orquestração`" em Nuvem. O Prefect suporta dois tipos de backend, Cloud(Nuvem do próprio Prefect) e Server(Sua Infraestrutura), com o objetivo é a utilização em nuvem seguiremos com esta opção. Instruções no Link: https://docs.prefect.io/orchestration/tutorial/overview.html#select-an-orchestration-backend
<br>
<br>

   3.1. Devemos rodar o seguinte comando no **venv** do nosso projeto para direcionar para nuvem:
   <br>

   ```shell
   prefect backend cloud
   ```
   <br>
   Assim que executado o comando deve ser retornado a sequinte mensagem:
   <br>

   ```python
   Backend switched to cloud
   ```
   <br>
   <br>

   3.2. Definindo o API key e configurando no ambiente:

   - Acessar a sua conta em: https://cloud.prefect.io.

   - Navegue até [API Keys page](https://cloud.prefect.io/user/keys). No menu do usuário no canto superior direito, vá para `Account Settings -> API Keys -> Create An API Key`.

   - Copie a chave criada, e guarde em lugar seguro.

   - Entrar com o comando do `Prefect CLI`.
   <br>

   ```python
   prefect auth login --key <YOUR-KEY>
   ```
   <br>
   Assim que executado o comando deve ser retornado a sequinte mensagem, confirmando a configuração com sua conta no Prefect Cloud:
   <br>

   ```console
   Logged in to Prefect Cloud tenant 'XXXXX Account' (xxxxxx-team-s-account)
   ```
   <br>
   <br>


   Obs: Para este tutorial foi gerado uma chave com validade, apenas para ilustrar este tutorial, porem a mesma foi inativada logo depois.
   <br><br>
   <p align="left">
      <img src="docs\images\prefect-API-Key-01.png" width="200" style="max-width: 200px;">
   </p>

   <br>
   <br>

   3.3. Para consulta de suas chaves no ambiente do Prefect, pode ser utilizado o comando abaixo:
   <br>

   ```python
   prefect auth list-keys
   ```
   <br>
   Para mais detalhes sobre as chaves consultar a documentação oficial em: https://docs.prefect.io/orchestration/concepts/api_keys.html#using-api-keys
   <br>
   <br>
   <br>

## Executando o Primeiro Teste:

4. Primeiro Teste para validar toda preparação e configuração do ambiente.
<br>

   4.1. Verifique o código de exemplo em *'dags\flow-test-hello\test-hello.py'*
   <br>
   <br>
   4.2. Observe que no final do código existe uma instrução de registro, especificando um projeto. É necessário que seja criado o projeto *'My Tests'* para que o *Agent* registre o Flow no Prefect e o mesmo possa ser monitorado.
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
   4.3. Executando o Flow *'dags\flow-test-hello\test-hello.py'*
   <br>

      - No terminal, acesse a pasta do Flow *'dags\flow-test-hello'* e execute a chamada via Python:
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
         Acima a mensagem escrita mo LOG, foi definida pela instrução escrita no código pela task `say_hello()`:
         <br>
         
         ```python
         @task
         def say_hello():
            logger = prefect.context.get("logger")
            logger.info("Test Hello, Cloud!")
         ```
         <br>
         <br>












