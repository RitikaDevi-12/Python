s = {2,32,6,1,"ritti",6,3,2,3,3,3,7,8}
print(s,type(s))
#add
s.add(54)
print(s,type(s))
#remove
s.remove(3)
print(s,type(s))
#length
print(s,len(s))
# clear
s.clear()
print(s,type(s))

# union
s1 = {1,2,3,4,5,6}
s2 ={4,5,6,7}
print(s1.union(s2))
#intersection
print(s1.intersection(s2))