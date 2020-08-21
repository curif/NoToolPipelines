from git import Repo
import os

def pull(uri, name, dest):
  repoURI = os.path.join(uri, name)
  path = os.path.join(dest, name)
  #repo = Repo(repoURI)
  #print("Bare?" + repo.bare)
  if not os.path.exists(path):
    print("path:" + os.getcwd())
    print("Clone repo " + path)
    Repo.clone_from(repoURI, path)

  repo = Repo(path)
  if repo.bare:
    raise Exception("Error clonando repo")

  origin = repo.remotes.origin
  origin.pull()


