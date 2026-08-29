name1 = "Abhimanyu"
nameshort = name1[0:9]
print(nameshort)
character1 = name1[0]
print(character1)
# Negative slicing
print(name1[-8:-1])
print(name1[1:5:3])
name2 = "ritika"
print(name2[1:4:2])
name3 = "abcdefghijklmnopqrstuvwxyz"
print(name3[1:25:2])
print(len(name3))
# to find length
name4 = "ritika"
print(len(name4))
# ends with
print(name4.endswith("ika"))
print(name4.endswith("xyz"))
# Starts with
name5 = "ritikabandral" 
print(name5.startswith("riti"))
print(name5.startswith("tika"))
# capitalize
print(name5.capitalize())
print(name4.capitalize())
# upper and lower case
print(name5.upper())
print(name5.lower())
# replace
text = "Ritikabandral"
text = text.replace("Ritikabandral" ,"ritikarajput")
print(text)