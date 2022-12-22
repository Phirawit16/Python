test_1 = int(input())
test_2 = int(input())
test_3 = int(input())
total = test_1 + test_2 + test_3
if total >= 80:
    print("A")
elif total >= 75:
    print("B+")
elif total >= 70:
    print("B")
elif total >= 65:
    print("C+")
elif total >= 60:
    print("C")
elif total >= 55:
    print("D+")
elif total >= 50:
    print("D")
elif total <50:
    print("F")
else:
    pass