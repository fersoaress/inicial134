import csv

import pytest

from main import somar, subtrair, multiplicar, dividir


def ler_csv(arquivo_csv):
    dados_csv = []
    try:
        with open(arquivo_csv, newline='') as massa:
            campos = csv.reader(massa, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')


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


#lista para uso como massa de teste
lista_de_valores = [
    (8, 7, 15),
    (20, 30, 50),
    (25, 0, 25),
    (-5, 12, 7),
    (6, -3, 3)

]

@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', lista_de_valores)
def testar_somar_leitura_de_lista(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    #Utilizamos a lista como massa de teste

    # 2 - Executa
    resultado_obtido = somar(numero_a, numero_b)

    # 3 - Valida
    assert resultado_esperado == resultado_obtido


@pytest.mark.parametrize('numero_a, numero_b, resultado_esperado', ler_csv('/home/fernanda/PycharmProjects/inicial134/vendors/csv/massa_teste_somar_positivo.csv'))
def testar_somar_leitura_de_csv(numero_a, numero_b, resultado_esperado):
    # 1 - Configura
    #Utilizamos a lista como massa de teste

    # 2 - Executa
    resultado_obtido = somar(int(numero_a), int(numero_b))

    # 3 - Valida
    assert int(resultado_esperado) == resultado_obtido



# TDD - Test Driven Development
# Criar os testes de unidade no começo do desenvolvimento.
# Executar todos os testes pelo menos uma vez por dia
