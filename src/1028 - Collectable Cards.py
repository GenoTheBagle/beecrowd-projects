import math
# greatest common divisor
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    print(math.gcd(a,b))
