def count_letters(input_string):
    capital_count = 0
    small_count = 0

    for char in input_string:
        if char.isupper():  # Checks if the character is uppercase
            capital_count += 1
        elif char.islower():  # Checks if the character is lowercase
            small_count += 1

    return capital_count, small_count


# Example usage
input_string = input("Enter a string: ")
capital, small = count_letters(input_string)

print(f"Number of capital letters: {capital}")
print(f"Number of small letters: {small}")
