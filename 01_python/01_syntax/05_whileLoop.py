username: str = "Advaith"
password: str = "22"
x = False
y = True

while x is not True:
    user = input("Username:")
    if user.lower() == username.lower():
        while y:
            pswd = input("Password:")
            if pswd == password:
                break
            else:
                print("Try Again")
        x = True
    else:
        print("Try Again")
