import re
sList = ["\b\t80cm\t60cm\n" , "\b\t81cm\t51cm\n" , "\b\t105cm\t145cm\n" ]
print(sList)

for x in range(len(sList)) :
 temp = re.findall(r'\d+', sList[x])
 res = list(map(int, temp))
 if res[0] < res[1] :
   print(res[0])