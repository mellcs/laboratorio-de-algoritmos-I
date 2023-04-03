mediap1 = float(input("Insira sua primeira nota:"))
mediap2 = float(input("Insira sua segunda nota:"))
nota = (mediap1 + mediap2)/2

if nota >=9.0 and nota <=10.0:
    print("Suas notas foram", mediap1, "e", mediap2, ". Sua média é de ", nota, "e seu conceito foi A. Parabéns, você foi aprovado!")
elif nota >= 7.5 and nota< 9.0:
    print("Suas notas foram", mediap1, "e", mediap2, ". Sua média é de ", nota, "e seu conceito foi B. Parabéns, você foi aprovado!")
elif nota >= 6.0 and nota< 7.5:
    print("Suas notas foram", mediap1, "e", mediap2, ". Sua média é de ", nota, "e seu conceito foi C. Parabéns, você foi aprovado!")
elif nota >= 4.0 and nota <6.0:
    print("Suas notas foram", mediap1, "e", mediap2, ". Sua média é de ", nota, "e seu conceito foi D. Infelizmente, você foi reprovado.")
elif nota >= 4.0 and nota <0:
    print("Suas notas foram", mediap1, "e", mediap2, ". Sua média é de ", nota, "e seu conceito foi E. Infelizmente, você foi reprovado.")


