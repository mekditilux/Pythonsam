#>90,"A",>80,"B",>70,"C",>60,"C",<=60,"F"

mark = int(input("pleas enter grade"))
if mark > 90:
   grade = "A"
elif mark > 80:
   grade = "B"
elif mark > 70:
   grade = "C"
elif mark > 60:
   grade = "D"
else:
   grade = "F"

print(grade)