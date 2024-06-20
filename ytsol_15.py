# a program to print multiplication table
def multiplication_table(num):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")

def main():
    try:
        num = int(input("Which number's multiplication table do you want? \n-> "))
        print(f"The table of {num} is: ")
        multiplication_table(num)

    except ValueError:
        print("Please provide integer value.")

if __name__ == '__main__':
    main()