from Employee import Employee

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