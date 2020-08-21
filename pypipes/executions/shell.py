
import os

def run(path, script):
  actupath = os.getcwd()
  os.chdir(path)
  print("RUN: " + path + " --> " + script)
  ret = os.system(os.path.join("./", script))
  os.chdir(actupath)
  if ret != 0:
    raise Exception("exec error")
