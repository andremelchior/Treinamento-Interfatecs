def primo():
    x = int(input())
    divisores = 0
    pd = 1
    
    i = 0
    while i <= x:
        if x % pd == 0:
            divisores+=1
        pd += 1
        i+=1
        
    if divisores == 2:
        print(f'{x} eh primo')
    else:
        print(f'{x} nao eh primo')

def main():
    qtd = int(input())

    i = 0
    while i < qtd:
        primo()
        i+=1
        
main()
