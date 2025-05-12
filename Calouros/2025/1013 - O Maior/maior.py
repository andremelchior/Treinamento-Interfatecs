a, b, c = input().split()
a, b, c = int(a), int(b), int(c) 
maior = (a + b + abs(a-b)) / 2

if maior < c:
    maior = c

print(f'{maior:.0f} eh o maior')
