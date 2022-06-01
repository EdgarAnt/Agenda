#Agenda
#Practica05
#Delgadillo Villegas Edgar Antonio
import os

while True:
    os.system("cls")
    print(" Agenda ")
    arch_orig = open("Agenda.txt","r")
    arch_r = open("agenda_resp.txt","w")

    for l in arch_orig:
        arch_r.write(l)

    arch_orig.close()
    arch_r.close()
    arch_r = open("agenda_resp.txt","r")
    arch_orig = open("agenda_original.txt","w")

    print("----------------------------")
    print("            Agenda:           ")
    print("-----------------------------")
    name = input("nombre del alumno: ")
    tel = input("Telefono del alumno: ")
    car = input("Carrera del alumno: ")
    code = input("codigo del alumno: ")


    a = arch_r.read()
    questions = a + "\n" + name + "\t\t" + tel + "\t" + car + "\t\t" + code
    arch_orig.write(questions)
    arch_orig.close()
    arch_r.close()
    opc = input("Deseas añadir a mas personas? s/n ")

    if opc == 'n':
        os.system("cls")
        print("\n\nHasta luego :D")
        break
