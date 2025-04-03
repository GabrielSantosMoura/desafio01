hora1 = int(input("Digite o primeiro tempo em hora: "))
#minuto1 = input("Digite o primeiro tempo em minutos: ")#
hora2 = int(input("Digite o segundo tempo em hora: "))
#minuto2 = input("Digite o segundo tempo tempo em minutos: ")#

soma_hora1_uss = hora1 + hora2
soma_mq6 = (hora1 + hora2) - 12
#soma_minuto1 =#
soma_hora1_brs = (hora1 - 12) + (hora2 - 12)
if hora1 > 12 or hora2 > 12:#se for no padrao brasileiro#
    print(soma_hora1_brs)
else:
    if hora1 <= 6 or hora2 <= 6: #codicao das horas no padrão americano#
        print(soma_hora1_uss)
    else:
        if hora1 + hora2 > 6: #condicao horas maior que 6#
            print(soma_mq6)
        else:
            if hora1 + hora2 > 18:
                print(soma_hora1_brs / 2)



