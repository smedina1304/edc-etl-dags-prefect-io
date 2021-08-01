import pandas as pd
import requests
import prefect
import os
from prefect import task, Flow
from prefect.schedules import IntervalSchedule
from datetime import datetime, timedelta
from io import BytesIO

csvUrl = 'https://github.com/BigDataGal/Python-for-Data-Science/blob/master/titanic-train.csv'
dirPath = '/Users/sergiomedina/Downloads/'
retry_delay = timedelta(minutes=15)

@task
def downloadCSV():
    # Logger
    logger = prefect.context.get("logger")
    logger.info(f"Download CSV: {csvUrl}")

    # Download CSV
    filebytes = BytesIO(
        requests.get(csvUrl, stream=True).content
    )

    # Verificando Diretorio Output
    if not dirPath.endswith('/'):
        dirOut = dirPath + '/'
    
    # Criando a pasta
    dirOut = dirPath + 'CSV/'
    os.makedirs(dirPath, exist_ok=True)
    
    # Granvando o arquivo no diretório
    dirOut = dirPath + 'titanic-train.csv'
    with open(dirOut, 'w') as f:
        f.write(filebytes.getbuffer())
        f.close()
    
    filebytes.close()

    return dirOut


@task
def get_data(fileCSV):
    # Carrega os dados do CSV em um Dataframe
    df = pd.read_csv(fileCSV)
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


# Definição do Fluxo (flow) e a sequencia das tasks
with Flow("flow-titanic") as flow:
    fcvs = downloadCSV()
    df = get_data(fcvs)
    med = calcula_media_idade(df)
    exibe_media_calculada(df)
    exibe_dataset(df)


# Registro do flow em um projeto
flow.register(project_name="My Tests")

# executando o agent
flow.run_agent()
