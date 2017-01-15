# -*- coding:utf-8

prompt = "\nPlease enter the name of a cityyou have visited:"
prompt += "\n(Enter 'quit' when you're finished.)"

while True:
    city = str(input(prompt))

    if (city == 'quit'):
        break
    else:
        print("I'd love to go to " + city.title() + "!")