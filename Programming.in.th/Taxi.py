import math
r = int(input()) #รัศมี
d = math.pi * (r**2) #พื้นที่วงกลม พายคูณอาร์กำลัง2
D = 2*((1/2)*(2*r)*(r)) #พื้นที่taxicab = พื้นที่ สี่เหลี่ยมจตุรัสที่ใหญ่ที่สุด ในวงกลมรัศมี r
print("%.6f" %(d))
print("%.6f" %(D))