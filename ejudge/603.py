with open('input.txt', 'w') as f:
    n = input()
    f.write(n + "\n")
    
    strings = input()
    f.write(strings + "\n")

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    strings = list(map(str, f.readline().split()))

result = " ".join(f"{i}:{string}" for i, string in enumerate(strings))
print(result)