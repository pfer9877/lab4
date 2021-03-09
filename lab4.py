

import re
p= input("Enter your password")
t = True
while t:
    if (len(p)<7):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[!@#$%^&*]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("The password is secure.")
        x=False
        break

if t:
    print("Password is not secure, please try again.")
