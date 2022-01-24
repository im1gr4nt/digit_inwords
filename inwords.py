#!/usr/bin/python3

#list of numbers
digits = ['zero', 'one', 'two','tree', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['zero', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eigteen', 'nineteen']
tens = ['zero', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

#retrieve a number from user
number = input("Insert your number: ")

#create a list where separate digits from retrieved number will be stored
leest = []
#add single digits of which a provisioned number consists to a leest list 
for i in number:
    leest.append(int(i))

#conditional based on number length
if len(leest) == 1:
    for i in leest:
        print(digits[i])
elif len(leest) == 2:


