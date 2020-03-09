import git
from git import Repo


info = f"""
Hello I am Hibana, I am a bot created by Madrix.
Commands-
    !help : All the info
    !hello : Greets
    !roll <No.> : Guessing game 
    !roles : view all the roles 
    !gif <query> : gif in chat
"""


def check_role(arr):
    for i in range(len(arr)):
        if arr[i] == "Developer":
            return True
        else:
            return False


def read_lines(c, file):
    with open(file, "r") as f:
        lines = f.readlines()
        return lines[c].strip()


def num_lines(file):
  l = 0
  with open(file, "r") as f:
    for line in f:
      l+=1
    return l

def write_path(c, file):
    with open("folderpath.txt", "a+") as file_object:
      file_object.seek(0)
      data = file_object.read(100)
      if len(data) > 0 :
          file_object.write("\n")
      file_object.write(c)


def git_push(pth, commitMessage):  #path #commit message
    repo = Repo(pth)
    repo.git.add(update=True)
    print("added")
    repo.index.commit(commitMessage)
    print("commited")
    origin = repo.remote(name='origin')
    origin.push()
    print("pushed")