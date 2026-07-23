# Pruebas del proyecto financiero
# Industrias Lácteas Toni S.A.

from src.analysis.analisis_financiero import calcular_liquidez


def test_liquidez():
    resultado = calcular_liquidez(10000, 5000)

    assert resultado == 2