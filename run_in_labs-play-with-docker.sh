#!/bin/bash

echo "-> RUN IN: labs.play-with-docker.com..."

echo "-> SETUP: TZ = UTC"
#export TZ=America/Sao_Paulo
export TZ=UTC


echo "-> Install libs"
pip3 install numpy
pip3 install pandas
pip3 install requests

echo "-> Install Prefect Core"
pip3 install prefect

echo "-> Prefect Backend Cloud..."
prefect backend cloud

echo "-> Login..."
prefect auth login --key <YOUR-KEY>

cd ./dags/flow-titanic

echo "Iniciando DAG-PREFECT"
python3 titanic-analyse.py

