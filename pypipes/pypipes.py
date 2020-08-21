"""
curif 2020
"""
import os
import sys

import config
import scm.gittools
import java.maven
import containers.docker
import containers.kubectl
import executions.shell

#variables globales
pipeline = None
pipelineCfg = None
parameters = None

def triggers():
    def byGit():
        print("trigger: git...")
        return True
    return byGit()

def pull():
    print("GIT CHECKOUT")
    scm.gittools.pull(uri=pipelineCfg["scm"]["git"]["uri"],
                      name=pipelineCfg["scm"]["git"]["repo"],
                      dest=parameters["workPath"])
    return True

def stages():
    for stageName, stage in pipeline["stages"].items():
        print("----")
        print(stageName)
        print("----")
        for step in stage:
            for directiva, paramsDirectiva in step.items():
                if directiva == "maven":
                    java.maven.package(parameters["projectPath"])
                elif directiva == "exec":
                    executions.shell.run(path = parameters["projectPath"],
                                         script = paramsDirectiva["path"])
                elif directiva == "kube":
                    containers.kubectl.apply(path = parameters["projectPath"],
                                             kubefile = paramsDirectiva["path"])
    return

def main():
    global pipeline, pipelineCfg, parameters
    if len(sys.argv) < 3:
        raise Exception("config file argument error conig.yaml pipeline")

    c = config.get(sys.argv[1], sys.argv[2])
    pipelineCfg = c[0]
    parameters = c[1]
    parameters["projectPath"] = os.path.join(parameters["workPath"], pipelineCfg["scm"]["git"]["repo"])

    # pull del repo configurado en el pipeline solicitado
    pull()

    #lee el pipeline en el repo
    pipeline = config.getPipeline(pipelineCfg, parameters)
    pipeline = pipeline["pipeline"]

    #ejecuta el pipeline
    if triggers():
        stages()

if __name__ == '__main__':
    print("START---")
    main()
    print("END---")

