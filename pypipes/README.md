# pipeline yaml sintaxis

    pipeline:
        stages:
            build:
                - maven:
                    package:
                        path: .
            release:
                - exec:
                    path: ./build.sh
            deploy:
                - kube:
                    path: pipelines/deploy.yaml
                     

## directivas

* pipeline: para indicar que es un pipeline
    * stages: para indicar los distintos estados (pueden tener cualquier nombre), cada estado es una lista de actividades
        * maven: actividad de maven
        * exec: ejecutar un programa o script
        * kube: aplicar un yaml de kubernetes
        * docker: instruccion docker (no implementado)
        * etc
        
#### Maven
indicar la directiva de mvn:

* package
* install
* compile
* validate
* etc
El contenido del documento son los parametros

#### exec
Ejecuta el script indicado en ̣'path'

#### kube
aplica el kubernetes file indicado en 'path'