class libro:
    codigo_libro=''
    nombre=''
    precio=0
    categoria=''
    titulo=''
    autor=''
    pais=''

    def _int_(self):
        self.codigo_libro='aa111'
        self.categoria=''
        self.titulo='Aventuras del pepe'
        self.autor='Garcia Marquez'
        self.nombre='S/N'
        self.precio=35000



    def setCodigo_libro(self, codigo):
        if len(codigo) >=0 and len(codigo)<=7:
            self.codigo_libro = codigo
            return True
        else:
            print("Largo de codigo incorrecto, debe tener entre  caracteres")
            return False


    def setPrecio(self,precio):
        if precio >= 10000 and precio <= 150000:
            self.precio = precio
            return True
        else:
            print("el precio debe estar entre 10000 y 150000")
            return False
