# Definição da Imagem, para detalhes ver: https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Environment configuration
ENV PREFECT_AUTH_KEY $PREFECT_AUTH_KEY
ENV DAG_PATH $DAG_PATH
ENV DAG_NAME $DAG_NAME

# Install pip requirements
COPY requirements.txt .
RUN pip3 install --no-cache -r requirements.txt

# Copy script to execute dag
COPY run_in_docker.sh .
RUN chmod 755 run_in_docker.sh

# Define and copy workdir
WORKDIR /dags
COPY dags/ /dags

# Creates a non-root user with an explicit UID and adds permission to access the /dags folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /dags
USER appuser

# Execute Script
CMD ["/run_in_docker.sh"]
