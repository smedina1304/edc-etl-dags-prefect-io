import pandas as pd
import requests
import prefect
import os
from prefect import task, Flow, case
from prefect.schedules import IntervalSchedule
from datetime import datetime, timedelta
from io import BytesIO

csvUrl = 'https://github.com/BigDataGal/Python-for-Data-Science/blob/master/titanic-train.csv'
dirPath = '/Users/sergiomedina/Downloads/'
retry_delay = timedelta(minutes=15)

@task
def download_csv():
    # Logger
    logger = prefect.context.get("logger")
    logger.info(f"Download CSV: {csvUrl}")

    # request get CSV
    req = requests.get(csvUrl, stream=True)
    if req.status_code == 200:

        # Verificando Diretorio Output
        if not dirPath.endswith('/'):
            dirOut = dirPath + '/'
    
        # Criando a pasta
        dirOut = dirPath + 'CSV/'
        os.makedirs(dirPath, exist_ok=True)
    
        # Granvando o arquivo no diretório
        dirOut = dirPath + 'titanic-train.csv'
        with open(dirOut, 'w') as f:
            f.write(req.content)
            f.close()

        logger.info(f"Arquivo CSV gravado em: {dirOut}")

    else:
        dirOut = None
    
    return (req.status_code==200), dirOut


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
    logger.info("Finalização do fluxo.")


# Definição do Fluxo (flow) e a sequencia das tasks
with Flow("flow-titanic") as flow:
    check_download, fcvs = download_csv()

    with case(check_download, True):
        df = ler_csv(fcvs)
        med = calcula_media_idade(df)
        exibe_media_calculada(df)
        exibe_dataset(df)


# Registro do flow em um projeto
flow.register(project_name="My Tests")

# executando o agent
flow.run_agent()
