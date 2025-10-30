from datetime import date
from DetalleOrdenCompra import DetalleOrdenCompra

class OrdenCompra:
    _contador_numero = 1

    def __init__(self):
        self.fecha = date.today()
        self.numero = OrdenCompra._contador_numero
        OrdenCompra._contador_numero += 1
        self.listaDetalles = []
        self.total = 0

    def agregar_detalle(self, detalle):
        self.listaDetalles.append(detalle)
        self.calcular_total()

    def calcular_total(self):
        total = 0
        i = 0
        while i < len(self.listaDetalles):
            total = total + self.listaDetalles[i].subtotal
            i = i + 1
        self.total = total

    def __str__(self):
        return f"{self.fecha} {self.numero} {self.total}"
