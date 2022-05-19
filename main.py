import pytest


def print_hi(name):
    print(f'Hi, {name}')


def somar(numero_a, numero_b):
    return numero_a + numero_b


def subtrair(numero_a, numero_b):
    return numero_a - numero_b


def multiplicar(numero_a, numero_b):
    return numero_a * numero_b


def dividir(numero_a, numero_b):
    try:
        return numero_a / numero_b
    except ZeroDivisionError:
        return 'Não dividirás por zero'


if __name__ == '__main__':
    print_hi('PyCharm')

    #Chamar a definição somar e mostrar o resultado
    resultado = somar(7, -6)
    print(f'A soma: {resultado}')

    #Chamar a definição subtrair e mostrar o resultado
    resultado = subtrair(25, 8)
    print(f'A subtração: {resultado}')

    #Chamar a definição multiplicar e mostrar o resultado
    resultado = multiplicar(8, 9)
    print(f'A multiplicação: {resultado}')

    #Chamar a definição divisão e mostrar o resultado
    resultado = dividir(100, 5)
    print(f'A divisão: {resultado}')


def testar_somar():
    #1 - Configura
    numero_a = 8
    numero_b = 7
    resultado_obtido = 15

    #2 - Executa
    resultado_esperado = somar(numero_a, numero_b)

    #3 - Valida
    assert resultado_esperado == resultado_obtido


def testar_subtrair():
    #1 - Configura
    #1.1 - Dados de entrada / valores do Teste
    numero_a = 15
    numero_b = 10

    #1.2 - Resultado esperado
    resultado_esperado = 5

    #2 - Executa
    resultado_obtido = subtrair(numero_a, numero_b)

    #3 - Valida
    assert resultado_obtido == resultado_esperado


def testar_multiplicar():
    #1 - Configura
    numero_a = 5
    numero_b = 9
    resultado_esperado = 45

    #2 - Executa
    resultado_obtido = multiplicar(numero_a, numero_b)

    #3 - Valida
    assert resultado_obtido == resultado_esperado


def testar_dividir_positivo():
    #1 - Configura
    numero_a = 386
    numero_b = 4
    resultado_esperado = 96.5

    #2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    #3 - Valida
    assert resultado_obtido == resultado_esperado


def testar_dividir_negativo():
    #1 - Configura
    numero_a = 386
    numero_b = 0
    resultado_esperado = 'Não dividirás por zero'

    #2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    #3 - Valida
    assert resultado_obtido == resultado_esperado

# TDD - Test Driven Development
# Criar os testes de unidade no começo do desenvolvimento.
# Executar todos os testes pelo menos uma vez por dia