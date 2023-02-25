# Represa Hidroituango

# ENTRADAS

nivelAgua = int(input("Digite el nivel del agua: "))

# PROCESO
if nivelAgua >= 0 and nivelAgua <= 250:
    print(f'el sensor marca {nivelAgua}, muy bajo..')
elif nivelAgua > 250 and nivelAgua <= 400:
    print(f'el sensor marca {nivelAgua},  operando normal..')
else:
    print(f'el sensor marca {nivelAgua}, peligro..')
