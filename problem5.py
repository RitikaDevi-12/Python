import os

# Directory whose contents you want to print
directory = "/"

contents = os.listdir(directory)

for item in contents:
    print(item)