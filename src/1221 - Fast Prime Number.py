for _ in range(int(input())):
    n = int(input())
    isit = False
    for i in range(2, (int(n**0.5)+1)):
        if n % i == 0:
            print("Not Prime")
            isit = True
            break
    if not isit: print("Prime")
