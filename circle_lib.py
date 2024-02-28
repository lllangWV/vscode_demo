
def process_circle_data(radius_input):
    # Validate input
    if not isinstance(radius_input, (int, float)) or radius_input <= 0:
        print("Error: The radius must be a positive number.")
        return

    # Calculate area
    area = get_area(radius_input)

    # Calculate circumference
    circumference = get_circ(radius_input)

    # Print results
    print(f"Circle with radius {radius_input}:")
    print(f"Area: {area}")
    print(f"Circumference: {circumference}")

def get_circ(radius_input):
    return 2 * 3.14159 * radius_input

def get_area(radius_input):
    return 3.14159 * radius_input ** 2