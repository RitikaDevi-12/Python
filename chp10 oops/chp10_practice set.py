from random import randint
# problem 1
class programmer :
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("Harry", 120000, 12312)
print(p.name,p.salary,p.pin)  
p = programmer("Niya", 130000, 22642)
print(p.name,p.salary,p.pin)        
p = programmer("Taniya", 120000, 82312)
print(p.name,p.salary,p.pin)        
p = programmer("Harash", 120000, 42312)
print(p.name,p.salary,p.pin)              


# problem 2 // calculato
class calculator:
    def __init__(self,n):
        self.n = n


    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
            print(f"The cube is {self.n*self.n*self.n}")
               
    def squareroot(self):
            print(f"The squareroot is {self.n**1/2}")        


a = calculator(4)   
a.square()
a.cube()
a.squareroot()


# problem 3
class Demo:
      a= 4

o = Demo()
print(o.a)
o.a = 0 
print(o.a)

# problem 4 // static method add

class calculator:
    def __init__(self,n):
        self.n = n


    def square(self):
        print(f"The square is {self.n*self.n}")

    def cube(self):
            print(f"The cube is {self.n*self.n*self.n}")
               
    def squareroot(self):
            print(f"The squareroot is {self.n**1/2}")   

    @staticmethod
    def hello():
          print("hello world")             


a = calculator(4) 
a.hello()
a.square()
a.cube()
a.squareroot()

# problem 5
class Train():

    def __init__(self,trainNo):
         self.trainNo = trainNo

    def book(self,fro,to):
     print(f"Ticket is booked in train no : {self.trainNo} from {fro} to {to}")

    def getstatus(self,):
         print(f"Train no : {self.trainNo} is running on time")

    def getfare(self,fro,to):
         print(f"Ticket fare in train no:{self.trainNo} from {fro} to {to} is {randint(101,2000)}")

    
t = Train(16232)
t.book("kathua" , "dehradun")
t.getstatus()
t.getfare("kathua","dehradun")