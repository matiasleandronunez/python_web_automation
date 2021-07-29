# python_automation
Integral boilerplate python automation project using behave and docker containers. Page object model, UI and API testing, parallel execution, multibrowser support 


Before Running:

After cloning the repository, create the secrets required by the sample app by executing the following commands that require you to init docker swarm first:

mkdir certs

openssl req -newkey rsa:4096 -nodes -sha256 -keyout certs/domain.key -x509 -days 365 -out certs/domain.crt

docker secret create revprox_cert certs/domain.crt

docker secret create revprox_key certs/domain.key

docker secret create postgres_password certs/domain.key

Make sure to copy the devscrets folder to the repository, or else edit the docker-compose file to correctly route the path.

