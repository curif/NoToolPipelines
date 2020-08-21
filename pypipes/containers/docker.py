
import os

def build(path, script):
  actupath = os.getcwd()
  os.chdir(path)
  ret = os.system(os.path.join("./", script))
  os.chdir(actupath)
  if ret != 0:
    raise Exception("Docker build error")
