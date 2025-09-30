# programa 01 - conversion de divisas (global change)
# autor: Cristhian 
# Descripcion: convierte un monto fijo de 1000 soles (PEN) a dolares (usd)
# utilizando una tasa de cambio de 3.85 PEN por USD

# monto en soles (PEN)
monto_soles = 1000
# tasa de cambio (1 USD = 3.85 PEN)
tasa_cambio = 3.85 
# calcular el monto equivalente en dolares (USD)
monto_dolares = monto_soles / tasa_cambio

# mostrar los resultados
print("\n--- conversion en global change ---")
print(f"monto en soles: S/{monto_soles: .2f}")
print(f"tasa de cambio: 1 USD = S/ {tasa_cambio: .2f}")
print(f"equivalente en dolares: $ {monto_dolares: .2f}")