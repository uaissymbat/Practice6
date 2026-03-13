f = open("demofile.txt")

f = open("demofile.txt", "rt")
print(f.read())

f = open("D:\\myfiles\welcome.txt")
print(f.read())

with open("demofile.txt") as f:
  print(f.read())

f.close()
