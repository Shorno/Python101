start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))

square = {x: x**2 for x in range(start, end) if x % 2 == 0}
print(square)