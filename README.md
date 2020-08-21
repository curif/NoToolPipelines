# No Tools pipelines

This Proof of Concept is an attemp to demostrate that it's possible to develop a DevOps **CI/CD process** without the existence of classic tools (like Jenkins (TM))

## Disclaimer

I don't encourage to really do it, it's just a POC.

Don't try to run it without analisys, you will need to understand a modify the code in order to run it.

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

* /javademo: simple service (java spring boot and maven) to build and deploy
* /pypipes: our python pipeline

## The pipeline

    mkdir work
    cd work
    git clone git@github.com:curif/NoToolPipelines.git
    cd work/javademo
    mvn package
    ./build.sh 
    kubectl apply -f pipelines/deploy.yaml 
    minikube service testpipe --url

Test:

    google-chrome <SERVICE IP>/sum?a=1&b=2
    
## Configuration files

Yo need to understand and modify these:

* pypipes/config.yaml (in pypipes) describe the pipelines
* javademo/pipelines/pipelines.yaml the pipeline

## Execute the pipeline

    python pypipes config.yaml javaProgram
