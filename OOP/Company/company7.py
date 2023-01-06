from Employee import Employee
from Engineer import Engineer
from Sales import Sales

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
