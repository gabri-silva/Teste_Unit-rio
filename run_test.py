from datetime import date, timedelta

import pytest
from run import calcular_idade, calcular_idade_futura, calcular_dias_passados


def test_calcular_idade():
    assert calcular_idade(1, 1, 2000) == 26
    assert calcular_idade(31, 12, 1990) == 35
    assert calcular_idade(15, 6, 1985) == 41

def test_calcular_dias_passados():
    assert calcular_dias_passados(1, 1, 2020) == (date.today() - date(2020, 1, 1)).days
    assert calcular_dias_passados(31, 12, 2019) == (date.today() - date(2019, 12, 31)).days
    assert calcular_dias_passados(15, 6, 2018) == (date.today() - date(2018, 6, 15)).days
