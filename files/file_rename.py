import os
path = "D:\\practice\\practice\\Python-mini-projects\\files"  
contents = os.listdir(path)
print(contents)
txt_files = [file for file in contents if file.endswith('.txt')]
print(txt_files)
num = 1
for f in txt_files:
    old_path = os.path.join(path, f)        
    new_name = "file_{}.txt".format(num)
    new_path = os.path.join(path, new_name)
    os.rename(old_path, new_path)
    print("Renamed {} to {}".format(f,new_name))
    num += 1