#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print("Hello, " + name + "!")

def greet_with_default(name="programmer"):
    print("Hello, " + name + "!")

def add(num1, num2):
    return num1 + num2

def halve(number):
    if not type(number) is int and not type(number) is float:
        return None
    
    return number/2
