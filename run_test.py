from datetime import date, timedelta

import pytest
from run import calcular_idade, calcular_idade_futura, calcular_dias_passados


def test_calcular_idade():
    assert calcular_idade(1, 1, 2000) == 26
    assert calcular_idade(31, 12, 1990) == 35
    assert calcular_idade(15, 6, 1985) == 41


def test_calcular_idade_futura():
    assert calcular_idade_futura(1, 1, 2000) == 27
    assert calcular_idade_futura(31, 12, 1990) == 36
    assert calcular_idade_futura(15, 6, 1985) == 42


def test_calcular_dias_passados_datas_antigas():
    assert calcular_dias_passados(1, 1, 2020) == (date.today() - date(2020, 1, 1)).days
    assert calcular_dias_passados(31, 12, 2019) == (date.today() - date(2019, 12, 31)).days
    assert calcular_dias_passados(15, 6, 2018) == (date.today() - date(2018, 6, 15)).days


def test_calcular_dias_passados():
    data_passada = date.today() - timedelta(days=10)
    assert calcular_dias_passados(data_passada.day, data_passada.month, data_passada.year) == 10


def test_calcular_dias_passados_hoje():
    hoje = date.today()
    assert calcular_dias_passados(hoje.day, hoje.month, hoje.year) == 0


def test_calcular_dias_passados_rejeita_futuro():
    amanha = date.today() + timedelta(days=1)
    with pytest.raises(ValueError, match="A data informada deve estar no passado"):
        calcular_dias_passados(amanha.day, amanha.month, amanha.year)
