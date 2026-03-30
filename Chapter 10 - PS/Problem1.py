class Programmer: 
    company = "Microsoft"
    
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin 

p = Programmer("Saif", 10000, 2006 )
print(p.name, p.salary, p.pin, p.company)
k = Programmer("Kaif", 12000, 2005 )
print(k.name, k.salary, k.pin, k.company)

