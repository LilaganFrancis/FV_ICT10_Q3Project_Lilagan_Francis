username = input("Enter Username: ")
password = input("Enter Password: ")

if len(username) < 7: #the len function returns the number of items in the object. In this case, len(username) < 7 makes sure that the characters that are entered are not less than 7 characters.
    print("Username must have at least 7 characters.")

elif len(password) < 10: #the len function returns the number of items in the object. In this case, len(password) < 10 makes sure that the characters that are entered are not less than 10 characters.
    print("Password must have at least 10 characters.")

elif not any(char.isalpha() for char in password):
    print("Password must have at least one letter.")

elif not any(char.isdigit() for char in password):
    print("Password must have at least one number.")

else:
    print("Account has been created!")