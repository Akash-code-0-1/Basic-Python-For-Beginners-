""" 
Write a Python program using nested for loops to print various patterns, such as a right-angled triangle, an inverted right-angled triangle, and so on
"""

def print_pattern(rows, symbol="*"):

  # Right-angled triangle
  print("Right-angled triangle:")
  for i in range(1, rows + 1):
    for j in range(i):
      print(symbol, end="")
    print()  

  # Inverted right-angled triangle
  print("\nInverted right-angled triangle:")
  for i in range(rows, 0, -1):
    for j in range(i):
      print(symbol, end="")
    print() 

  # Pyramid
  print("\nPyramid:")
  midpoint = rows // 2 + 1  
  for i in range(1, rows + 1):
    for j in range(midpoint - i):
      print(" ", end="")
    for j in range(2 * i - 1):
      print(symbol, end="")
    print()  

# Example usage
rows = 5
print_pattern(rows)
