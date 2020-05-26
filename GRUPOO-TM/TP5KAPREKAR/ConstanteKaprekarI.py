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
        while True:
           if self.resultado != 6174:
                #Condicion para gestionar la resta de numero ingreso ascendente - descendente:

                if self.nroAscendente < self.nroDescendente:

                    self.resultado = self.nroDescendente - self.nroAscendente
                    print()
                    print(self.nroDescendente, " - ", self.nroAscendente, " = ", self.resultado)
                    

                else:
                
                    self.resultado = self.nroAscendente - self.nroDescendente
                    print()
                    print(self.nroAscendente, " - ", self.nroDescendente, " = ", self.resultado)
           #El valor obtenido en resultado debo volver a aplicar Ascendente y Descendente:

                self.nroAscendente = 0
                self.nroDescendente = 0 
            
                self.textoNum2 = str(self.resultado)

                self.tupla2 = (self.textoNum2) 

            #Transformo la tupla en lista y la ordenamos en forma Ascendente:
                self.lista2 = self.tupla2

            #Ordena la lista de forma Ascendente:
                self.listaAscendente2 = sorted(self.lista2)
        #subo el codigo hasta aca Rama Bruno.S
        