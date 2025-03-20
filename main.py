n = 1
p = 1
fim = 0

def sequencia_de_fibonacci(n,p,numero_final,fim):
    resultado = 0
    anterior = n
    soma = n + p
    resultado = soma + anterior
    fim = resultado
    if fim > numero_final:
        print('fim de fibonacci')
        return
    print(resultado)
    return sequencia_de_fibonacci(soma,anterior,numero_final,fim)


numero_final = int(input("Sequencia de Fibonacci até:\nEscolha o número:  "))

sequencia_de_fibonacci(n,p,numero_final,fim)


print('Fim de Fibonacci')