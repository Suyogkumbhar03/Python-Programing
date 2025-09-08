import os

with open("example.txt","w") as file:
    print(file.write("this is old file"))

os.rename("example.txt","new.txt")
print("file renamed successfully")