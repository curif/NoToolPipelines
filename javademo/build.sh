
# este eval apunta el cliente de docker al docker 
# dentro de minikube, permitiendo guardar la imagen
# en minikube. De esta manera evitamos la necesidad
# de utilizar una registry

eval $(minikube -p minikube docker-env)

docker build -t testpipe:latest .
docker images | grep testpipe
