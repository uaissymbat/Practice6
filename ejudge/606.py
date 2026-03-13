with open('input.txt', 'w') as f:
    n = input()
    f.write(n + "\n")
    
    numbers = input()
    f.write(numbers + "\n")

with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    numbers = list(map(int, f.readline().split()))

nonn = all(n >= 0 for n in numbers)
if nonn:
    print("Yes")
else:
    print("No")