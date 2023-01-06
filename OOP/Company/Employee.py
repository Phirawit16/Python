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