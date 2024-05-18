# a program to find the area of a triangle

# a function to find the area of the triangle 

def area_of_triangle(base, height):

    # rather than writing this -> area = 1/2*(base*height)

    return 0.5*base*height

def main():
    try:    
        base = float(input("Enter the base of the triangle in cm: "))
        height = float(input("Enter the height of the triangle in cm: "))

        if base <= 0 or height <= 0:
            print("The base and height must be positive numbers.")
            return
        
        answer = area_of_triangle(base,height)
        print(f"The area of the triangle is {answer:.2f} cm².")

    except ValueError:
        print("Invalid inputs. Please enter numeric values. ")

if __name__ == "__main__":
    
    main()
   