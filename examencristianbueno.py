from statistics import mean , geometric_mean
from random import randint 

nombre = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trabajadores=[]
sueldos=[]




def sueldos_aleatorios():
    for trabajador in nombre:
        info={"nombre":trabajador} , {"sueldo":randint(300000 , 2500000)}
        trabajadores.append(info)
        sueldos.append(randint(300000 , 2500000))
    print(trabajadores)
    print("sueldos aleatorios creados con exito!!")
    
        
            
            
def ver_estadistica():
    for i in sueldos:
        print(f"el sueldo minimo es de : {min(sueldos)}")
        print(f"el sueldo maximo es de : {max(sueldos)}")
        print(f"promedios de los sueldos: {mean(sueldos)}")
        print(f"promedio aritmetico es de: {geometric_mean(sueldos)}")
    
    
def impresion():
    for i in trabajadores:
        archivo=open("archivo" , "w")
        archivo.write({trabajadores})
        archivo.close           
       
    
    
        
while True:
    print("1) Asignar sueldos aleatorios :")
    print("2) Clasificar sueldos : ")
    print("3) Ver estadisticas : ")
    print("4) Reporte de sueldos : ")
    print("5) Salir del programa")
    opc=input("ingrese una opcion : ")
    if opc=="1":
        sueldos_aleatorios()
    elif opc=="2":
        print("ayuda")    
    elif opc=="3":
        ver_estadistica()
    elif opc=="4":
        impresion()
    elif opc =="5":
        print(" salir del programa ")
        break
    
        
        
    


        
        

            
        
        
        

        
        
        

        
           


    
    
    
    
    