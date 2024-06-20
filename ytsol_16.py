# a program to print the fibonacci series with user desired length
def get_fibonacci(steps):
    steps = steps - 2
    fibonacci_series = [0,1]
    for i in range(steps):
        sum=fibonacci_series[0+i]+fibonacci_series[1+i]
        fibonacci_series.append(sum)

    for i in range(len(fibonacci_series)):   
        print(fibonacci_series[i],end =' ')
        '''for anyone who is reading I couldn't find how to get rid of the comma in the end so I
        made the code sorry I overcomplicate it. '''
        while i<(len(fibonacci_series)-1):
            print(',', end=' ')
            break

def main():
    try:
        user_input = int(input("Enter the length of fibonacci series you want:  "))
        get_fibonacci(user_input)
    except ValueError:
        print("Please provide valid numeric value. ")

if __name__ == '__main__':
    main()