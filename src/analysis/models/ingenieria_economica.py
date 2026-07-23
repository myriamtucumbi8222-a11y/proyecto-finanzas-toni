import numpy_financial as npf

# Inversión inicial
inversion = -50000000

# Flujos de caja proyectados
flujos = [12000000, 14000000, 16000000, 18000000, 22000000]

# Tasa de descuento
tasa = 0.12

# VAN
van = npf.npv(tasa, flujos) + inversion

# TIR
tir = npf.irr([inversion] + flujos)

print("========== RESULTADOS ==========")
print(f"VAN: ${van:,.2f}")
print(f"TIR: {tir*100:.2f}%")