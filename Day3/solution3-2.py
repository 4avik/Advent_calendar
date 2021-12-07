f = open("example3.txt", "r")

lines = [line.strip() for line in f.readlines()]
print(lines)
counter = [0,0,0,0,0]
for i in range(len(counter)):
    print(i)
    for l in lines:
        print(l)