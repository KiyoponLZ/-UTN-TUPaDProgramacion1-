class Producto:
    def __init__(self, codigo, denominacion, rubro, marca, precio_compra):
        self.codigo = codigo
        self.denominacion = denominacion
        self.rubro = rubro
        self.marca = marca
        self.precio_compra = precio_compra

    def __str__(self):
        return f"{self.codigo};{self.denominacion};{self.rubro};{self.marca};{self.precio_compra}"
