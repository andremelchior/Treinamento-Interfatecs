c1, n1, v1 = input().split()
c2, n2, v2 = input().split()

c1, n1, v1 = int(c1), int(n1), float(v1)
c2, n2, v2 = int(c2), int(n2), float(v2)

r = n1 * v1 + n2 * v2

print(f'VALOR A PAGAR: R$ {r:.2f}')
