# Análisis financiero
# Proyecto: Industrias Lácteas Toni S.A.

# Este archivo contiene la estructura
# para realizar cálculos financieros
# como liquidez, endeudamiento y rentabilidad.

def calcular_liquidez(activo_corriente, pasivo_corriente):
    return activo_corriente / pasivo_corriente


def calcular_roa(utilidad_neta, activos):
    return utilidad_neta / activos


def calcular_roe(utilidad_neta, patrimonio):
    return utilidad_neta / patrimonio