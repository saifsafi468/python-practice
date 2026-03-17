class Employee:
    language = "Python" # This is a class attribute
    salary = 10000 # This is a class atrribute

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The langauge is {self.language}. The salary is {self.salary}. ")
    
    @staticmethod
    def greet(self):
        print("Good Morning!!")




saif = Employee("Kaif", 12000, "Javascript")
#
# saif.name = "Saif"

print(saif.name, saif.salary, saif.language)