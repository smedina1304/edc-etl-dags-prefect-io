BUILD
docker build -f Dockerfile -t smedina1304/myprefectdags:v1.0 .

RUN
docker run -t -i -e PREFECT_AUTH_KEY='<KEY>' --rm --name prefect smedina1304/myprefectdags:v1.0

docker run -t -i -e PREFECT_AUTH_KEY='<KEY>' -e DAG_PATH='/app/dags/flow-test-hello' -e DAG_NAME='test-hello.py' --rm --name prefect -v data:/app/data smedina1304/myprefectdags:v1.3
docker run -d -e PREFECT_AUTH_KEY='<KEY>' -e DAG_PATH='/app/dags/flow-titanic' -e DAG_NAME='titanic-analyse.py' --rm --name prefect -v data:/app/data smedina1304/myprefectdags:v1.3

docker run -d -e PREFECT_AUTH_KEY=$PREFECT_KEY -e DAG_PATH='/app/dags/flow-titanic' -e DAG_NAME='titanic-analyse.py' --rm --name prefect -v data:/app/data smedina1304/myprefectdags:v1.3


PUBLISH
docker login -u smedina1304
password prompt: <token>

Se necessario mudar a tag para o repositório no Docker-hub
docker tag smedina1304/myprefectdags:v1.0 <ID_USER>/<ID_REPORITORIO>:[TAG]

docker push smedina1304/myprefectdags:v1.0 