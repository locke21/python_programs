# --- Second Assignment Coursera; Day 3 --- #
# --- Objective: Ask user for input and determine highest/lowest --- #

largest, smallest = None, None
while True:
    entered_input = input('Enter whole number (type "done" if finished with inputs): ').lower()
    if entered_input == 'done':
        break
    try:
        number = int(entered_input)
    except ValueError:
        print('Invalid input')
        continue
    if largest is None or largest < number:
        largest = number
    if smallest is None or smallest > number:
        smallest = number

print(f"Maximum entered is: {largest}, Minimum entered is: {smallest}. ")


# --- Same program rewritten 3 months laters --- #

numbers = []
while True:
    entered_numbers = input('Enter whole number (type "done" if finished with inputs): ').lower()
    try:
        numbers.append(int(entered_numbers))
    except ValueError:
        print('Invalid input')
    if entered_numbers == 'done':
        break

print(f"Maximum entered is: {max(numbers)}, Minimum entered is: {min(numbers)}. ")
