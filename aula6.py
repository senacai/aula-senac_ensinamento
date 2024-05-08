'''
def fatorial( a ):
    if a == 0:
        return 1
    else:
        fat = 1
        for i in range (1, a+1):
            fat *= i
            return fat
         
x = int(input("Digite um número inteiro:"))
print("O fatorial de " , x, " é: " , fatorial(x))
'''
'''
nome = input("Digite seu nome")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
tem_carro = input("Você possui algum carro? (Sim/Não): ")


tem_carro = tem_carro.lower() == "sim"

print("Informações digitadas: ")
print("Nome: ", nome)
print("Idade: ", idade)
print("Altura: ", altura)
print("Tem carro/ ", "Sim" if tem_carro else "Não")
'''

'''
def contagem_regressiva():
    numero = int(input("Digite um número inteiro positivo: "))

    if numero <= 0:
        print("Por favor, digite um número inteiro positivo. ")
        contagem_regressiva()

    else:
        while numero >=0:
            print(numero)
            numero -= 1

            contagem_regressiva()

'''

def soma ( a, b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao (a, b):
    return a  * b
def divisao (a, b):
    if b != 0:
     return a / ( " belse " )
     return "Divisão invalida"