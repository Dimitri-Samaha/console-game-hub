#help(string) # on Python 3
#....
#DATA
    #ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    #ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #digits = '0123456789'
    #hexdigits = '0123456789abcdefABCDEF'
    #octdigits = '01234567'
    #printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
    #punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    #whitespace = ' \t\n\r\x0b\x0c'

import os
import string
import random as rand

lcl_list = list(string.ascii_lowercase)
ucl_list = list(string.ascii_uppercase)
dig_list = list(string.digits)
punc_list = list(string.punctuation)

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "p_file.txt")

def sign_in():

    def create_username():
        # loop variable
        username_valid = False
        while not username_valid:
            print("Your username should have minimum 4 charatcters.")
            username_input = input("User ID: ")
            if len(username_input) >= 4:
                username_valid = True
        return username_input


    def create_password():
        # loop variable
        password_valid = False
        # password needs
        print("Your password should contain minimum 1 lowercase 1 uppercase 1 digit and should have minimum 8 characters.")
        while password_valid == False:
            password_input = input("Create Password: ")


            # function for formulating errors
            def formulate_error(e):
                print(f"Your password should {e}. Please try a new one!")
                return

            #checking length
            if len(password_input) < 8:
                formulate_error("include minimum 8 characters")
            #checking content
            else:
                u = 0
                l = 0
                d = 0
                e = 0
                for c in password_input:
                    #checking for punc
                    if c in punc_list:
                        formulate_error("not contain punctuations")
                        e = 1
                        break
                    #checking for minimum 1 uppercase
                    elif c in ucl_list:
                        u = 1
                    #checking for minimum 1 lowercase
                    elif c in lcl_list:
                        l = 1
                    #checking for minimum 1 digit
                    elif c in dig_list:
                        d = 1
                # calling the formulating errors function
                if u == 0:
                    formulate_error("contain minimum 1 uppercase characters")
                    e = 1
                if l == 0:
                    formulate_error("contain minimum 1 lowercase letters")
                    e = 1
                if d == 0:
                    formulate_error("contain minimum 1 digit")
                    e = 1
                if e == 0:
                    password_valid = True
        return password_input


    new_username = create_username()
    new_password = create_password()
    with open(file, "a") as f:
        f.write(new_username + " " + new_password + "\n")
    return new_username

    
def log_in():
    user_check = False
    while not user_check:
        username_find = input("User ID: ")
        users_pass = ""
        # finding username and it's password
        with open(file, "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split(" ")
                if user == username_find:
                    users_pass = passw
                    print(users_pass)
                    user_check = True
                    break
            # if username isnt found so its a wrong username so write a new one
            if users_pass == "":
                print("No such user!")

    # checking if user is the real user by asking for password 
    password_input = ""
    while password_input != users_pass:
        password_input = input("Password: ")
        if password_input != passw:
            print("Wrong password!!")
    # Welcoming user
    print(f"Welcome {user}")
    return user


def log_sign_func():
    # log in or sign in??
    purpose_check = False
    while not purpose_check:
        purpose = input("Log in[L] or Sign in[S] or play as guest[G]: ")
        if purpose.lower() == "l":
            purpose_check = True
            user = log_in()
        elif purpose.lower() == "s":
            purpose_check = True
            user = sign_in()
        elif purpose.lower() == "g":
            purpose_check = True
            user = "Guest" + str(rand.randint(0, 10000000))
        else:
            print("I didn't understand your input. ")
    return user


if __name__ == "__main__":
    log_sign_func()
