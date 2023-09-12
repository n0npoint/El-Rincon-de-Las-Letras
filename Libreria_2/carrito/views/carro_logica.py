class Carrito:

    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")

        if not carro:
            carro = self.session["carro"] = {}
        
        self.carro=carro
    
    def agregar_producto(self , producto):

        if(str(producto.id_libro) not in self.carro.keys()):
            self.carro[producto.id_libro] = { 
            "id_libro": producto.id_libro,
            "id_autor": str(producto.id_autor),
            "isbn": producto.isbn,
            "titulo": producto.titulo,
            "precio": str(producto.precio_venta),
            "edicion": producto.edicion, 
            "caratula": producto.caratula.url
        }
            print ("Producto agregado al carro")
            print(producto.caratula.url)
        else:
            print ("Producto ya existe")

        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True


    def eliminar_producto(self , producto):
        producto.id_libro=str(producto.id_libro)

        if producto.id_libro in self.carro:
            del self.carro[producto.id_libro]
            self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified = True
