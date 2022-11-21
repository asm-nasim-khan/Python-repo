num=input("List: ")
lis=[int(i) for i in num.split(',')]
n=len(lis)
largest = lis[0]
for number in lis:
    if number>largest:
        largest = number
sec_largest = lis[0]
sec_largest_index = 0
for iter in range(n):
    if lis[iter]>sec_largest and lis[iter] != largest:
        sec_largest = lis[iter]
        sec_largest_index = iter
print(sec_largest_index,'--> Index of 2nd largest')