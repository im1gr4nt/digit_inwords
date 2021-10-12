#!/usr/bin/python3




num = input("Enter number: ")
l = []

#get a list of integers in number
for i in str(num):
    l.append(int(i))

#number of tens

    if l[-2] == 1 and l[-1]:
        tens = "one"
    elif l[-2] == 2:
        tens = "two"
    elif l[-2] == 3:
        tens = "three"
    elif l[-2] == 4:
        tens = "four"
    elif l[-2] == 5:
        tens = "five"
    elif l[-2] == 6:
        tens = "six"
    elif l[-2] == 7:
         tens = "seven"
    elif l[-2] == 8:
        tens = "eight"
    elif l[-2] == 9:
        tens = "nine"
    else: 
        tens = "zero"


#unity digit
    if l[-1] == 1:
        uni = "one"
    elif l[-1] == 2:
        uni = "two"
    elif l[-1] == 3:
        uni = "three"
    elif l[-1] == 4:
        uni = "four"
    elif l[-1] == 5:
        uni = "five"
    elif l[-1] == 6:
        uni = "six"
    elif l[-1] == 7:
         uni = "seven"
    elif l[-1] == 8:
        uni = "eight"
    elif l[-1] == 9:
        uni = "nine"
    else: 
        uni = "zero"
    print(uni)

inwords = tens + " " + uni
