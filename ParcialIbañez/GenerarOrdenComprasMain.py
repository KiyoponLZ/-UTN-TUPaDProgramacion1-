from Producto import Producto
from DetalleOrdenCompra import DetalleOrdenCompra
from OrdenCompra import OrdenCompra

# Cargar productos desde archivo

def leer_productos(path):
    db = {}
    try:
        f = open(path, 'r', encoding='utf-8')
        lineas = f.readlines()
        f.close()
    except:
        return db

    i = 0
    while i < len(lineas):
        linea = lineas[i]
        if i == 0:
            i = i + 1
            continue
        linea = linea.strip('\n').strip('\r')
        if linea == "":
            i = i + 1
            continue
        partes = linea.split(';')
        if len(partes) < 5:
            i = i + 1
            continue
        try:
            codigo = int(partes[0])
            denominacion = partes[1]
            rubro = partes[2]
            marca = partes[3]
            precio = int(partes[4])
            p = Producto(codigo, denominacion, rubro, marca, precio)
            db[codigo] = p
        except:
            pass
        i = i + 1
    return db

ProductosDataBase = leer_productos('productos_compra.txt')

listaOrdenCompras = []

# Utilidades basicas

def input_entero(mensaje):
    while True:
        dato = input(mensaje)
        try:
            return int(dato)
        except:
            print("Ingrese un numero valido")

def si_no(mensaje):
    r = input(mensaje).strip().lower()
    if r == 's':
        return True
    return False

# Opciones del menu

def ver_ordenes():
    if len(listaOrdenCompras) == 0:
        print("No hay Ordenes de Compra cargadas")
        return
    i = 0
    while i < len(listaOrdenCompras):
        oc = listaOrdenCompras[i]
        print(str(oc.fecha) + " " + str(oc.numero) + " " + str(oc.total))
        i = i + 1

def cargar_ordenes():
    while True:
        oc = OrdenCompra()
        detalles_cargados = 0
        while True:
            codigo = input_entero("Ingrese codigo de producto: ")
            if codigo in ProductosDataBase:
                prod = ProductosDataBase[codigo]
                cant = input_entero("Ingrese cantidad (>0): ")
                if cant <= 0:
                    print("Cantidad debe ser mayor a 0")
                    continue
                det = DetalleOrdenCompra(cant, prod)
                oc.agregar_detalle(det)
                detalles_cargados = detalles_cargados + 1
            else:
                print("Codigo inexistente")
                continue
            if not si_no("Desea cargar otro detalle? (S/N): "):
                break
        if detalles_cargados == 0:
            print("Debe cargar al menos 1 detalle")
        else:
            listaOrdenCompras.append(oc)
        if not si_no("Desea cargar una nueva Orden de Compra? (S/N): "):
            break

def generar_archivo_por_numero():
    if len(listaOrdenCompras) == 0:
        print("No hay Ordenes de Compra cargadas")
        return
    nro = input_entero("Ingrese numero de Orden de Compra: ")
    oc = None
    i = 0
    while i < len(listaOrdenCompras):
        if listaOrdenCompras[i].numero == nro:
            oc = listaOrdenCompras[i]
            break
        i = i + 1
    if oc is None:
        print("La Orden de Compra con número " + str(nro) + " no existe")
        return

    print("Orden de Compra N° " + str(oc.numero))
    print("Fecha: " + str(oc.fecha))
    print("------------ Productos Comprados ------------------------")
    print("Codigo Denominacion Rubro Marca Cantidad SubTotal")
    j = 0
    while j < len(oc.listaDetalles):
        d = oc.listaDetalles[j]
        print(str(d.producto.codigo) + " " + d.producto.denominacion + " " + d.producto.rubro + " " + d.producto.marca + " " + str(d.cantidad) + " " + str(d.subtotal))
        j = j + 1
    print("TOTAL: " + str(oc.total))

    if si_no("¿Desea Generar el archivo de la Orden de Compra? Ingrese S para generar: "):
        nombre = "ordenCompra_nro_" + str(oc.numero) + ".txt"
        try:
            f = open(nombre, 'w', encoding='utf-8')
            f.write("Orden de Compra N° " + str(oc.numero) + "\n")
            f.write("Fecha: " + str(oc.fecha) + "\n")
            f.write("------------ Productos Comprados ------------------------\n")
            f.write("Codigo Denominacion Rubro Marca Cantidad SubTotal\n")
            j = 0
            while j < len(oc.listaDetalles):
                d = oc.listaDetalles[j]
                linea = str(d.producto.codigo) + " " + d.producto.denominacion + " " + d.producto.rubro + " " + d.producto.marca + " " + str(d.cantidad) + " " + str(d.subtotal) + "\n"
                f.write(linea)
                j = j + 1
            f.write("TOTAL: " + str(oc.total) + "\n")
            f.close()
            print("Archivo generado: " + nombre)
        except:
            print("No se pudo generar el archivo")

# Main loop

def menu():
    while True:
        print("a- Ver Orden de Compras Cargadas")
        print("b- Cargar 1 o más Órdenes de Compra")
        print("c- Generar Archivo Orden de Compra por numero")
        print("d- Salir")
        op = input("Opcion: ").strip().lower()
        if op == 'a':
            ver_ordenes()
        elif op == 'b':
            cargar_ordenes()
        elif op == 'c':
            generar_archivo_por_numero()
        elif op == 'd':
            break
        else:
            print("Opcion invalida")

if __name__ == '__main__':
    menu()
