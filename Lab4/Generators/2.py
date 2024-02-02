n = int(input())
even_nums = (str(num) for num in range(2, n, 2))
print(", ".join(even_nums))