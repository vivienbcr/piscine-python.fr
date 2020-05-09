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
                print(x, " OUI")
            else:
                print(x, " NON")
    f.close()
except FileNotFoundError:
    print('File does not exist')
