notap1 = float(input("Insira sua primeira nota parcial:"))
notap2 = float(input("Insira sua segunda nota parcial:"))
frequencia = float(input("Insira a porcentagem da sua frequência no semestre atual:"))

media = (notap1 + notap2) / 2

if media >= 7.0 and frequencia >= 75:
    print("Você foi aprovado! Parabéns!")
elif media >= 4.0 and media < 7.0 and frequencia > 75:
    print("Você está em exame! Boa sorte!")
elif media < 4.0 or frequencia < 75:
    print("Você foi reprovado! Nos vemos no próximo semestre!")

#Não tenho certeza se este está funcionando.
