# No Tools pipelines

This Proof of Concept is an attemp to demostrate that it's possible to develop a DevOps **CI/CD process** without the existence of classic tools (like Jenkins (TM))

I don't encourage to do it, it's just a POC.

## Ingredients
* Java
  * Maven
  * Spring boot
* Python
* BASH
* Docker
* GIT
* Kubernetes (minikube)

## The pipeline

    mkdir work
    cd work
    git clone /home/fabio.curi/repos/testpipe/
    cd work/testpipe
    mvn package
    ./build.sh 
    kubectl apply -f pipelines/deploy.yaml 
    minikube service testpipe --url

Test:

    google-chrome http://172.17.0.3:31633/sum?a=1&b=2
