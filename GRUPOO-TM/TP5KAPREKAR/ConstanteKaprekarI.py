#print(self.listaAscendente2[:])

            #Transformo la lista en una variable String:
                self.textoNum2 = "".join(self.listaAscendente2)

            #Transformo el Strign en una variable numerica:
                self.nroAscendente = int(self.textoNum2)

        
            #Transformo la tupla en lista y la ordenamos en forma Descendente:
                self.lista2 = self.tupla2

            #Ordena la lista de forma Descendente:
                self.listaDescendente2 = sorted(self.lista2, reverse = True)

                #print(self.listaDescendente2[:])

            #Transformo la lista en una variable String:
                self.textoNum3 = "".join(self.listaDescendente2)

            #Transformo el Strign en una variable numerica:
                self.nroDescendente = int(self.textoNum3)
      
                self.contador = self.contador + 1    
            
            else:
                print()
                print("Se alcanzo la constante de Kaprekar. En ", self.contador, " ciclos.")
                break        



miConstante = Kaprekar()

while True:

    try:

        miConstante.constanteKaprekar()
        print()
        print("Programa terminado.")
        break

    except ValueError:

        print()
        print("Error. No se puede ingresar texto.")    

#subo el codigo hasta aca Rama3 Juan
        
