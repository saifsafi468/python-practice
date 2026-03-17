class Employee:
    language = "Python" # This is a class attribute
    salary = 10000 # This is a class atrribute

saif = Employee()
saif.name = "Saif" # This is a object or instance attribute
print(saif.name, saif.language, saif.salary)

kaif = Employee()
kaif.name = "Kaif Ul Islam" # This is a object or instance attribute
print(kaif.name, kaif.language, kaif.salary)

# Here name is a object attribute and language and salary are class attributes as they directly belong to the class
