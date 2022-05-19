from main import somar, subtrair, multiplicar, dividir


def testar_somar():
    # 1 - Configura
    numero_a = 8
    numero_b = 7
    resultado_obtido = 15

    # 2 - Executa
    resultado_esperado = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido


def testar_subtrair():
    # 1 - Configura
    # 1.1 - Dados de entrada / valores do Teste
    numero_a = 15
    numero_b = 10

    # 1.2 - Resultado esperado
    resultado_esperado = 5

    # 2 - Executa
    resultado_obtido = subtrair(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def testar_multiplicar():
    # 1 - Configura
    numero_a = 5
    numero_b = 9
    resultado_esperado = 45

    # 2 - Executa
    resultado_obtido = multiplicar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def testar_dividir_positivo():
    # 1 - Configura
    numero_a = 386
    numero_b = 4
    resultado_esperado = 96.5

    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado


def testar_dividir_negativo():
    # 1 - Configura
    numero_a = 386
    numero_b = 0
    resultado_esperado = 'Não dividirás por zero'

    # 2 - Executa
    resultado_obtido = dividir(numero_a, numero_b)

    # 3 - Valida
    assert resultado_obtido == resultado_esperado

# TDD - Test Driven Development
# Criar os testes de unidade no começo do desenvolvimento.
# Executar todos os testes pelo menos uma vez por dia

#teste