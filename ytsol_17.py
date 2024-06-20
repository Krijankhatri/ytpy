# a program to check wether the number is armstrong or not

def check_armstrong(number):
    x = len(number)
    sum = 0
    for i in range(x):
        new_num = int(number[i])
        sum = sum + (new_num**x)
    if sum == int(number):
        print("Yes!, It's an armstrong number.")
    else:
        print("No!, It's not an armstrong number.")   

def main():
    try:
        user_input = input("Enter the number you want to check: ")
        check_armstrong(user_input)
    except ValueError:
        print("Please provide valid numeric value. ")

if __name__ == '__main__':
    main()           