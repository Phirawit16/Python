# Create Class
# Constructor
class Employee:
    
    def __init__(self,name,department,salary): # Constructor
        self.name = name
        self.department = department
        self.salary = salary
    
    def show_data(self):
        print("Employee data:")
        print("Name         : {}".format(self.name))
        print("Department   : {}".format(self.department))
        print("Salary       : {}".format(self.salary))

emp1 = Employee("Phirawit","Engineer",20000)
emp1.show_data()