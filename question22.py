nums = list(range(1, 31))
mult3 = [n for n in nums if n % 3 == 0]
mult5 = [n for n in nums if n % 5 == 0]
both = [n for n in nums if n % 15 == 0]
print(mult3, mult5, both)
