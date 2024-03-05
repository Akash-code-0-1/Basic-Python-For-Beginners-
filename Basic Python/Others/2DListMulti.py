""" 
You are asked to take user input for a 2D List,  take row and column size also.
And make sure your code maintin those conditions....
1) print Enterd 2D list
2) make 2 list for even and odd numbers from the 2Dlist and Print them
3) Make a multiplication table between to first 2 list and print the multiplicatin table and product sum of table.

Sample Input:
Enter Row Size: 3
Enter Column Size: 3
Enter 3 elements for row 1:
1 2 3
Enter 3 elements for row 2:
2 3 4
Enter 3 elements for row 3:
3 4 5


Sample Output:
Entered 2D List: [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
Printing even Number List:  [2, 2, 4, 4]
Printing odd Number List:  [1, 3, 3, 3, 5]
Muliplication Table:
1 X 2 = 2
2 X 3 = 6
3 X 4 = 12
2 X 3 = 6
3 X 4 = 12
4 X 5 = 20

Sum of products: 58

"""

rows = int(input("Enter Row Size: "))
cols = int(input("Enter Column Size: "))

numbers = []

for i in range(rows):
    row = []
    print(f"Enter {cols} elements for row {i + 1}:")
    elements = input().split()
    for j in range(cols):
        element = int(elements[j])
        row.append(element)
    numbers.append(row)

print("Entered 2D List:",numbers)

evenLinst=[]
oddList=[]

for i in numbers:
    for element in i:
        if element%2==0:
            evenLinst.append(element)
        else:
             oddList.append(element)       
               
print("Printing even Number List: ",evenLinst)
print("Printing odd Number List: ",oddList)

sum_of_products = 0
print("Muliplication Table: ")
for i in range(len(numbers) - 1):  
    for j in range(len(numbers[i+1])):
        sum_of_products += numbers[i][j] * numbers[i+1][j]
        print(f"{numbers[i][j]} X {numbers[i+1][j]} = {numbers[i][j] * numbers[i+1][j]}")

print("\nSum of products:", sum_of_products)
