def isPrime(a):
    count = 0
    if a>1:
        for i in range(2,a):
            if a % i == 0:
                count = count + 1
        if count == 0:
            return True
    return False

def kNumCounter(a,b):
    kCount = 0
    while(a<b):
        sum = 0
        for i in range(1,a+1):
            if a % i == 0:
                sum = sum + i
        print('sum for',a,':',sum)
        check = isPrime(sum)
        if check:
            kCount = kCount + 1
        a = a + 1
    return kCount

size = int(input(""))
values = []
for i in range(size):
    values.append(input(""))
for items in values:
    sp = items.split(" ")
    start = int(sp[0])
    end = int(sp[1])
    count = kNumCounter(start,end)
    print(count)