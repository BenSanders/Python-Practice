# Define your function here
# Get the input in the program
# Manipulate the input so it is in the setup/data structure to solve the problem
# Process the manipulated input to reach solution data
# Output results

def feet_to_steps(feet):
    steps = feet / 2.5
    return int(steps)

if __name__ == '__main__':
    # Type your code here.
    feet_walked = float(input())
    print(feet_to_steps(feet_walked))
    #print(feet_to_steps)