myfile = open("Day 3/example3.txt")
lines = myfile.readlines()
gamma = ""
epsilon =  ""

print(lines)

rate = [0]*len(lines[0].strip())
print(rate)

for bin_num in lines:
    i = 0
    for bit in bin_num.strip:
        if bit == "0":
            rate[i] -= 1
        else:
            rate[i] += 1
        i += 1

print(rate)

for bit in rate:
    if bit <= 0:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(int(gamma, 2)*int(epsilon, 2))