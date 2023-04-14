def ASCII(x):
    print("ASCII value of entered character:", ord(x))


def character(x):
    print("Value of Given ASCII value:", chr(x))


x = input("Enter any character:")
ASCII(x)
y = int(input("Enter any ASCII value:"))
character(y)
