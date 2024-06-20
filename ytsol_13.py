# a program to convert fahrenheit to celsius
def Celsius_to_fahrenheit(Celsius):
     return (Celsius*(9/5))+32
def Fahrenheit_to_celsius(fahrenheit):
     return (fahrenheit-32)*(5/9)
class InvalidOptionError(Exception):
    pass


def main():
    try:
        user_input = input("Choose a option.\n1. Celsius to fahrenheit\n2.fahrenheit to Celsius\n")
        if user_input not in {'1','2'}:
            raise InvalidOptionError(f"Invalid Choice: Valid options are 1 or 2")
        user_input = int(user_input)
        if user_input == 1:
            Celsius = float(input("Enter the celsius: "))
            fahrenheit = Celsius_to_fahrenheit(Celsius)
            print(f"{Celsius} degree celsius is equal to {fahrenheit:.2f} F.")
        elif user_input == 2:
            fahrenheit = float(input("Enter the fahrenheit: "))
            Celsius = Fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} F is equal to {Celsius:.2f} degree celsius.")
    except ValueError:
        print("Please provide valid numerical values.")
    except InvalidOptionError as e:
        print(e)            

if __name__ == "__main__":
    main()        