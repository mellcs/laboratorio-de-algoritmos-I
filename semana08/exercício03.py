def total ():
    laranjas = int(input("Quantas laranjas você comprou?"))
    precoUnitário = 0

    if laranjas <= 12:
        precoUnitario = 0.40
    
    elif laranjas >= 12:
        precoUnitario = 0.25

    multi = laranjas*precoUnitario
    return multi
    

    
def main():
    totalvalor = total()
    print("Você deverá pagar:", totalvalor)
    
main()