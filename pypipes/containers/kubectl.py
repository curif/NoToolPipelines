
import os

def apply(path, kubefile):
  actupath = os.getcwd()
  os.chdir(path)
  ret = os.system("kubectl apply -f '" + kubefile + "' ")
  os.chdir(actupath)
  if ret != 0:
    raise Exception("Kubectl apply error")
