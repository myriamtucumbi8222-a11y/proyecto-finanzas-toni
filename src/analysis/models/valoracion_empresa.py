# Valoración empresarial
# Proyecto: Industrias Lácteas Toni S.A.

# Método de Flujo de Caja Descontado (DCF)

def valor_flujo_caja_descontado(flujos, tasa_descuento, crecimiento_terminal):

    valor_presente = 0

    for periodo, flujo in enumerate(flujos, start=1):

        valor_presente += flujo / ((1 + tasa_descuento) ** periodo)


    ultimo_flujo = flujos[-1]


    valor_terminal = (
        ultimo_flujo * (1 + crecimiento_terminal)
    ) / (
        tasa_descuento - crecimiento_terminal
    )


    valor_empresa = valor_presente + (
        valor_terminal /
        ((1 + tasa_descuento) ** len(flujos))
    )


    return valor_empresa



# Método de contraste por múltiplos

def valor_por_multiplo(utilidad_operativa, multiplo):

    valor = utilidad_operativa * multiplo

    return valor