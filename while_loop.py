# Using while loop write a code that will first ask a user for a username and password.
# Then, it will check for the username and password validity, 
# if correct it will print you have access, if not it will ask the user to enter their password or username 5 times, 
# if username or password not correct after 5 times, we print account locked.


username_passwd = {
    "user_1" : "passwd_1",
    "user_2" : "passwd_2",
    "user_3" : "passwd_3",
}

n = 5
username = []
password = []

while n != 0:
    username = input("ENTER YOUR USER NAME HERE\n")
    password = input("ENTER YOUR PASSWORD HERE\n")
    n -= 1
    if username in username_passwd and username_passwd[username] == password:
        print("\n YOU HAVE ACCESS \n")
        break
    elif n > 0:
        print("Try again.")
    else:
        print("Account locked.")




