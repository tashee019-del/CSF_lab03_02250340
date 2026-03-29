def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter n: "))

for i in range(1, n + 1):
    result = check_even_odd(i)
    print(f"{i} -> {result}")