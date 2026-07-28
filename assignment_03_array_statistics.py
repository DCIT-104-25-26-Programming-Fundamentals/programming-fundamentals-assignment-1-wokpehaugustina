# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================



numbers = [4,7,2,9,1]
n = int(input("How many numbers? "))
if n < 0:
    print("Error: Number of values must be greater 0.")
numbers = []
for i in range(n):
    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)

def calculateSum(numbers):
    total = 0

    for number in numbers:
        total += number
    return total

def calculateAverage(numbers):
    total = calculateSum(numbers)
    return total / len(numbers)

def findMax(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


def findMin(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest

print("\nResults:")
print("Sum:", calculateSum(numbers))
print("Average:", calculateAverage(numbers))
print("Maximum:", findMax(numbers))
print("Minimum:", findMin(numbers))





