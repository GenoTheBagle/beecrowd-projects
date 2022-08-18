import math
x1, y1 = list(map(float, input().split()))
x2, y2 = list(map(float, input().split()))

d = ((x2-x1)**2) + ((y2-y1)**2)
d = math.sqrt(d)
print(f"{d:.4f}") # I forget how to do :.4f without an f-string haha
