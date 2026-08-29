a = (9,2,5,"ritti",False,"shanvi",675)
print(a)
print(type(a))

# tuple methods
x = (1,3,"riti",5,1,False,9,6,"shanvi",4,2,)
print(x)
no = x.count(9)
print(no)
i = x.index("riti")
print(i)
#concatination
num1 = (1,2,3,4)
num2 = (5,6,7,8,9,10)
concatinated = num1 + num2
print(concatinated)
# repeated using '*'
repeat = num1*4
print(repeat)
# check the element using  'in'
print(5 in num1)
print(6 in num2)
# find length 
print(len(num2))
#slicing
mytuple =(1,4,3,2,5,6,7)
sliced = mytuple[2:5]
print(sliced)
# unpacking
tuple = (1,2,3,)
a, b, c = tuple
print(a,b,c)
