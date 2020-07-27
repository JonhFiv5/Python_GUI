import re


def validar_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)
    if len(cpf) != 11:
        return 'CPF inválido.'
    novo_cpf = cpf[0:9]
    soma = 0

    # Calculando o décimo dígito
    for progressivo, regressivo in enumerate(range(10, 1, -1)):
        soma += int(novo_cpf[progressivo]) * regressivo

    novo_cpf += str(0 if 11 - (soma % 11) > 9 else 11 - (soma % 11))
    soma = 0

    # Calculando o décimo primeiro dígito
    for progressivo, regressivo in enumerate(range(11, 1, -1)):
        soma += int(novo_cpf[progressivo]) * regressivo

    novo_cpf += str(0 if 11 - (soma % 11) > 9 else 11 - (soma % 11))

    sequencia = (str(novo_cpf[0]) * len(cpf)) == novo_cpf

    return 'CPF válido.'\
        if cpf == novo_cpf \
        and not sequencia \
        else 'CPF inválido.'
