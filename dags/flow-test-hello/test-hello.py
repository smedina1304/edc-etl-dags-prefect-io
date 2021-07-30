import prefect
from prefect import task, Flow

# Tasks do fluxo
@task
def say_hello():
    logger = prefect.context.get("logger")
    logger.info("Test Hello, Cloud!")

# Definição do Fluxo (flow) e a sequencia das tasks
with Flow("flow-test-hello") as flow:
    say_hello()

# Registro do flow em um projeto
flow.register(project_name="My Tests")

# executando o agent
flow.run_agent()
