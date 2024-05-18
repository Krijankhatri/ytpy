# a progtam to find the square root of a number

from math import sqrt

# writing a function with error handeling
def sqr_root(number):

    if number < 0:

        raise ValueError("Please provide positive number only")
    
    return sqrt(number)

# taking user input

def main():

    try:

        num1 = float(input("Enter the number number: "))

        answer = sqr_root(num1)

        print(f"The square root of {num1} is {answer}")

    except ValueError as e:

        print(f"Error: {e}")

if __name__ == "__main__":
    main()
