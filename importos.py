import os

path = "D:\laptop"

if os.path.exists(path):
    print("This locatioin exists...")
    if os.path.isfile(path):
        print('this is a file')
    elif os.path.isdir(path):
        print("This is a directory")
else :
    print("THis locationn doesn't exist")