class Cliente:
    def __init__(self, nombre, apellido, correo, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.direccion = direccion
        self.carrito_compras = []

    def agregar_producto(self, producto):
        self.carrito_compras.append(producto)
    
    def mostrar_carrito(self):
        print(f"Carrito de {self.nombre} {self.apellido}:")
        for producto in self.carrito_compras:
            print(f"- {producto}")
    
    def realizar_compra(self):
        total = sum(producto.precio for producto in self.carrito_compras)
        print(f"{self.nombre} {self.apellido} ha realizado una compra por un total de ${total:.2f}")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

skdfljsklfsdklfjsk
jsfjlsdfjslfklsd