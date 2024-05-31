################################
# Github Repo link: https://github.com/Pelchukwangden/03230190_BIA101_CAP3
# Your Name: Pelden Wangchuk
# Your Section: B
# Your Student ID Number: 03230190
################################
# REFERENCES
# 1. Robotics Back-End. (2021, August 9). Python - Read Each Line From a File. YouTube. 
# https://www.youtube.com/watch?v=R549pu8-6_s. Accessed May 25, 2024.
################################
# SOLUTION
# Your Solution Score: The total sum from the given input file 190.txt is 491648
# ################################

# Read the input.txt file
def read_input(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()  # Read all lines from the file and store them in a list
    return lines

# Calculate the sum of the first and last digits for each line
def calculate_sum(lines):
    total_sum = 0
    for line in lines:
        line = line.strip()  # Remove leading/trailing whitespace from the line
        if line:  # Skip empty lines
            first_digit = None
            last_digit = None
            left = 0
            right = len(line) - 1
            
            while left <= right and first_digit is None:# Find the first digit from the start of the line
                if line[left].isdigit():
                    first_digit = int(line[left])  # Convert the character to an integer
                left += 1
            
            while right >= 0 and last_digit is None: # Find the last digit from the end of the line

                if line[right].isdigit():
                    last_digit = int(line[right])  # Convert the character to an integer
                right -= 1
            
            # If both first and last digits are found, add their two-digit number to the total sum
            if first_digit is not None and last_digit is not None:
                total_sum += first_digit * 10 + last_digit
    return total_sum

# Print the solution
def print_solution(file_name, total_sum):
    print(f"The total sum from the given input file {file_name} is {total_sum}")

# Main function
def main():
    file_name = "190.txt"  # Replace with your actual input file name
    lines = read_input(file_name)  # Read the input file and get the list of lines
    total_sum = calculate_sum(lines)  # Calculate the total sum of the first and last digits for each line
    print_solution(file_name, total_sum)  # Print the solution with the input file name and total sum

# Running the main function
if __name__ == "__main__":
    main()