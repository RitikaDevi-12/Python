# problem 1
n = int(input("Enter a number : "))
for i in range(1,11):
    print(f"{n}X{i}= {n*i}")
# problem 2
l = ["herry","sonam","ritti","rashi","sourav"]
for name in l:
    if(name.startswith("s")):
        print(f"hello  {name}")

# problem 3 while loop
n = int(input("Enter a number : "))

i = 0
while(i<11):
    print(f"{n}X{i}= {n*i}")
    i += 1

# problem 4 prime no
n = int(input("Enter a number : "))
for  i in range(2,n):
    if(n%i) == 0:
        print("Number is not prime")
        break
else:
    print ("Number is prime")    


# problem 5 sum  
n = int (input("Enter a number : "))
i = 1
sum = 0
while(i<=n):
    sum += i
    i += 1
print(sum) 

#  problem 6 factorial
n = int (input("Enter the number :"))
product = 1
for i in range(1,5):
    product = product * i
print(product)    

# problem 7 print reversetable
n  =  int(input("Enter the number :"))
for i in range(1,11):
    print(f"{n}X{11-i} ={n}*{11-i}")


                