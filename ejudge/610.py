with open('input.txt', 'w') as f:
    f.write(input() + "\n")
    f.write(input() + "\n")

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    numbers = list(map(int, f.readline().split()))

result = sum(map(bool, numbers))
print(result)