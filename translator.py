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
hund_l = 'hundred'
hunds_l = 'hundreds'
thou_l = 'thousand'
thous_l = 'thousands'

def units():
    n = l[-1]
    unit = unit_l[n-1]
    inwords.append(unit)

def teens():
    n = l[-2]
    teen = teens_l[n-1]
    inwords.append(teen)

def tens():
    n = l[-2]
    ten = tens_l[n-1]
    inwords.append(ten)

def hundreds():
    if l[-3] == 1:
        inwords.append('one hundred')
    n = l[-3]
    hundred = hubd_l[n-1]
    inwords.append(ten)

if l[-2] == 1 and l[-1] != 0:
    teens()
else:
    tens()

units()

print(*inwords)

