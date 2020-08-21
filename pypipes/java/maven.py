# maven

import os

def package(path):
  actupath = os.getcwd()
  os.chdir(path)
  ret = os.system("mvn package")
  os.chdir(actupath)
  if ret != 0:
    raise Exception("Package maven error")


