# a program to generate a random integer in range 0-100
import random

def generate_random_int():
    num = random.randint(0,100)
    return num

def main():
        random_num = generate_random_int()
        print(random_num)

        while True:
            user_input = input("Do you want to generate another? (Y/N): ").strip().lower()
            # .strip removes any blank space and .lower converts all uppercase to lowercase.

            if(user_input in ['n','no']):
                print("Exiting the program.")
                break

            elif(user_input in ['y','yes']):
                print(random_num)
                continue

            else:
                print("  Invalid input. Please enter 'Y' or 'N'.")
            
# writing this line is crucial because the main() function will only be executed only if condition is true
if __name__ == "__main__":
    main()