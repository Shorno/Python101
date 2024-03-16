import random

random_nums = [random.randint(0,100) for x in range(50)]

unique_nums = list(set(random_nums))

duplicates = []
for num in random_nums:
    print(num,end=" ")
    if num in unique_nums:
        unique_nums.remove(num)
    else:
        duplicates.append(num)

print("\nDuplicate numbers are:", duplicates)


