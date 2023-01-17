file = open("test.txt")

line = file.readline()
for line in file.readlines():
    print(line)

file.close()