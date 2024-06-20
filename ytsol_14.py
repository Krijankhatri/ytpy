# a program to print the factrorial of a number
def fact(number : int):
    if number == 1 or number == 0:
        return 1
    elif (number > 1):
        return number * fact(number-1)

def main():
    try:
        user_input = int(input("Which no would you like to make factorial of? \n-> "))
        if user_input < 0:
            print("You can't have the factorial of negative number.")
        else:
            print(f"The factorial of the number {user_input} is {fact(user_input)}.")
    except ValueError:
        print("Please provide a integer.")
        
if __name__ == "__main__":
    main()   