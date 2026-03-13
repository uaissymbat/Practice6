with open('input.txt', 'w') as f:
    n = input()
    f.write(n + "\n")
    
    numbers = input()
    f.write(numbers + "\n")

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    numbers = list(map(int, f.readline().split()))

result = sorted(set(numbers))
print(*result)