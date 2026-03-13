with open('input.txt', 'w') as f:
    n = input()
    f.write(n + "\n")
    
    n1 = input()
    f.write(n1 + "\n")

    n2 = input()
    f.write(n2 + "\n")

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    n1 = list(map(int, f.readline().split()))
    n2 = list(map(int, f.readline().split()))

result = sum(x * y for x, y in zip(n1, n2))
print(result)