#!/bin/bash

echo "RUN IN: labs.play-with-docker.com..."

echo "SETUP: TZ"
export TZ=America/Sao_Paulo


echo "Install Prefect Core"
pip install prefect

echo "Prefect Backend Cloud..."
prefect backend cloud

echo "Login..."
prefect auth login --key <YOUR-KEY>

cd ./dags/flow-test-hello

echo "Iniciando DAG-PREFECT"
python3 test-hello.py

