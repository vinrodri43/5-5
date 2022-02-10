# user inputs a phone number with alphabetic characters
# uppercase every letter in the number
user=input('Enter a phone number with alphabetic characters in XXX-XXX-XXXX format: ').upper()
number=user.split('-')
# look through the number and translate characters to numbers using for loop and if statements
# for statement should omit the area code
for numbers in number:
    for i in numbers:
        if i in 'ABC':
            number[i]=2
        elif i in 'DEF':
            number[i]=3
        elif i in 'GHI':
            number[i]=4
        elif i in 'iKL':
            number[i]=5
        elif i in 'MNO':
            number[i]=6
        elif i in 'PQRS':
            number[i]=7
        elif i in 'TUV':
            number[i]=8
        elif i in 'WXYZ':
            number[i]=9
output='-'.join(number)
print(output)