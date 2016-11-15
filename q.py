file = open("palabras", "r")
vocales = ['a', 'e', 'i','o','u'] 
consonantes=['b','c','d','f','g','h','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cadena=file.read()
#palabra = 'ana'
total=0

##########################################cuenta si la primera letra es vocal suma 1 si la primera es consoonante suma 2
t = list(cadena)
print t

#print t[0]

if t[0] in vocales:
	total=total+1
elif t[0] in cadena:
	total=total+2

#########################################################cuenta cuantas vocales hay en la palabra y las suma
conta=0
for letra in cadena:
	if letra in vocales:
		conta=conta+1
		
		#print conta

#print total


########################################################
contacons=0
for letra in cadena:
	if letra in consonantes:
		contacons=contacons+1
		sumaconso=contacons *2   #############################33aqui divide no multiplica
		
	
###############################################################################################
t=conta+total+sumaconso
print t

#archivo=open('total.txt','w')
#archivo.write(cadena)
#archivo.write(t)
#archivo.close()


