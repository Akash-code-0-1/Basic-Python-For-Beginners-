heights = {'child': [30, 40, 35, 45, 30], 'teenage': [23, 34, 45, 56, 67]}

average_heights = {}

for age_group, height_list in heights.items():
    average_height = sum(height_list) / len(height_list)
    average_heights[age_group] = average_height

print(average_heights)
