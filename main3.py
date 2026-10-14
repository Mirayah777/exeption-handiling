valid = True
while valid:
    try:
        n = int(input("enter a number: "))
        while n % 2 == 0:
            print(" bye")
            n = int(input("enter a number: "))
        valid = False
    except ValueError:
        print("invalid")
        


