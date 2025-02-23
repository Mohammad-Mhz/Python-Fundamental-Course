user = {
    "username": "matin007",
    "password": "123456"
}

status = True
while status:
    entered_username = input("Please enter your username: ")
    entered_pass = input("Please enter your password: ")

    if  (entered_username == user["username"]) and (entered_pass == user["password"]):
        print("you are loged in.")
        status = False

    else:
        print("the password or username is not correct.")

