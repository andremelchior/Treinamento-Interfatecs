a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

triangulo = (a * c) / 2
circulo = 3.14159 * c**2
trapezio = (a + b) * (c / 2)
quadrado = b**2
retanqulo = a * b

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {quadrado:.3f}')
print(f'RETANGULO: {retanqulo:.3f}')
