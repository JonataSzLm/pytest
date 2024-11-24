"""
    1 - Receber um numero inteiro
    2 - Retornar Bacon com ovos se o numero for multiplo de 3 e 5
    3 - Retornar Passar fome se o numero não for multipllo de 3 ou de 5
    4 - Retornar Bacon se o numero for multiplo de 3
    5 - Retornar Ovos se o numero for multiplo de 5
"""


def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser int'

    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'

    if n % 3 == 0:
        return 'Bacon'

    if n % 5 == 0:
        return 'Ovos'

    return 'Passar fome'
