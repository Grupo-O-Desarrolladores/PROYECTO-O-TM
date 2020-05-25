class Kaprekar():


    def constanteKaprekar(self):

        #Variable condicion booleana:
        self.condicion = True

        #Estructura de repeticion while:
        while self.condicion == True:

            #Solicitamos al Usuario que ingrese un numero:
            print()
            self.nro1 = int(input("Ingrese un numero de 4 cifras (no repetidas): "))
            self.textoNum = str(self.nro1)

            self.tupla1 = (self.textoNum)
           


            #Primer estructura condicional que evalua que el numero tenga 4 digitos:
            if self.nro1 > 999 and self.nro1 < 10000:

                #Estructuras condicionale anidadas para evaluar las interaccioes:
                if self.tupla1[0] == self.tupla1[1] and self.tupla1[1] == self.tupla1[2] and self.tupla1[2] == self.tupla1[3]:

                    print()
                    print("El numero ingresado es incorrecto. Vuelva a intentarlo")
                    self.condicion = True

                elif self.tupla1[0] == self.tupla1[1] and self.tupla1[2] == self.tupla1[3] and self.tupla1[0] == self.tupla1[3]:

                    print()
                    print("El numero ingresado es incorrecto. Vuelva a intentarlo")
                    self.condicion = True 
                    
                elif self.tupla1[1] == self.tupla1[2] and self.tupla1[0] == self.tupla1[3]:

                    print()
                    print("El numero ingresado es incorrecto. Vuelva a intentarlo")
                    self.condicion = True
                    
                else:
                
                    print()
                    print("El numero ingresado es Correcto.")          
                    break
                

            else:
            
                print()
                print("El numero ingresado es incorrecto. Vuelva a intentarlo.")    
                self.condicion = True

        
        #Transformo la tupla en lista y la ordenamos en forma Ascendente:
        self.lista1 = self.tupla1

        #Ordena la lista de forma Ascendente:
        self.listaAscendente = sorted(self.lista1)

        #print(self.listaAscendente[:])

        #Transformo la lista en una variable String:
        self.nrotext = "".join(self.listaAscendente)

        #Transformo el Strign en una variable numerica:
        self.nroAscendente = int(self.nrotext)

        
        #Transformo la tupla en lista y la ordenamos en forma Descendente:
        self.lista1 = self.tupla1

        #Ordena la lista de forma Descendente:
        self.listaDescendente = sorted(self.lista1, reverse = True)

        #print(self.listaDescendente[:])

        #Transformo la lista en una variable String:
        self.nrotext = "".join(self.listaDescendente)

        #Transformo el Strign en una variable numerica:
        self.nroDescendente = int(self.nrotext)

        #Comenzamos el paso de restar el numero mayor al numero menor ordenados, hasta alcanzar la constante:

        self.resultado = 0
        self.contador = 0

        #subo el codigo hasta aca Rama Fede.S

        