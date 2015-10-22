_author_ = 'tcato'

print("Hello World")

reply = -1
while reply != 0:
    try:
        reply = int(input("Enter a positive integer, zero when done: "))
        if reply < 0:
            print("That integer is not positive")
        elif reply == 0:
            print("Exiting")
        else:
            print("Your input is doubled is", reply*2)
    except:
        print("You did not enter an integer")
