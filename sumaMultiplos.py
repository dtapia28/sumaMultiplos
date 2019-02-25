def sumaMultiplos(maximo):
	contador=0
	sumaMultiplo=0
	for i in range(1,maximo):
		for x in range(1,i+1):
			if i%x==0:
				contador +=1
		if contador==2:
			print("El número " + str(i) + " es primo")
			sumaMultiplo +=i
			contador=0
		else:
			contador=0
	print("La suma de los números primos menores a" + str(maximo) + " es " + str(sumaMultiplo))			


sumaMultiplos(400)				