# function
def avg():
    a = int(input("Enter the number :"))
    b = int(input("Enter the number :"))
    c = int(input("Enter the number :"))

    average = (a+b+c)/3
    print(average)

avg()
avg()
avg()
avg()
# function with arguments
def goodDay(name , ending):
    print("Good day, " +  name)
    print(ending)
    return"done"

goodDay("Ritika", "Thankyou")    
a = goodDay("chidiya" , "Thanks")    
print(a)

# Default case
def goodDay(name ,ending ="thanks"):
    print(f"Good day,{name}")
    print(ending)
    

goodDay("Ritti")    

