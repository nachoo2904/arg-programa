class Empleado:

    def __init__(self, sueldo1, sueldo2, sueldo3):
        self.sueldo1 = sueldo1
        self.sueldo2 = sueldo2
        self.sueldo3 = sueldo3
juan = Empleado (300, 500, 700)

def calcular_sueldo():
    promedio = (juan.sueldo1 + juan.sueldo2 + juan.sueldo3) / 3
    print("El sueldo promedio de Juan durante el año fue de ", promedio)

    if(promedio < 300):
        print("Sueldo bajo")
    if(300 < promedio < 900):
        print("Sueldo normal")
    if(promedio > 900):
        print("Sueldo mejor de lo normal")
    

calcular_sueldo()
