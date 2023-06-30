from random import randint
estudiante = []
while True:
    print("Bienvenido al Liceo Profesional")
    print("1) Grabar")
    print("2) Buscar")
    print("3) Imprimir Certificado")
    print("4) Salir")
    opc = int(input(" Ingrese una opcion: "))
    if opc == 1:
        while True:
            run = int(input("Ingrese su rut: "))
            nombre = input("Ingrese sus nombres: ")
            apellido = input("Ingrese sus apellidos: ")
            fecha = (input("Ingrese su fecha de nacimiento: "))
            carrera = input("Ingrese su carrera: ")
            asignatura = input("Ingrese sus asignaturas: ")
            notas = int(input("Ingrese su promedio: "))
            numero = int(input("Numero de lista: "))
            
            print("DATOS AÑADIDOS")
            
            for i in estudiante:
                print(f"run          :{i[0]}")
                print(f"nombre       :{i[1]}")
                print(f"apellido     :{i[2]}")
                print(f"fecha        :{i[3]}")
                print(f"carrera      :{i[4]}")
                print(f"asignatura   :{i[5]}")
                print(f"notas        :{i[6]}")
                print(f"numero       :{i[7]}")
            break
    elif opc == 2:
        
        run = input("Ingrese Rut")
        for i in estudiante:
            if i[0] == run:
                print("RUT NO ENCONTRADO")
                
                print(f"run          :{i[0]}")
                print(f"nombre       :{i[1]}")
                print(f"apellido     :{i[2]}")
                print(f"fecha        :{i[3]}")
                print(f"carrera      :{i[4]}")
                print(f"asignatura   :{i[5]}")
                print(f"notas        :{i[6]}")
                print(f"numero       :{i[7]}")
                break
            else:
                print("Estudiante no encontrado")
    elif opc == 3:
         
         while True:
             
             print("Certificados")
             
             print("1.-Certificado de alumno regular")
             print("2.-Certificado de notas")
             print("3.-Salir")
             resp = int(input("Ingrese una opcion:"))
             
             if resp == 1:
                 print("1.-Certificado de alumno regular")
                 while True:
                     run= input("Ingrese su rut")
                     if len(run) == 6:
                         if (run[:4].isalpha() and run[4:].isdigit()) or (run[:2].isalpha() and run[2:].isdigit()):
                             break
                         for i in run:
                             if i[0] == run:
                                 print("rut no encontrado")
                                 print("------------------------------------")
                                 print("certificado de alumno regular")
                                 print(f"run      :{i[0]}")
                                 print(f"carrera  :{i[4]}")
                                 numero = randint(1000,5000)
                                 print(f"Valor            :${numero}")
                                 break
                             
                             else:
                                 print("ESTUDIANTE NO ENCONTRADO")
                                 
             elif resp == 2:
                 print("2.-Certificado de notas")
                 while True:
                     patente = input("Ingrese su rut")
                     if len(run) == 6:
                         if (run[:4].isalpha() and run[4:].isdigit()) or (run[:2].isalpha() and run[2:].isdigit()):
                             break
                         for i in estudiante:
                             if i[0] == patente:
                                 print("Estudiante encontrado")
                                 print("------------------------------------")
                                 print("Tipo de certificado: certificado de notas")
                                 print(f"asignaturas        :{i[5]}")
                                 print(f"promedio           :{i[6]}")
                                 numero = randint(1000,5000)
                                 print(f"Valor        :${numero}")
                                 break
                             
                             elif resp ==3:
                                 print("Has salido de la seccion de certificados")
                                 break
                             
                             elif opc ==4:
                                 print("Has salido de nuestro menu")
                                 break
                
        
                                 
                                 
             
        
                
                
                
               
            
        
             
            
          