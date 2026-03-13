with open('input.txt', 'w') as f:
    n = input()
    f.write(n + "\n")
    
    n1 = input()
    f.write(n1 + "\n")

with open('input.txt', 'r') as f:
    n = f.readline().strip()
    n1 = f.readline().split()


result = max(n1, key=len)
print(result)