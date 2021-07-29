<p align="center">
   <img src="https://images.ctfassets.net/gm98wzqotmnx/3Ufcb7yYqcXBDlAhJ30gce/c237bb3254190795b30bf734f3cbc1d4/prefect-logo-full-gradient.svg" width="200" style="max-width: 200px;">
</p>

# dags-prefect-io
## Objetivo:
Este projeto tem como base o [PREFECT CORE](https://www.prefect.io/core) (open-source workflow). Estaremos buscando atender o processamento de Dataflows distribuidos pelo engine do prefect executando em docker containers, viabilizando o processamento distribuido, utilizando o ambiente em nuvem do [prefect.io](https://www.prefect.io/) como gerenciador e visualizador dos processos.

<br>

Link para referência de documentação do PREFECT CORE: 
- https://www.prefect.io/core
- https://docs.prefect.io/core/

<br><br>
## Preparação do Ambiente de Desenvolvimento:
O ambiente de desenvolvimento será composto:
- VS Code (IDE)
- Linguagem Python 3.9 (ou superior)

<br>

1. Criação do ambiente de virtual Python para download das libs do Prefect.
<br>
Obs: todos os comandos ou ações abaixo deveram ser executadas no diretório base do projeto "dags-perfect-io".
<br>

   1.1. Criando o ambiente virtual chamado **"venv"**:<br>

   ```console
   python -m venv venv
   ```
   <br>
   Obs: No windows para funcionamento do "venv" pode ser necessário executar o seguinte comando via Powershell: <br>

   ```console
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
   ```
   <br><br>
   1.2. Ativando o ambiente virtual **"venv"**:
   <br>

   ```console
   .\venv\Scripts\Activate.ps1
   ```
   Obs: via CMD utilizar "`activate.bat`", no `Linux` ou `MAC` utiliar "activate".
   <br>

   Para verificar que está funcionando e o ambiente foi ativado, deve aparecer o nome do ambiente destacado com prefixo do seu prompt de comandos, conforme abaixo:
   
   ```js
   '(venv)' PS C:\Users\ych885\Documents\Sources\dags-prefect-io>
   ```
   <br>
   Para desativar o ambiente virtual **"venv"**:

   ```console
   deactivate
   ```
   `ATENÇÃO:` Este comando de ser usado apenas quando não mais for necessário execução no ambiente.
   <br>
   <br>

   1.3. Instalação do pacote do Prefect no **"venv"**, detalhamento no link de documentação do produto https://docs.prefect.io/core/getting_started/installation.html 
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

3. Definindo as configurações para o Prefect utilizar o "`Backend de Orquestração`" da Nuvem. O Prefect suporta dois tipos de backend, Cloud(Nuvem do próprio Prefect) e Server(Sua Infraestrutura), com o objetivo é a utilização em nuvem seguiremos com esta opção. Instruções no Link: https://docs.prefect.io/orchestration/tutorial/overview.html#select-an-orchestration-backend
<br>
<br>

   3.1. Assim devemos rodar o seguinte comando no **venv** do nosso projeto:
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
   Assim que executado o comando deve ser retornado a sequinte mensagem:
   <br>

   ```console
   Logged in to Prefect Cloud tenant 'XXXXX Account' (xxxxxx-team-s-account)
   ```
   <br>
   <br>


   Obs: Para este tutorial foi gerado uma chave com validade, apenas para ilustrar este tutorial, porem a mesmo foi inativada logo depois.
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














