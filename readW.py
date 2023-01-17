file = open("test.txt")

#print(file.read())

line = file.readline()
while line!="":
    print(line)
    line = file.readline()

file.close()
