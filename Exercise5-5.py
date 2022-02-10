# user inputs a phone number with alphabetic characters
# uppercase every letter in the user
user=input('Enter a phone number with alphabetic characters in XXX-XXX-XXXX format: ').upper()
list(user)
# look through user and translate characters to numbers using for loop and if statements
# for statement should omit the area code
for letter in user:
    if letter in 'ABC':
        user.replace(letter,'2')
    elif letter in 'DEF':
        user.replace(letter,'3')
    elif letter in 'GHI':
        user.replace(letter,'4')
    elif letter in 'IKL':
        user.replace(letter,'5')
    elif letter in 'MNO':
        user.replace(letter,'6')
    elif letter in 'PQRS':
        user.replace(letter,'7')
    elif letter in 'TUV':
        user.replace(letter,'8')
    elif letter in 'WXYZ':
        user.replace(letter,'9')
print(user)