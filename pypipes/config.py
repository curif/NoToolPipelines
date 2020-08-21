from yaml import load, dump, FullLoader
import os

def get(path, name):
  with open(path, "r") as st:
    c = load(st, Loader=FullLoader)
  print(c)
  if not name in c["pipelines"]:
    raise Exception(name + " pipeline not in config")

  return c["pipelines"][name], c["parameters"]

def getPipeline(pipelineCfg, parameters):
  path = os.path.join(parameters["projectPath"], pipelineCfg["path"])
  with open(path, "r") as st:
    c = load(st, Loader=FullLoader)
  print(c)

  return c