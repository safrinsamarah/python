import helper

helper.greet("Safrin")
helper.bye("Samarah")

name = input("What is your name? -> ")
helper.greet(name)

from helper import bye
bye(name)