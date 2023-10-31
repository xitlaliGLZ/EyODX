#Listas Practicas 1
Itic3 =  ["Xitlali Gonzalez", "Aylin Martinez Santos", "Emmanuel de Jesus Esparza", "Maria Fernanda Pantoja", "Zuleyma de Jesus Manzano "]
Carreras_Itpa=["Logistica","ITIC","Gestion Empresarial","Industrial","Mecatronica"]
Edades=[18,20,19,20,20,19,19,18,19,19,19,19]


#Imprimir lista

print(Carreras_Itpa)

#Imprimir el tercer campo de cada lista 
print (Carreras_Itpa[ 2])

#Agregar elementos al final de la lista 
Itic3.append('Xitlali')
print(Itic3)

#Agregar otra lista 
Itic3.extend(['Vanesa','Juan' ])
print(Itic3)

#Agregar elememnto en la posicion 5
Itic3.insert(4,'Rainer')
print(Itic3)

#Borrrar algun elemento determinado
del Edades[0]
print(Edades)

#ver el tamaño de nuestra listas
print(len(Edades))
print(len(Itic3))
print(len(Carreras_Itpa))


#Eliminar un elemento espesifico
Edades.remove(20)
print(Edades)

#ordenar elementos 
print(Edades)
Edades.sort()
print(Edades)
