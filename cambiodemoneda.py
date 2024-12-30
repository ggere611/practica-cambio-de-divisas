
mon_eur=float(input("ingresar el valor del EUR: "))
mon_dol=float(input("ingresar el valor del USD: "))
#elegir el tipo de cambio
#De dolar a euro
tipo_moneda=input("Se quiere cambiar de peso mexicano a (EUR/USD): ")
moneda=float(input("Valor que se quiere convertir: "))
if tipo_moneda.upper()=="EUR":
    resultado=moneda*mon_eur
    print("El valor de peso mexicano a EUR es:",resultado)
elif tipo_moneda.upper()=="USD":
    resultado=moneda*mon_dol
    print("El valor de peso mexicano a USD es:",resultado)
else:
    print("El tipo de divisa no esta apta para la conversion")