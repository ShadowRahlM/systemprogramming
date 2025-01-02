#!/usr/bin/env python3


def score(dice):
    # Initialize the sum to store the total score
    sum = 0
    # Initialize a counter list to count occurrences of each die face (1 through 6)
    counter = [0, 0, 0, 0, 0, 0]
    # Points for three of a kind for each die face (1 through 6)
    points = [1000, 200, 300, 400, 500, 600]
    # Extra points for each additional die face beyond three of a kind
    extra = [100, 0, 0, 0, 50, 0]

    # Count occurrences of each die face
    for die in dice:
        counter[die - 1] += 1

    # Calculate the score based on the counts
    for i, count in enumerate(counter):
        # Add points for three of a kind if count is 3 or more
        sum += points[i] if count >= 3 else 0
        # Add extra points for any additional dice beyond three of a kind
        sum += extra[i] * (count % 3)

    # Return the total score
    return sum


# Example usage:
# print(score([1, 1, 1, 5, 1]))  # Should print 1150
# print(score([2, 3, 4, 6, 2]))  # Should print 0
# print(score([3, 4, 5, 3, 3]))  # Should print 350
# print(score([1, 5, 1, 2, 4]))  # Should print 250

allGuests = {
    "Alice": {"apples": 5, "pretzels": 12},
    "Bob": {"hamsandwiches": 3, "apples": 2},
    "Carol": {"cups": 3, "apple pies": 1},
}


def total_brought(guests, items):
    numbrought = 0
    for k, v in guests.items():
        numbrought += v.get(items, 0)
    return numbrought


print("Numbers of things being brought:")
print(f" - Apples,{total_brought(allGuests, 'apples')}")
print(f" - Cups,  {total_brought(allGuests, 'cups')}")
print(f" - Cakes,{total_brought(allGuests, 'cakes')}")
print(f" - Ham Sandwiches , {total_brought(allGuests, 'hamsandwiches')}")
print(f" - Apple Pies,{total_brought(allGuests, 'apple pies')}")
print(f" - pretzels,{total_brought(allGuests, 'pretzels')}")





import sys
import os
import re

def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
  return returned_errors
  
def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/Desktop/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()

    
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)