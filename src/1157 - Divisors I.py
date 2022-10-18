l = []; n = int(input())
for i in range(1, n+1):
    if n % i == 0: l.append(i)
l = list(set(l)); l.sort()
for item in l: print(item)
