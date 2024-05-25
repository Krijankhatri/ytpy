# a program to find largest number among three
def is_largest(a,b,c):
    if (a<b):
        if (c<b):
            print(b," is the largest number.")
        else:
            print(c," is the largest number.")
    else:
        print(a," is the largest number.")          

def main():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        c = float(input("Enter the third number: "))
        is_largest(a,b,c)
    except ValueError:
        print("Please provide numeric value only.")

if __name__ == '__main__':
    main()