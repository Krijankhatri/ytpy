# a program to find wether the number is odd or even
def is_it_odd(number):
    number = int(number)
    if number == 0:
        print("The number you provided is neither odd nor even.")
    else:
        if number%2 == 0:
            print("The number you provided is even.")
        else:
            print("The number you provided is odd.")

def main():
    try:
        user_input =(input("Enter a number: "))
        is_it_odd(user_input)

    except ValueError:
        print("Invalid input. Please enter a whole number.")   

if __name__ == "__main__":
    main()           