#!/usr/bin/python3

#list of numbers
digits = ['zer1', 'one', 'two','three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['zer2', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eigteen', 'nineteen']
tens = ['zer3', 'ten', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds = "hundreds"
thousands = "thousands"

#retrieve a number from user
number = input("Insert your number: ")

#create a list where separate digits from retrieved number will be stored
l = []

#final list which will be printed 
inwords = []

#add single digits of which a provisioned number consists to a l list 
for i in number:
    l.append(int(i))

#define functions for various lenghts of numbers
def one():
    inwords.append(digits[l[-1]])

def two():
    if l[-2] == 1 and l[-1] != 0:
       inwords.append(teens[l[-1]])
    elif l[-2] == 0:
        pass
    elif l[-2] != 1 and l[-1] == 0:
        inwords.append(tens[l[-2]])
    elif l[-2] == 1 and l[-1] == 0:
        inwords.append(tens[l[-2]])
    elif l[-2] != 1 and l[-1] != 0:
        inwords.append(tens[l[-2]])
        inwords.append(digits[l[-1]])
    else:
        pass

def three():
    if l[-3] == 1 and l[-2] == 0 and l[-1] == 0: 
       print("one hundred", end="")
    elif l[-3] == 1 and l[-2] != 0:
        inwords.append("one hundred")
    elif l[-3] != 1 and l[-3] != 0:
        inwords.append(digits[l[-3]])
        inwords.append(hundreds)
    else: 
        pass

def four():
    if l[-4] == 1 and l[-3] == 0 and l[-2] == 0 and l[-1] == 0:
        print("one thousand", end="")
    elif l[-4] == 1:
        inwords.append("one thousand")
    elif l[-4] != 1:
        inwords.append(digits[l[-4]])
        inwords.append(thousands)
    else:
        pass

#conditional based on number length
if len(l) == 1:
    one()
elif len(l) == 2:
    two()
elif len(l) == 3:
    three()
    two()
elif len(l) == 4:
    four()
    three()
    two()
else:
    pass

print(' '.join(inwords))
