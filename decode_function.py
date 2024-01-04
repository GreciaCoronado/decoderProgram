import math

# Read the content of the file
message_file = 'coding_qual_input.txt'
with open(message_file, 'r') as file:
    lines = file.readlines()

# Extract the numbers and words from each line
numbers = [(int(line.split()[0]), line.split()[1]) for line in lines]

# Sort the pyramid based on the numbers
numbers.sort()

# Retrieve the numbers corresponding to the sorted pyramid
decod_numbers = [num for num, _ in numbers]

# Retrieve the words corresponding to the sorted numbers
decod_words = [word for num, word in numbers]

s_value = len(decod_numbers) # Represents the total number of elements in the file

# Determine the number of rows needed in the pyramid to accommodate all the words
def calculate_k(s_value):    

    k = (-1 + math.sqrt(1 + 8 * s_value)) / 2
    
    # Check if k is a positive integer
    if k.is_integer() and k > 0:
        return int(k)  # If k is a positive integer, return its integer value
    else:
        return None    # If k is not a positive integer, return None

def pyramid():
    # Create the staircase pyramid structure
    decoded_staircase = ""
    
    y = 1
    result_k = calculate_k(s_value)
    for i in range(1, result_k + 1):
        for j in range (1, i+1):
            decoded_staircase += (str(y)+ " ")
            y += 1
        decoded_staircase  += "\n"  # Add a newline character to separate rows
    return decoded_staircase

def decoded_message():
    result_staircase = pyramid()
    # Split the pyramid string into lines
    pyramid_lines = result_staircase.strip().split("\n")

    # Extract the last numbers from each line and store in a list
    last_numbers = [line.split()[-1] for line in pyramid_lines]

    # Create a dictionary to map numbers to words
    number_word_map = dict(zip(decod_numbers, decod_words))

    # Retrieve the words corresponding to the last numbers
    decoded_words = [number_word_map[int(number)] for number in last_numbers]

    # Join the words into a string
    decoded_mess = ' '.join(decoded_words)
    return decoded_mess

# Example usage:
decode = decoded_message()
print(decode)
