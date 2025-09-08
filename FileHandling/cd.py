import os

# os.mkdir("my_folder")
# print("Directory created successfully!")

print("Contents of current directory:")
print(os.listdir("."))

os.rmdir("my_folder")
print("my_folder removed!")