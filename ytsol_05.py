# program to convert kilometer to miles and viceversa
 
def km_to_miles(km):

    return km*0.621371

def miles_to_km(miles):

    return miles*1.609323

def main():

    try:
        userinp = int(input("Choose an option:\n1: Kilometer to miles \n2: Miles to kilometer \n"))
        if userinp == 1:
            num1 = float(input("Enter the kilometers: "))
            print(km_to_miles(num1)," km")
        elif userinp == 2:
            num1 = float(input("Enter the miles: "))
            print(miles_to_km(num1)," miles")
        else:
            raise KeyError (f"Invalid choice:{userinp}. Valide options are 1 or 2 ")
    except ValueError:
        print("Please provide valid values.")

if __name__ == "__main__":
    main()       

'''
# code improved by ChatGPT
def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles * 1.60934

class InvalidOptionError(Exception):
    pass

def main():
    try:
        userinp = input("Choose an option:\n1: Kilometer to miles \n2: Miles to kilometer \n")
        if userinp not in {'1', '2'}:
            raise InvalidOptionError(f"Invalid choice: {userinp}. Valid options are 1 or 2.")
        
        userinp = int(userinp)  # Convert to integer after validating

        if userinp == 1:
            num1 = float(input("Enter the kilometers: "))
            result = km_to_miles(num1)
            print(f"{num1} kilometers is equal to {result:.2f} miles.")
        elif userinp == 2:
            num1 = float(input("Enter the miles: "))
            result = miles_to_km(num1)
            print(f"{num1} miles is equal to {result:.2f} kilometers.")
    except ValueError:
        print("Please provide valid numerical values.")
    except InvalidOptionError as e:
        print(e)

if __name__ == "__main__":
    main()
'''