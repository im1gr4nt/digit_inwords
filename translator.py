#!/usr/bin/python3




num = input("Enter number: ")
l = []

for i in str(num):
    l.append(int(i))

#unity digit
if l[-1] == 1:
    print("one")
elif l[-1] == 2:
    print("two")
elif l[-1] == 3:
    print("three")
elif l[-1] == 4:
    print("four")
elif l[-1] == 5:
    print("five")
elif l[-1] == 6:
    print("six")
elif l[-1] == 7:
    print("seven")
elif l[-1] == 8:
    print("eight")
elif l[-1] == 9:
    print("nine")
else 
    print("zero")
print(l)
