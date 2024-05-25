# a program to find whether the year is leap year or not
def is_leap_year(year):
    if year%4 == 0 and year%400 == 0 :
        print(year," is a leap year.")
    elif year%4 == 0 and year%100 != 0 :    
        print(year," is a leap year.")
    else:    
        print(year," is not a leap year.")

def main():
    try:
        input_year = int(input("Enter the year: "))
        is_leap_year(input_year)
    
    except ValueError:
        print("Please provide integers only.")

if __name__ == '__main__':
    main()