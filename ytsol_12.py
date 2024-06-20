# a program to list all the prime number in range ()
def is_prime(n):
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False
    if n == 2:
        return True  # 2 is the only even prime number
    if n % 2 == 0:
        return False  # no other even number is prime
    
    max_divisor = int(n**0.5) + 1  # we only need to test up to the square root of n
    for d in range(3, max_divisor, 2):
        if n % d == 0:
            return False
    return True

def main():   
    numbers = []    
    for j in range(0,100):
        if is_prime(j) == True:
            numbers.append(j) 
    print(numbers)  

if __name__ == "__main__":
    main()      


