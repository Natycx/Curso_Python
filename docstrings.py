"""
Documentando funções com docstrings

OBS: Podemos ter acesso á documentação de um função em python
utilizando a propriedade especial __doc__

"""

# Exemplos

def diz_oi():
    """ Uma funçao simpes que retorna a string oi"""
    return 'Oi'

def exponencial(numero, potencia=2):
    """
    FUnção que retorna por padrão o quadrado de um numero ou numero a potencia informada
    :param numero: Numero que desejamos gerar o exponencial
    :param potencia: Potencia que queremos gerar o exponencial Por padrão é 2
    :return: Retorna o exponencial de um numero por potencia
    """
    return numero ** potencia