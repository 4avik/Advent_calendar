f = open("example.txt", "r")

lines = f.readlines()
counter = 0

for i in range(len(lines)-1):
    line = int(lines[i].strip())
    next_line = int(lines[i+1].strip())
    if line < next_line:
        counter += 1

print(counter)
