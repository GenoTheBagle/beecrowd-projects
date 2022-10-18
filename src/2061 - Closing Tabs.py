n, m = list(map(int, input().split()))
for _ in range(m):
    a = input()
    if a == "fechou": # close tab
        n += 1
    elif a == "clicou": # click on ad
        if n != 0:
            n -= 1
print(n)
