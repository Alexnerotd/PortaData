#CAJERO QUE PARTE DE UN SALDO DE $1000

print(".:Menu.:")
saldo = 1000
print("1.Si desea depositar a su cuenta")
print("2.Si desea retirar de su cuenta")
print("3.Si desea revisar el saldo de su cuenta")
print("4.Si desea salir")
print()
opcion = int(input("Digite la accion que quiera realizar: "))
print()

if opcion==1:
    extra = float(input("Digite el dinero que quiera depositar: "))
    saldo += extra
    print(f"Su saldo ahora es de ${saldo}")
elif opcion==2:
    ret = float(input("Digite el saldo que quiera retirar: "))
    saldo -= ret
    print(f"Su saldo ahora es de ${saldo}")
elif opcion==3:
    print(f"Su saldo actual es de ${saldo}")
elif opcion==4:
    print("Gracias por usar nuestros servicios (:")

