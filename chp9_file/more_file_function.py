f = open ("chp9_file/file.txt")

'''lines = f.readlines()

print(lines ,type(lines))
f.close()
'''
# In while loop
line = f.readline()
while (line != ""):
    print(line)
    line = f.readline()

f.close()