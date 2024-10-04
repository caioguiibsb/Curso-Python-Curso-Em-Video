#Faça um programa que leia o ano de nascimento de um jovem e informe de acorco com a idade dele se ele ainda vai se alistar ao servico milita. se a esta na hora de se alistar. se ja passou do tempo do alistamento. tambem  devera mostrar p tempo qeu falta ou o tempo q ja se passou
anonascimetno=int(input("Digite o ano do seu nascimento;"))
anoatual = 2024
if anoatual-anonascimetno > 18:
    print("Ja passou do periodo de alistamento")
elif anoatual-anonascimetno == 18:
    print("Ja esta na hora de se alistar")
else:
    anoatual-anonascimetno < 18
    print("Voce ainda vai se alistar")

if anoatual-anonascimetno > 18:
    print(f"Ja se passou: {(anoatual-anonascimetno-18)*12} meses")
elif anoatual-anonascimetno < 18:
    print(f"Falta ainda: {(anoatual-anonascimetno-18)*12} meses")
