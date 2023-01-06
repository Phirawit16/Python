from Employee import Employee

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