# -*- coding: utf-8

prompt = "\nTell me something, and I'll repeat it back to you:"
prompt += "\nEnter 'quit' to end to program. "

active = True
while (active):
    message = str(input(prompt))

    if (message == 'quit'):
        active = False
    else:
        print(message)