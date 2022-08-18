p1c, p1n, p1p = input().split()
p1c, p1n = int(p1c), int(p1n)
p1p = float(p1p)

p2c, p2n, p2p = input().split()
p2c, p2n = int(p2c), int(p2n)
p2p = float(p2p)

# don't need p1c/p2c in this case
total = 0.0
total += (p1n*p1p)
total += (p2n*p2p)
print(f"VALOR A PAGAR: R$ {total:.2f}")
