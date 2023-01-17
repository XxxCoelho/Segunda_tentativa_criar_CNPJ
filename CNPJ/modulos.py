from random import randint


def validacao_ou_gerador_CNPJ(CNPJ_inteira=None, Gerador=False):
    """
    :param CNPJ_inteira: None, se caso não for verificar seu CNPJ
    :param Gerador: Vai gerar um CNPJ novo
    :return: Verdadeiro ou Falso
    """
    try:
        if Gerador:
            CNPJ_inteira = gerador_CNPJ()

        CNPJ = retirar_residuos(CNPJ_inteira)

        CNPJ_copia = CNPJ[:-2] if len(CNPJ) == 14 else CNPJ

        if not CNPJ.isnumeric():
            print('Digite apenas números!')
            return False

        if verificador_repetidos(CNPJ):
            print(f'CNPJ com números repedidos: {organizador(CNPJ)}')

        if len(CNPJ) > 14:
            print(f'CNPJ: {CNPJ} tem mais de 14 digitos!')

        digito1 = achar_digito(CNPJ_copia, 1)
        CNPJ_copia += digito1
        digito2 = achar_digito(CNPJ_copia, 2)
        CNPJ_copia += digito2

        if Gerador:
            print(f'CNPJ: {organizador(CNPJ_copia)}')
            return True

        if CNPJ == CNPJ_copia:
            return True
        else:
            return False
    except Exception as erro:
        print(erro)
        return False


def achar_digito(lista, digito):
    Lista_de_numeros = [int(valor) for valor in lista]
    lista_multiplicadores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    if digito == 1:
        lista_multi = lista_multiplicadores[1:]
    elif digito == 2:
        lista_multi = lista_multiplicadores
    else:
        return None

    uniao = zip(Lista_de_numeros, lista_multi)
    total = sum([valor[0] * valor[1] for valor in uniao])

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0
    return str(digito)


def verificador_repetidos(numeros):
    sequencia = numeros[0] * len(numeros)
    if sequencia == numeros:
        return True


def organizador(numeros):
    organizado = ''
    for indices, valor in enumerate(str(numeros)):
        if indices == 1 or indices == 4:
            organizado += valor
            organizado += '.'
        elif indices == 7:
            organizado += valor
            organizado += '/'
        elif indices == 11:
            organizado += valor
            organizado += '-'
        else:
            organizado += valor
    return organizado


def retirar_residuos(CNPJ):
    CNPJ = CNPJ.strip().replace('.', '').replace(',', '').replace('/', '').replace('-', '')
    return CNPJ


def separador_numeros(numeros):
    Lista_de_numeros = [int(valor) for valor in numeros]
    return Lista_de_numeros


def soma_digito(lista, digito):
    Lista_de_numeros = [int(valor) for valor in lista]
    lista_multiplicadores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    if digito == 1:
        lista_multi = lista_multiplicadores[1:]
    elif digito == 2:
        lista_multi = lista_multiplicadores
    else:
        return None

    uniao = zip(Lista_de_numeros, lista_multi)
    total = sum([valor[0] * valor[1] for valor in uniao])
    return total


def gerador_CNPJ():
    CNPJ = str(randint(10000000, 99999999)) + '0001'
    return CNPJ
