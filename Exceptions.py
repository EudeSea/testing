itens = 0

if itens != 2:
    pass


assert (itens == 0)

try:
    with open('test.txt','r') as reader:
        reader.read()
except Exception as e:
    print("error on: ", e)

finally:
    print("checking the resources")