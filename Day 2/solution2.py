f = open("Day 2/example2.txt", "r")

lines = f.readlines()
print(lines)
horizontal = 0
depth = 0

for command in lines:
    command = command.split()
    print(command)
    if command [0] == "forward":
        horizontal += int(command[1]) 
    elif command[0] == "down":
        depth +int(command[1])
    elif command[0] == "up":
        depth -= int(command[1])
    print(horizontal * depth)
