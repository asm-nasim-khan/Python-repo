
def partition(s):
    res = []
    part = []

    def dfs(i):
        if i >= len(s):
            res.append(part.copy())
            return
        for j in range (i, len(s)):
            if isPali(s, i, j):
                part.append(s[i:j+1])
                dfs(j + 1)
                part.pop()
    dfs(0)
    return res
def isPali(s, l, r):
    print('2')
    while l < r:
        if s[1] != s[r]:
            return False
        l, r= 1+1, r - 1
    return True
resut = partition('npn')