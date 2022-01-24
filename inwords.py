#!/usr/bin/python3

#list of numbers
digits = ['zer', 'one', 'two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['zer', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eigteen', 'nineteen']
tens = ['zer', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

#retrieve a number from user
number = input("Insert your number: ")

#create a list where separate digits from retrieved number will be stored
l = []
#add single digits of which a provisioned number consists to a l list 
for i in number:
    l.append(int(i))

#conditional based on number length
if len(l) == 1:
    print(digits[l[0]])
elif len(l) == 2:
    if l[0] == 1 and l[1]!=0:
       print(teens[l[1]])
    elif l[0]!=1 and l[1] == 0:
        print(tens[l[0]])
    elif l[0] == 1 and l[1] == 0:
        print(tens[1])
    elif l[0]!=1 and l[1]!=0:
        print(tens[l[0]], digits[l[1]])
    else:
        pass
else:
    pass
