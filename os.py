import os

print(os.name)
cwd = os.getcwd()
print("Current working directory:", cwd)

def current_path():
    print('current working directory before')
    print(os.getcwd(), end="\n")
current_path()
os.chdir('../')
current_path()

file = "newbanana.txt"
paren_dir = "D:/parentdir/"
path = os.path.join(paren_dir, file)
with open(file, "w") as f:
    pass
print("directory '% s' created" % file)
# set read-write permissions for owner (0o600)
os.chmod(path, 0o600) 
os.remove(file) # delete empty files in directory

directory = "newDir"
parent_dir = "D:/Pycharm projects"
# mode (0o666), which grants read and write permissions 
mode = 0o666
path = os.path.join(parent_dir, directory)
os.makedirs(path)
print("Directory '% s' created" % directory)
print("Inf:", os.stat(directory))
os.rmdir(path) # delete empty paths

path = "/"
dir_list = os.listdir(path)
print("files and directories in '", path, "' :")
print(dir_list)