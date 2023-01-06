# Overload method
# Overiding Method

class Employee(): # Super Class
    #Class Variable
    company_name = "Peter Indusrty"
    min_Salary = 15000
    max_Salary = 50000

    def __init__(self, name, department, salary):
        #Instance Variable
        self.__name = name
        self.__department = department
        self.__salary = salary

    def set_bonus(self,bonus = 0 ):
        self.__bonus = bonus * self.__salary

    def setSalary(self,new_salary): # Set new salary
        self.__salary = new_salary

    def getName(self):  # Get employee name
        return self.__name

    def getSalary(self): # Get employee salary
        return self.__salary

    def getDepartment(self): # Get employee department
        return self.__department

    def _showData(self):
        print("")
        print(f"Employee_name   :{self.__name}")
        print(f"Department      :{self.__department}")
        print(f"Salary          :{self.__salary}")
        
    def _annual_income(self):
        return f"Annual Income   :{self.__salary * 12}"
    
    def _bonus(self):
        print(f"Bonus           :{self.__bonus}")


class Engineer(Employee): # Sub Class
    __department = "Engineer"
    def __init__(self, name, salary, age, experience, skill): #Constuctor
        super().__init__(name, self.__department, salary)
        self.__age = age #Overload Method
        self._exp = experience #Overload Method
        self._skill = skill #Overload Method
    
    def _showData(self): #Overriding Method
        super()._showData()
        print(f"Age             :{self.__age}")
        print(f"Experience      :{self._exp} year")
        print(f"Skill           :{self._skill}")

    def _bonus(self):
        super()._bonus()

class Sales(Employee): # Sub Class
    __department = "Sales"
    def __init__(self, name, salary, age, experience): #Constuctor
        super().__init__(name, self.__department, salary)
        self.__age = age #Overload Method
        self._exp = experience #Overload Method
    
    def _showData(self): #Overriding Method
        super()._showData()
        print(f"Age             :{self.__age}")
        print(f"Experience      :{self._exp} year")

    def _bonus(self):
        super()._bonus()

eng1 = Engineer("Phirawit",40000,23,2,"Game Developer")
eng1.set_bonus(2)

eng1._showData()
print(eng1._annual_income())
eng1._bonus()

sale1 = Sales("Kanokorn",30000,23,2)
sale1.set_bonus(3)

sale1._showData()
print(sale1._annual_income())
sale1._bonus()
