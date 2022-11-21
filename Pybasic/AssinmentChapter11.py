import re
fh = input("File name:")
fhand = open(fh)
#lst = list()
lst= re.findall('[0-9]+',fhand.read())
sum=0
for x in lst:
    x=int(x)
    sum=sum+x
print(sum)

**************************
