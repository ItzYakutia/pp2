import os 

pa = os.getcwd()

dir_only = [f for f in os.listdir() if os.path.isdir(f)]
files_and_dir = [f for f in os.listdir(pa)]
files_only = [f for f in os.listdir() if os.path.isfile(f)]

print(dir_only)
print(files_and_dir)
print(files_only)