with open("output.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")

list_day15 = []

with open("../day15/sample.txt") as f:
    for line in f:
        list_day15.append(line)

print(list_day15)