s = raw_input()
alpha = False
alphanum = False
digits = False
lowercase = False
uppercase = False
for letter in s:
    if letter.isalnum():
        alphanum = True
    if letter.isalpha():
        alpha = True
    if letter.isdigit():
        digits = True
    if letter.islower():
        lowercase = True
    if letter.isupper():
        uppercase = True
print alphanum       
print alpha
print digits
print lowercase
print uppercase
