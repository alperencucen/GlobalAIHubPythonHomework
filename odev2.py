list1 = []
firstname = str(input("Firstname:"))
lastname = str(input("lastname:"))
age = int(input("Age:"))
dateofbirth = int(input("Date of birth:"))

list1.append(firstname)
list1.append(lastname)
list1.append(age)
list1.append(dateofbirth)

for i in list1:
    print(i)

if (age < 18):
    print("You can't go out because it's too dangerous")
else:
    print("You can go out to the street")