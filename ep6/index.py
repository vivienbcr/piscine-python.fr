import re
try:
    f = open('ep6.txt', mode="r")
    f.seek(0)
    first_char = f.read(1)
    if not first_char:
        print("file is empty")
    else:
        f.seek(0)
        for x in f:
            temp = re.findall(r'\d+', x)
            res = list(map(int, temp))
            if res[0] < res[1]:
                 print("OUI V1 : ", res[0], "< à V2 :", res[1])
            else:
                print("NON V1: ", res[0], "> à la V2 :", res[1])
    f.close()
except FileNotFoundError:
    print('File does not exist')
