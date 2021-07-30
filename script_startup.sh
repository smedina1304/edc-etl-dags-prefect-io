#!/bin/bash

#RUN IN: labs.play-with-docker.com
#pip install prefect
#export TZ=America/Sao_Paulo

echo "Prefect Backend Cloud..."
prefect backend cloud

echo "Login..."
prefect auth login --key <YOUR-KEY>

cd /app/dags/flow-test-hello

echo "Iniciando DAG-PREFECT"
python test-hello.py

