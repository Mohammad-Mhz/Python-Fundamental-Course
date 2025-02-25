def passvalidation(password):
    
    if len(password) < 8:
        print("Your password must be at least 8 characters.")
    
    elif password.isnumeric():
        print("Your password must at least have one letter")

    elif password.isalpha():
        print("Your password must at least have one number")

    else:
        print('Your password is correct')


input_pass = '12345678as'
passvalidation(input_pass)



