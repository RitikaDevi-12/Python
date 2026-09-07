
class Employee:

    def __init__(self, name, language, salary):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")


harry = Employee("harry", "javascript", 200000)
print(harry.name, harry.salary, harry.language)

rohan = Employee("rohan","python",3000)
print(rohan.name,rohan.salary,rohan.language)


harry.getinfo()