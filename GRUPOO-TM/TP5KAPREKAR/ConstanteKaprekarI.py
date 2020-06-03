class Kaprekar:
    # Función para tomar por el usuario la cantidad de casos de estudio
    def entrada(self):
        iteraciones = int(input("Ingrese número de casos de prueba: "))

        print("Ingrese un numero de 4 cifras (al menos 2 dígitos diferentes)")
        for i in range(iteraciones):
            Kaprekar.constanteKaprekar(self)

    # Esta función se encarga de devolver los dos números correctos en caso de que el parámetro sea menor a 1000
    def completar_cifras(num):
        num1 = ''.join(sorted(num.zfill(4)))
        num2 = ''.join(sorted(num.zfill(4), reverse=True))
        menor = int(num1)
        mayor = int(num2)
        return [menor, mayor]

    def constanteKaprekar(self):

        # Variable condicion booleana:
        self.condicion = True
        self.repdigit = False
        self.menos_de_cuatro_cifras = False
        self.es_krapekar = False
        # Variables utilizadas para restar los números y calcular cantidad de iteraciones
        self.contador = 0
        self.resultado = 0

        # Estructura de repeticion while:
        while self.condicion == True:

            # Solicitamos al Usuario que ingrese un numero:
            self.nro1 = int(input("\nIngreso: "))
            self.textoNum = str(self.nro1)
            
            self.tupla1 = (self.textoNum)

            # Primer estructura condicional que evalua que el numero tenga 4 digitos:
            if self.nro1 > 999 and self.nro1 < 10000:

                # Estructuras condicionale anidadas para evaluar las interacciones:
                if self.tupla1[0] == self.tupla1[1] and self.tupla1[1] == self.tupla1[2] and self.tupla1[2] == \
                        self.tupla1[3]:

                    self.contador = 8
                    self.repdigit = True
                    break

                elif self.tupla1[0] == self.tupla1[1] and self.tupla1[2] == self.tupla1[3] and self.tupla1[0] == \
                        self.tupla1[3]:

                    print()
                    print("El numero ingresado es incorrecto. Vuelva a intentarlo")
                    self.condicion = True

                elif self.tupla1[1] == self.tupla1[2] and self.tupla1[0] == self.tupla1[3]:

                    print()
                    print("El numero ingresado es incorrecto. Vuelva a intentarlo")
                    self.condicion = True

                else:
                    if self.nro1 == 6174:
                        self.es_krapekar = True
                    """print()
                    print("El numero ingresado es Correcto.")"""
                    break

            # Sino si es un número entre 1 y 999 inclusive
            elif self.nro1 > 0 and self.nro1 < 1000:
                self.menos_de_cuatro_cifras = True
                break

            else:

                print()
                print("El numero ingresado es incorrecto. Vuelva a intentarlo.")
                self.condicion = True

        # En caso de no ser un numero con digitos repetidos o la constante de Krapekar
        if self.repdigit is False and self.es_krapekar is False:

            # Si no es un número menor a 1000
            if not self.menos_de_cuatro_cifras:

                # Transformo la tupla en lista y la ordenamos en forma Ascendente:
                self.lista1 = self.tupla1

                # Ordena la lista de forma Ascendente:
                self.listaAscendente = sorted(self.lista1)

                # print(self.listaAscendente[:])

                # Transformo la lista en una variable String:
                self.nrotext = "".join(self.listaAscendente)

                # Transformo el Strign en una variable numerica:
                self.nroAscendente = int(self.nrotext)

                # Transformo la tupla en lista y la ordenamos en forma Descendente:
                self.lista1 = self.tupla1

                # Ordena la lista de forma Descendente:
                self.listaDescendente = sorted(self.lista1, reverse=True)

                # print(self.listaDescendente[:])

                # Transformo la lista en una variable String:
                self.nrotext = "".join(self.listaDescendente)

                # Transformo el Strign en una variable numerica:
                self.nroDescendente = int(self.nrotext)

            # subo el codigo hasta aca Rama Fede.S

            # Si es número menor a 1000
            else:
                self.numeros = Kaprekar.completar_cifras(self.tupla1)
                self.nroAscendente = self.numeros[0]
                self.nroDescendente = self.numeros[1]

            # Comenzamos el paso de restar el numero mayor al numero menor ordenados, hasta alcanzar la constante:
            while True:
                if self.resultado != 6174:
                    # Si el resultado es menor a 1000
                    if self.resultado <= 999 and self.resultado is not 0:
                        self.numeros = Kaprekar.completar_cifras(str(self.resultado))
                        self.nroAscendente = self.numeros[0]
                        self.nroDescendente = self.numeros[1]
                    # Condicion para gestionar la resta de numero ingreso ascendente - descendente:

                    if self.nroAscendente < self.nroDescendente:

                        self.resultado = self.nroDescendente - self.nroAscendente
                        """print()
                        print(self.nroDescendente, " - ", self.nroAscendente, " = ", self.resultado)"""


                    else:

                        self.resultado = self.nroAscendente - self.nroDescendente
                        """print()
                        print(self.nroAscendente, " - ", self.nroDescendente, " = ", self.resultado)"""
                    # El valor obtenido en resultado debo volver a aplicar Ascendente y Descendente:

                    self.nroAscendente = 0
                    self.nroDescendente = 0

                    self.textoNum2 = str(self.resultado)

                    self.tupla2 = (self.textoNum2)

                    # Transformo la tupla en lista y la ordenamos en forma Ascendente:
                    self.lista2 = self.tupla2

                    # Ordena la lista de forma Ascendente:
                    self.listaAscendente2 = sorted(self.lista2)
                    # subo el codigo hasta aca Rama2 Bruno

                    # print(self.listaAscendente2[:])

                    # Transformo la lista en una variable String:
                    self.textoNum2 = "".join(self.listaAscendente2)

                    # Transformo el Strign en una variable numerica:
                    self.nroAscendente = int(self.textoNum2)

                    # Transformo la tupla en lista y la ordenamos en forma Descendente:
                    self.lista2 = self.tupla2

                    # Ordena la lista de forma Descendente:
                    self.listaDescendente2 = sorted(self.lista2, reverse=True)

                    # print(self.listaDescendente2[:])

                    # Transformo la lista en una variable String:
                    self.textoNum3 = "".join(self.listaDescendente2)

                    # Transformo el Strign en una variable numerica:
                    self.nroDescendente = int(self.textoNum3)

                    self.contador = self.contador + 1

                else:
                    print(f"Salida: {self.contador}")
                    break

        # Si es la constante de Krapekar, entonces se devuelve 0
        elif self.es_krapekar:
            print(f"Salida: {self.contador}")

        # Si es un repdigit no se puede aplicar Krapekar y se devuelve 8
        else:
            print(f"Salida: {self.contador}")


miConstante = Kaprekar()

while True:

    try:

        miConstante.entrada()
        print()
        print("Programa terminado.")
        break

    except ValueError:

        print()
        print("Error. No se puede ingresar texto.")

        # subo el codigo hasta aca Rama3 Juan