hora1 = int(input("Digite o primeiro tempo em hora: "))
minuto1 = int(input("Digite o primeiro tempo em minutos: "))
hora2 = int(input("Digite o segundo tempo em hora: "))
minuto2 = int(input("Digite o segundo tempo tempo em minutos: "))
somah = hora1 + hora2
somm = minuto1 + minuto2

if somm > 59:
    somah+=1
    somah=somah - 60
if somah >= 36:
    somah-= 36
elif somah >= 24:
    somah = somah - 24
elif somah >= 12:
    somah = somah - 12
print(somah, somm)
