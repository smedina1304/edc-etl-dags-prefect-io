# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Prepare Prefect Cloud Backend
RUN prefect auth login --key <YOUR-KEY>

RUN MKDIR /app/dags

COPY ./ /app
COPY ./dags /app/dags

RUN chmod -R 755 /app

WORKDIR /app


# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# COMMANDS
CMD ["/bin/bash", "/app/script_startup.sh"]
