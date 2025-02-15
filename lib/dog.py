#!/usr/bin/env python3

class Dog:
    #a method that takes in an argument of the dogs name
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

fido = Dog("Poseidon")
print(fido.name)
print(fido.breed)