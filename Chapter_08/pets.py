# -*- coding: utf-8
def describe_pet(animal_type, pet_name):
    """顯示寵物的資訊"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')