"""
lab_1a.py
This is to simulate a change made on a robot: robot_speed = 5 # m/s
The first lab in the BWSI CSS course. To complete this lab, fill out the variable on line 10
with your name. Then, save the code, add it to the staging area, and commit it to the Git tree.
"""
def request_santized_number(prompt: str) -> float:
    """
    Function to request and sanitize user input for the operatio
    
    Returns:
        float: The sanitized numeric input by the user.
    """
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def main():
    print("Hello World!")

    name = "Brayden Yuan" # TODO: Insert your name between the double quotes

    print(f"{name}, Welcome to the CSS course!")
    print(f"Hello, my name is {name}.")

if __name__ == "__main__":
    main()
