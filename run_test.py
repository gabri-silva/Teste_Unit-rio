from run import calcular_idade, calcular_idade_futura


def test_calcular_idade():
    assert calcular_idade(1, 1, 2000) == 26
    assert calcular_idade(31, 12, 1990) == 35
    assert calcular_idade(15, 6, 1985) == 41


def test_calcular_idade_futura():
    assert calcular_idade_futura(1, 1, 2000) == 27
    assert calcular_idade_futura(31, 12, 1990) == 36
    assert calcular_idade_futura(15, 6, 1985) == 42