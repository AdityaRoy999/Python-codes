#exception = events detected during execution that interrupt the flow of the program 
#they are always within the try and except block except exceptiontype
try:
    numerator = int(input("enter a number:"))
    denominator = int(input("enter a number:"))
    number = numerator / denominator 
    print(number)
#except ValueError:   # personal error exception 
    #print("only enter a number not a string")
#except ZeroDivisionError:
    #print("You can't divide by zero idiot")
#except Exception:   # it is universal exception 
    #print("something went wrong :(")
except Exception as e:
    print(e)
    print("there is somthing wrong in this program pls check or run the program again")
else:
    print(number)
finally:
    print("this will always execute")