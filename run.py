from datetime import date #uso da biblioteca datetime para pegar a data atual no sistema

#função para calcular idade atual do usuário
def calcular_idade(dd, mm, aa) -> int:
    hoje = date.today()
    return hoje.year - aa - ((hoje.month, hoje.day) < (mm, dd))

#funcao para calcular idade futura do usuário
def calcular_idade_futura(dd, mm, aa) -> int:
    return calcular_idade(dd, mm, aa) + 1