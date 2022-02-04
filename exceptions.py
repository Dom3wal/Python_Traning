
try:
    numerator = int(input("Enter number to device: "))
    denominator = int(input("Enter a number to device by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You devided by 0")

except ValueError as e:
    print(e)
    print("Enter only numbers")
    
except Exception as e:
    print(e)
    print("Something else went wrong, sory")
else:
    print(result)
finally:
    print("This will alaways execute")