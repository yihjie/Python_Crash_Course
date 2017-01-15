# -*- coding:utf-8

while True:
    age = int(input("PLease tell me how old are you, and I'll show you the ticket price: "))

    print("You are " + str(age) + " years old. ")
    if age > 12:
        print("The price is 15 USD.")
    elif age >= 3:
        print("The price is 10 USD.")
    else:
        print("The ticket is free for you.")