# a program to find wether the number is zero, positive or negative
def is_it_zero(number):
    number = float(number)
    if number == 0:
        print("The number you provided is zero")
    else:
        if number > 0:
            print("The number you provided is positive.")
        else:
            print("The number you provided is negative.")

def main():
    try:
        user_input =(input("Enter a number: "))
        is_it_zero(user_input)

    except ValueError:
        print("Invalid inputs. Please enter a numeric values.")   

if __name__ == "__main__":
    main()           