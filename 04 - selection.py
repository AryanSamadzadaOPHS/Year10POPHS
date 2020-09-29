#Selection

#Selection uses if/elif and else
#things people get wrong are:
#1. Forgetting the colon
#2. Forgetting indentation
#3. Not understanding comparison operators ==

skycolour = "blue"

if skycolour == ("blue"):
    print("The sky is blue today")

print("Good bye!")

baby = input("Has the baby been born yet? y or n?")

if baby == ("y"):
    print("congratulations")
else:
    print("Call us when you have news")

food = "kebab"

if food == "kebab":
    print("Ummm, my favourite!")
    print("I feel like saying it 100 times...")
    print(100 *(food + "! "))
else:
    print("I'm hungry")

