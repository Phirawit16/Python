# Setter , Getter Method
class Employee():

    def __init__(self, name, department, salary):
        self.__name = name
        self.__department = department
        self.__salary = salary
    
    def setSalary(self,new_salary):
        self.__salary = new_salary

    def getSalary(self):
        return self.__salary
    
    def getName(self):
        return self.__name

    def getDepartment(self):
        return self.__department

    def _showData(self):
        print(f"""
        Name        :{self.getName()}
        Department  :{self.getDepartment()}
        Salary      :{self.getSalary()}""",)

emp1 = Employee("Phirawit","Engineer",20000)
emp2 = Employee("Kanokorn","Sales",30000)
emp1._showData()
emp2._showData()