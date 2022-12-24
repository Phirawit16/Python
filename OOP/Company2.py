# Create Class
# Encapsulation
class Employee:

    def __init__(self,name,department,salary): # Constructor
        self.__name = name
        self.__department = department
        self.__salary = salary

    def company_name(self):
        print("Peter Industry")

    def _show_data(self):
        print("Employee data:")
        print("Name         : {}".format(self.__name))
        print("Department   : {}".format(self.__department))
        print("Salary       : {}".format(self.__salary))

emp1 = Employee("Phirawit","Engineer",25000)
emp2 = Employee("Kanokorn","Sales",30000)
emp1._show_data()
emp2._show_data()