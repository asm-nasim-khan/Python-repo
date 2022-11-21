name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
dd = dict()
for line in handle:
    if not line.startswith("From"): continue
    if line.startswith("From:"): continue
    lx = line.split()
    dd[lx[1]] = dd.get(lx[1], 0) + 1
bigC = None
bigw = None
for key, value in dd.items():
    if bigC is None or value > bigC:
        bigC = value
        bigw = key
print(bigw, bigC)