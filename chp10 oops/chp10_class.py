class Employee:
    language = "py"
    salary = 2000000

'''Naman = Employee() 
print(Naman.language,Naman.salary)
'''
E1 = Employee()
E1.name ="Naman"
print(E1.name,E1.salary,E1.language)
'''Rohan = Employee()
print(Naman.salary)
print(Naman.language)'''
E2 = Employee()
E2.name = "Raj"
E2.language = "java"
print(E2.name ,E2.salary,E2.language)

# self attributes
class Employee:
 def getinfo(self):
    print(f"The language is {self.language}.The salary is {self.salary}")

 ''''def greet(self):
   print("Good morning")
       '''
 @staticmethod
 def greet():
    print("good morning")

harry = Employee()    
harry.language = "javascript"
harry.salary = 200000

harry.getinfo()
harry.greet()
# Employee.getinfo(harry)       