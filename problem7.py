heights = {'Child': [30, 40, 35, 45, 30], 'Teenage': [50, 60, 55, 65, 60], 'Adult': [85, 90, 92, 88, 82]}

average_heights = {age_group: sum(heights) / len(heights) for age_group, heights in heights.items()}

print(average_heights)
