friends = ["apple" ,"banana" ,"orange" ,"pear" ,123,'a','b',"riti"]
print(friends[6])
friends[6] =["ritti"]
print(friends[6])
print(friends[2:7])
# Append
friends.append("bandral")
print(friends)
x = [1,2,3]
y = x
y.append(4)
print(x)
# sortingy = 
l1 = [1,4,2,3,6,7,5,9,10,8]
l1.sort()
print(l1)
# reversing
l1.reverse()
print(l1)
#insert
l1.insert(4,"ritika")
print(l1)
#pop ----> for deletion element at a index
x = [1,2,34,5,6,7,5,3,2]
x.pop(2)
print(x)
value = x.pop(4)
print(value)
# remove
num = [1,4,56,12,66,84,2,44]
num.remove(66)
print(num)