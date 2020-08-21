# No Tools pipelines

This Proof of Concept is an attemp to demostrate that it's possible to develop a DevOps **CI/CD process** without the existence of classic tools (like Jenkins (TM))

I don't encourage to really do it, it's just a POC.

## Ingredients
* Java
  * Maven
  * Spring boot
* Python
* BASH
* Docker
* GIT
* Kubernetes (minikube)

## sources

/javademo: simple service (java spring boot and maven) to build and deploy
/pypipes: our python pipeline

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

    google-chrome <SERVICE IP>/sum?a=1&b=2
