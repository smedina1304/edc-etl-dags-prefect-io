BUILD
docker build -f Dockerfile -t smedina1304/myprefectdags:v1.0 .

RUN
docker run -t -i -e PREFECT_AUTH_KEY='<KEY>' --rm --name prefect smedina1304/myprefectdags:v1.0

docker run -t -i -e PREFECT_AUTH_KEY='<KEY>' -e DAG_PATH='/dags/flow-test-hello' -e DAG_NAME='test-hello.py' --rm --name prefect smedina1304/myprefectdags:v1.2


PUBLISH
docker login -u smedina1304
password prompt: <token>

Se necessario mudar a tag para o repositório no Docker-hub
docker tag smedina1304/myprefectdags:v1.0 <ID_USER>/<ID_REPORITORIO>:[TAG]

docker push smedina1304/myprefectdags:v1.0 