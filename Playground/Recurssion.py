import time

A = [0]*100


def F(n):
    if n == 0 or n == 1:
        return n
    else:
        return F(n - 1) + F(n - 2)


def FM(n):
    print("Aloz")
    if A[n] > 0:
        return A[n]
    if n == 0 or n == 1:
        return n
    else:
        A[n] = FM(n - 1) + FM(n - 2)
        return A[n]


def CalcFib():
    A.insert(0, 1)
    A.insert(1, 1)
    for i in range(2, 30):
        A.insert(i, A[i - 1] + A[i - 2])


#-------------Tester----------------#
CalcFib()
startTime = time.time_ns()
print(FM(6))
duration = time.time_ns() - startTime
print(duration)

