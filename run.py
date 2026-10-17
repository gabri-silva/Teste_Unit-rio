from datetime import date #uso da biblioteca datetime para pegar a data atual no sistema

#função para calcular idade atual do usuário
def calcular_idade(dd, mm, aa) -> int:
    hoje = date.today()
    return hoje.year - aa - ((hoje.month, hoje.day) < (mm, dd))

#Calcular quantos dias foram passados
def calcular_dias_passados(dd, mm, aa) -> int:
    data_passada = date(aa, mm, dd)
    hoje = date.today()

    if data_passada > hoje:
        raise ValueError("A data informada deve estar no passado.")

    return (hoje - data_passada).days
