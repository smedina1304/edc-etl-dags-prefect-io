#!/bin/bash

echo "-> RUN IN: labs.play-with-docker.com..."

echo "-> SETUP: TZ = UTC"
#export TZ=America/Sao_Paulo
export TZ=UTC


echo "-> Install Prefect Core"
pip install prefect

echo "-> Prefect Backend Cloud..."
prefect backend cloud

echo "-> Login..."
prefect auth login --key <YOUR-KEY>

cd ./dags/flow-titanic

echo "Iniciando DAG-PREFECT"
python3 titanic-analyse.py

