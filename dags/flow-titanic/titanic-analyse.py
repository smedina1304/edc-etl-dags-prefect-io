import pandas as pd
import requests
import prefect
import os
from prefect import task, Flow, case
from prefect.schedules import IntervalSchedule
from datetime import datetime, timedelta
from io import BytesIO

csvUrl = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
dirPath = '/Users/sergiomedina/Downloads/'
retry_delay = timedelta(minutes=15)

@task
def download_csv(csvUrl, dirPath):
    # Logger
    logger = prefect.context.get("logger")
    logger.info(f"Download CSV: {csvUrl}")

    # request get CSV
    req = requests.get(csvUrl, stream=True)
    if req.status_code == 200:

        # Verificando Diretorio Output
        if not dirPath.endswith('/'):
            dirPath = dirPath + '/'
    
        # Criando a pasta
        dirPath = dirPath + 'CSV/'
        os.makedirs(dirPath, exist_ok=True)
        logger.info(f"Path CSV: {dirPath}")
    
        # Granvando o arquivo no diretório
        dirOut = dirPath + 'titanic-train.csv'
        logger.info(f"Arquivo CSV: {dirOut}")
        with open(dirOut, 'wb') as f:
            f.write(req.content)
            f.close()

        logger.info(f"Arquivo CSV gravado em: {dirOut}")

    else:
        dirOut = None
    
    return dirOut


@task
def existe_csv(fileCSV):
    # Logger
    logger = prefect.context.get("logger")

    check = os.path.exists(fileCSV)
    logger.info(f"Arquivo CSV [exists={check}]: {fileCSV}")

    return check


@task
def ler_csv(fileCSV):
    # Logger
    logger = prefect.context.get("logger")
    logger.info(f"Lendo arquivo CSV: {fileCSV}")

    # Carrega os dados do CSV em um Dataframe
    df = pd.read_csv(fileCSV)

    logger.info(f"Dataset com [{df.shape[0]}]linhas e [{df.shape[0]}]colunas.")

    return df


@task
def calcula_media_idade(df):
    # Calculo da Média
    return df.Age.mean()


@task
def exibe_media_calculada(m):
    # Logger 
    logger = prefect.context.get("logger")
    logger.info(f"A média de idade calculada é: {m}")


@task
def exibe_dataset(df):
    # Logger 
    logger = prefect.context.get("logger")
    logger.info(df)


@task
def termino():
    # Logger 
    logger = prefect.context.get("logger")
    logger.info("Finalização do fluxo sem processamento.")


# Definição do Fluxo (flow) e a sequencia das tasks
with Flow("flow-titanic") as flow:
    fcvs = download_csv(csvUrl, dirPath)
    existe_csv = existe_csv(fcvs)

    with case(existe_csv, True):
        df = ler_csv(fcvs)
        med = calcula_media_idade(df)
        exibe_media_calculada(df)
        exibe_dataset(df)

    with case(existe_csv, False):
        termino()


# Registro do flow em um projeto
flow.register(project_name="My Tests")

# executando o agent
flow.run_agent()
