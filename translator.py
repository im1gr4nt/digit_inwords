#!/usr/bin/python3




num = input("Enter number: ")
l = []

#get a list of integers in number
for i in str(num):
    l.append(int(i))


#lists with numbers
unit = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['ten', 'twenty', 'thirty', 'fourty', 'fivety', 'sixty', 'seventy', 'eighty', 'ninety']
hund = 'hundred'
hunds = 'hundreds'
thou = 'thousand'
thous = 'thousands'

#number of tens
if l[-2] == 1 and l[-1] == 1:
    tens = "eleven"
elif l[-2] == 1 and l[-1] == 2:
    tens = "twelve"
elif l[-2] == 1 and l[-1] == 3:
    tens = "thirteen"
elif l[-2] == 1 and l[-1] == 4:
    tens = "fourteen"
elif l[-2] == 1 and l[-1] == 5:
    tens = "fifteen"
elif l[-2] == 1 and l[-1] == 6:
    tens = "sixteen"
elif l[-2] == 1 and l[-1] == 7:
    tens = "seventeen"
elif l[-2] == 1 and l[-1] == 8:
    tens = "eighteen"
elif l[-2] == 1 and l[-1] == 9:
    tens = "nineteen"
elif l[-2] == 1 and l[-1] == 0:
    tens = "ten"
elif l[-2] == 2:
    tens = "twenty"
elif l[-2] == 3:
    tens = "thirty"
elif l[-2] == 4:
    tens = "fourty"
elif l[-2] == 5:
    tens = "fifty"
elif l[-2] == 6:
    tens = "sixty"
elif l[-2] == 7:
     tens = "seventy"
elif l[-2] == 8:
    tens = "eighty"
elif l[-2] == 9:
    tens = "ninety"

#unity digit

if l[-2] == 1:
    uni = ""
elif l[-1] == 1:
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

inwords = tens + " " + uni
print(inwords)
