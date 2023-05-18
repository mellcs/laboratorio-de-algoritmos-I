def temperatura (celsius, farhrenheit):
    celsius = float(input("Insira a temperatura:"))
    farhrenheit = (celsius * 9/5) + 32 
    
def main (temperatura):
    celsius = float(input("Insira a temperatura:"))
    farhrenheit = (celsius * 9/5) + 32 
    print("A conversão é de:", farhrenheit)

main(temperatura)