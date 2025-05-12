a, b = input().split()
a, b = int(a), int(b)


if a % b == 0 or b % a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
