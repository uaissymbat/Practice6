with open('input.txt', 'w') as f:
    n = input()
    f.write(n + "\n")


with open('input.txt', 'r') as f:
    n = f.readline().strip().lower()

vowels = {'a', 'e', 'i', 'o', 'u'}
result = "Yes" if any(char in vowels for char in n) else "No"
print(result)