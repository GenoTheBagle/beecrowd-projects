a, b, c = list(map(float, input().split()))

t = 0.5 * a * c
print(f"TRIANGULO: {t:.3f}")

t = 3.14159 * (c**2)
print(f"CIRCULO: {t:.3f}")

t = ((a + b)/2) * c
print(f"TRAPEZIO: {t:.3f}")

t = b * b
print(f"QUADRADO: {t:.3f}")

t = a * b
print(f"RETANGULO: {t:.3f}")
