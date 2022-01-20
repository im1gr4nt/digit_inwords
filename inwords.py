#!/usr/bin/python3

digits = ['zero', 'one', 'two','tree', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['zero', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eigteen', 'nineteen']
number = input("Insert your number: ")
leest = []

for i in number:
    leest.append(int(i))


for i in leest:
    print(digits[i])
