f = open("sample.txt")

content = f.read()

print(content)

f.close()

f = open("sample.txt")

for line in f:
    print(line.strip())

f.close()


with open("sample.txt") as f:
    for line in f:
        print(line.strip())
