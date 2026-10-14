try:
    num1 = int(input("enter the numerator"))
    num2 = int(input("enter the denominator"))
    result = num1/num2
    print("result is",result)
except ZeroDivisionError:
    print("division by 0 is ERROR")
except ValueError:
    print("please enter a vaild number")
except:
    print("wrong input")
else:
    print(" no exception")
finally:
    print("this will execute no matter what")
    
