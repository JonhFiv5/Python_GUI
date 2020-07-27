from random import randint


def gerar_cpf():
    novo_cpf = str(randint(100000000, 999999999))
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

    return f'{novo_cpf[:3]}.{novo_cpf[3:6]}.{novo_cpf[6:9]}-{novo_cpf[9:]}'
