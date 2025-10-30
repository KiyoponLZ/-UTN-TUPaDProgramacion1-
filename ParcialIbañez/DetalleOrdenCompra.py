from Producto import Producto

class DetalleOrdenCompra:
    def __init__(self, cantidad, producto):
        self.cantidad = cantidad
        self.producto = producto
        self.subtotal = self.producto.precio_compra * self.cantidad

    def __str__(self):
        return (
            str(self.producto.codigo) + " " +
            self.producto.denominacion + " " +
            self.producto.rubro + " " +
            self.producto.marca + " " +
            str(self.cantidad) + " " +
            str(self.subtotal)
        )
