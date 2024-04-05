import glob
 
file_list = glob.glob("subdirs/**/*.py", recursive=True)
print(len(file_list))