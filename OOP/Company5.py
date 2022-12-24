# __str__(Object)

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

    def setSalary(self,new_salary): # Set new salary
        self.__salary = new_salary

    def getName(self):  # Get employee name
        return self.__name

    def getSalary(self): # Get employee salary
        return self.__salary

    def getDepartment(self): # Get employee department
        return self.__department

    def _showData(self):
        print(f"""
        Employee_name   :{self.__name}
        Department      :{self.__department}
        Salary          :{self.__salary}""",)

    def _annual_income(self):
        return f"""
        Employee_name   :{self.__name}
        Position        :{self.__department}
        Annual Income   :{self.__salary * 12}"""

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
print(eng1._annual_income())
print(sale1._annual_income())
print(eng1.getName())