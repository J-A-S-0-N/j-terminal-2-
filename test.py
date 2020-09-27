import os 


os.chdir('C:\\Users\\jason\\Desktop')
dirpath = os.getcwd()
print(dirpath)
if os.path.exists("test.txt"):
    print("it works")
else:
    print("no file")