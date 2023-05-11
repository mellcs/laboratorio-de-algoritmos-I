def converter_notacao(hora, minutos):
    if hora >= 0 and hora <= 23 and minutos >= 0 and minutos <= 59:
        if hora >= 12:
            periodo = "P.M."
            if hora > 12:
                hora -= 12
        else:
            periodo = "A.M."
            if hora == 0:
                hora = 12
        
        return hora, minutos, periodo
    else:
        return None

def exibir_notacao(hora, minutos, periodo):
    if hora is not None:
        print("A notação de 24 horas {}:{} corresponde a {}:{} {}.".format(hora, minutos, hora, minutos, periodo))
    else:
        print("Valores de hora ou minutos inválidos!")

hora = int(input("Digite a hora (entre 0 e 23): "))
minutos = int(input("Digite os minutos (entre 0 e 59): "))

hora_convertida = converter_notacao(hora, minutos)
exibir_notacao(*hora_convertida)