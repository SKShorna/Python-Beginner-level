# important

# 3*3
# list = [[1, 2, 3]
#         [4, 5, 6]
#         [7, 8, 9]]

# Method-01
# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(f"{list1[0]}\n{list1[1]}\n{list1[2]}")
# print("Before number putting:")
# print(list1[2][1])
# number = int(input("Enter the number you want to place:"))
# print("After number putting:")
#
# list1[2][1] = number
# print(number)
# print(f"{list1[0]}\n{list1[1]}\n{list1[2]}")

# Method-02-with smily
#
# row1 = ['🧐', '🧐', '🧐']
# row2 = ['🧐', '🧐', '🧐']
# row3 = ['🧐', '🧐', '🧐']
#
# matrix = [row1, row2, row3]
#
# print(f"{row1}\n{row2}\n{row3}")
#
# position = input("Enter the position you want to hide money:") # 32 row--> 3 and column--> 2
#
# row_number = int(position[0])
# column_number = int(position[1])
# row_selected = matrix[row_number-1]
# row_selected[column_number-1] = 'X'
# print(f"{row1}\n{row2}\n{row3}")


row1 = ['🧐', '🧐', '🧐']
row2 = ['🧐', '🧐', '🧐']
row3 = ['🧐', '🧐', '🧐']

print(f"{row1}\n{row2}\n{row3}")

position = input("Enter the position:")

row_num = int(position[0])
col_num = int(position[1])
matrix = [row1, row2, row3]
# print(matrix)
# row_selected = matrix[row_num-1]
matrix[row_num-1][col_num-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")


