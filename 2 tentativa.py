from CNPJ import modulos


if modulos.validacao_ou_gerador_CNPJ(Gerador=True):
    print('Válido')
else:
    print('Inválido')
