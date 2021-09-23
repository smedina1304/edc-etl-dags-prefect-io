#!/bin/bash

echo "-> RUN IN DOCKER..."
echo "DAG_PATH: " $DAG_PATH
echo "DAG_NAME: " $DAG_NAME

echo "-> SETUP: TZ = UTC"
#export TZ=America/Sao_Paulo
export TZ=UTC

echo "-> Prefect Backend Cloud..."
prefect backend cloud

echo "-> Login..."
prefect auth login --key $PREFECT_AUTH_KEY

cd $DAG_PATH

echo "Iniciando DAG"
pwd
python3 $DAG_NAME

