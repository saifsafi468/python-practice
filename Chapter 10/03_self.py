class Employee:
    language = "Python" # This is a class attribute
    salary = 10000 # This is a class atrribute

    def getInfo(self):
        print(f"The langauge is {self.language}. The salary is {self.salary}. ")
    
    @staticmethod
    def greet(self):
        print("Good Morning!!")




saif = Employee()
#saif.language = "JavaScript" # This is a object or instance attribute

saif.greet()
#Employee.greet(saif)

saif.getInfo()
#Employee.getInfo(saif)
