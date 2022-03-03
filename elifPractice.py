print("Welcome")



def function1():
    print("Select a number")
    x = int(input())
    if x == 1:
        print("One")
    elif x == 2:
        print("Two")
    elif x == 3:
        print("Three")
    else:
            print("Sorry you lose")

function1()

def function2():
    print("Do you want to play again y/n?")
    i = input()
    while i == "y":
        function1()
        print("Do you still want to play? y/n")
        i = input()
    if i == "n":
        print("You're no fun")
    else:
        print("You don't know what you're doing")

function2()


print("Goodbye")
