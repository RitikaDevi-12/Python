# greatest of three
a = 2
b = 7
c = 6

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

print(greatest(a,b,c))    

# convert celsius to fahrenheit
def f_to_c(f):
    c = 5*(f-32)/9
    return c
f = int(input("Enter the temp in f :"))
c = f_to_c
print(f"{round(c(f),2)} degree celsius")

#  prevent function to print new line
print("ritika")
print("bandral")
print("Ritika",end ="")
print("bandral", end ="")


# recursive function to print natural num
def sum(n):
    if(n==1):
        return 1
    else:
        return n + sum (n-1)
print(sum(10))

# pattern printing

def pattern(n):
    if(n==0):
         print("")
    else:
        print("*" * n)
        pattern(n-1)
pattern(6)

# convert inch_to_cm
def inch_to_cm(inch):
    return inch * 2.54
inch = int(input("Enter the inch :"))
print(inch_to_cm(inch))

# remove and strip
def remove(l,word):
    n =[]
    for item in l :
        if not(item == word):
            n.append(item.strip(word))
        return n
l = ["ritika", "bandral","ritti","chidiya","ka"]
print(remove(l,"ka"))

# multiply
def multiply(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")
multiply(3)        
