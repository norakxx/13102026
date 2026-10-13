# Hacer una calculadora de pagos mensuales de hipoteca.
# M = P[r(1+r)^n] / [(1+r)^n - 1]
#Obtener capital
precioinicial= int(input("introduce el capital en euros: "))
#Obtener interes fijo
EURIBOR= 3.354
interes= EURIBOR + 1
#obtener número de cuotas
numero_anos= int(input("En cuentos años lo quieres pagar: "))
numero_cuotas= numero_anos * 12
interes_mensual= interes / 12 / 100
#Calcular cuota mensual en base a la formula de AF
cuota_mensual= precioinicial* (interes_mensual * (1+interes_mensual) ** numero_cuotas) / ((1+interes_mensual)** numero_cuotas)
cuota_mensual= round(cuota_mensual,2)
print(f"La cuota mensual es {cuota_mensual} €")
#sueldo
Sueldo= int(input("Introduce tu sueldo: "))
Sueldo_30= Sueldo*0.3
if Sueldo_30 < cuota_mensual :  
    print("No te la puedes comprar")
else:
    Sueldo_30 > cuota_mensual
    print("Felicidades chula")