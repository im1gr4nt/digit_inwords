#!/usr/bin/python3




num = input("Enter number: ")
#list made of input digits
l = []
#list made of strings - number inwords - printed finally
inwords = []

#get a list of integers in number
for i in str(num):
    l.append(int(i))


#lists with numbers in words
unit_l = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
teens_l = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens_l = ['ten', 'twenty', 'thirty', 'fourty', 'fivety', 'sixty', 'seventy', 'eighty', 'ninety']
hunds = ' hundreds'
thous = ' thousands'

def units():
    n = l[-1]
    unit = unit_l[n-1]
    inwords.append(unit)

def tens():
    if l[-2] == 1 and l[-1] == 0:
        n = l[-2]
        teen = teens_l[n-1]
        inwords.append(teen)
    else:
        n = l[-2]
        ten = tens_l[n-1]
        inwords.append(ten)

def hundreds():
    if l[-3] == 1:
        inwords.append('one hundred')
    else:
        n = l[-3]
        unit = unit_l[n-1]
        inwords.append(unit + hunds)

def thousands():
    if l[-4] == 1:
        inwords.append('one thousand')
    else:
        n = l[-4]
        unit = unit_l[n-1]
        inwords.append(unit + thous)

if len(l) == 4:
    thousands()
    hundreds()
    tens()
    units()
elif len(l) == 3:
    hundreds()
    tens()
    units()
elif len(l) == 2:
    tens()
    units()
elif len(l) == 1:
    units()
print(*inwords)

