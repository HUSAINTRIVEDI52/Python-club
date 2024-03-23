try:
    nuemrator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))

    result= nuemrator/denominator 

except ZeroDivisionError as e:
    print(e)
    print("Any number is not divisible by zero")
except ValueError as e:
    print(e)
    print("Enter only numbers")
except Exception as e:
    print(e)
    print("Something went wrong")
else:
    print(result)
finally:
    print("This will always execute")