number = 0
while number != 9:
    number = number + 1
    print("the number is", number)

answer = "N"
while answer != "Y":
    print("are we there yet?")
    answer = input("Please respond Y or N")
print("Yay! We are tnere!")

username = ""
while not username:
    username = input("Please enter username: ")

import sys

answerOK = False
while answerOK == False:

    answer = input("Exit? y or n").upper()
    if answer == "y":
        answerOK = True

