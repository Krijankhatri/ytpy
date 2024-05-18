# a progtam to swap variables

def swapper(x,y):
  
    return y,x

def main():
    try:

        x = input("Enter the value for x : ") 
        y = input("Enter the value for y : ")   
        x,y = swapper(x,y)
        print(f"Now, x = {x} and y = {y}")

    except ValueError:

        print("Please provide valid values.")

if __name__ == "__main__":
    main()    