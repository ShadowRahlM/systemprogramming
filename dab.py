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
    sum += (points[i] if count >= 3 else 0)
    # Add extra points for any additional dice beyond three of a kind
    sum += extra[i] * (count % 3)

  # Return the total score
  return sum

# Example usage:
# print(score([1, 1, 1, 5, 1]))  # Should print 1150
# print(score([2, 3, 4, 6, 2]))  # Should print 0
# print(score([3, 4, 5, 3, 3]))  # Should print 350
# print(score([1, 5, 1, 2, 4]))  # Should print 250