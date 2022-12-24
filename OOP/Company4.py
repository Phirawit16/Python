# Inheritance

class Employee(): # Super Class
    #Class Variable
    company_name = "Peter Indusrty"
    _minSalary = 15000
    _maxSalary = 50000

    def __init__(self, name, department, salary):
        #Instance Variable
        self.__name = name
        self.__department = department
        self.__salary = salary

    def _showData(self):
        print(f"""
        Name        :{self.__name}
        Department  :{self.__department}
        Salary      :{self.__salary}""",)

class Engineer(Employee): # Sub Class
    __department = "Engineer"
    def __init__(self, name, salary):
        super().__init__(name, self.__department, salary)
    pass

class Sales(Employee): # Sub Class
    __department = "Sales"
    def __init__(self, name, salary):
        super().__init__(name, self.__department, salary)
    pass

eng1 = Engineer("Phirawit",40000)
sale1 = Sales("Kanokorn",30000)
eng1._showData()
sale1._showData()