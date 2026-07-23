# Modelo de evaluación de inversiones
# Industrias Lácteas Toni S.A.

def calcular_van(flujos, tasa, inversion):
    valor_actual = 0
    
    for periodo, flujo in enumerate(flujos, start=1):
        valor_actual += flujo / ((1+tasa)**periodo)
    
    return valor_actual - inversion


def calcular_tir():
    pass