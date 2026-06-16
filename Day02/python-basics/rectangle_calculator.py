def calculate_area(length, width):

    area = length * width
    return area
if __name__ == "__main__":
    
    length = input("Enter the length of the rectangle: ")
    length = float(length)  # Convert the input to a float
    width = input("Enter the width of the rectangle: ")
    width = float(width)  # Convert the input to a float

    area = calculate_area(length, width)
    print(f"The area of the rectangle is: {area}")