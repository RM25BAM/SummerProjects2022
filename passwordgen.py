y = input('Hello, welcome to password generator.Please enter your name:')
print('Greeting, {name}!'.format(name = y))
import random
import string
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
def random_password():
        #user can decide the length of the password
        length = int(input("Enter password length: "))
        print("Password:")
        #use random to shuffle the characters
        random.shuffle(characters)

        ## picks random char in the list // uses for loop
        password = []
        for i in range(length):
            password.append(random.choice(characters))

        ## shuffling the resulting char
        random.shuffle(password)

        #from list to string
        ## printing the list
        print("".join(password))
## invoking the function
random_password()
print('Thank you {name} for trying the password generator. See you soon!'.format(name = y))

