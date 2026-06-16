class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        return f"Código: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock}"


class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto): #hola
        if producto.codigo in self.productos:
            raise ValueError("Ya existe un producto con ese código.")

        self.productos[producto.codigo] = producto

    def buscar_producto(self, codigo):
        if codigo not in self.productos:
            raise KeyError("Producto no encontrado.")

        return self.productos[codigo]

    def listar_productos(self):
        if not self.productos:
            print("No hay productos registrados.")
            return

        print("\n--- INVENTARIO ---")
        for producto in self.productos.values():
            print(producto.mostrar_info())


class Venta:
    def __init__(self):
        self.items = []
        self.total = 0

    def agregar_item(self, producto, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")

        if cantidad > producto.stock:
            raise ValueError("Stock insuficiente.")

        subtotal = producto.precio * cantidad

        producto.stock -= cantidad

        self.items.append({
            "producto": producto.nombre,
            "cantidad": cantidad,
            "subtotal": subtotal
        })

        self.total += subtotal

    def mostrar_factura(self):
        print("\n--- FACTURA ---")

        for item in self.items:
            print(
                f"{item['producto']} | "
                f"Cantidad: {item['cantidad']} | "
                f"Subtotal: ${item['subtotal']:.2f}"
            )

        print(f"\nTOTAL A PAGAR: ${self.total:.2f}")


class TiendaVirtual:
    def __init__(self):
        self.inventario = Inventario()

    def registrar_producto(self):
        try:
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))

            producto = Producto(codigo, nombre, precio, stock)
            self.inventario.agregar_producto(producto)

            print("Producto registrado correctamente.")

        except ValueError as e:
            print("Error:", e)

    def realizar_venta(self):
        venta = Venta()

        while True:
            try:
                codigo = input("\nCódigo del producto (0 para finalizar): ")

                if codigo == "0":
                    break

                producto = self.inventario.buscar_producto(codigo)

                cantidad = int(input("Cantidad: "))

                venta.agregar_item(producto, cantidad)

                print("Producto agregado a la venta.")

            except (ValueError, KeyError) as e:
                print("Error:", e)

        if venta.items:
            venta.mostrar_factura()
        else:
            print("No se registraron productos en la venta.")

    def menu(self):
        while True:
            print("\n===== TIENDA VIRTUAL =====")
            print("1. Registrar producto")
            print("2. Ver inventario")
            print("3. Realizar venta")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            try:
                if opcion == "1":
                    self.registrar_producto()

                elif opcion == "2":
                    self.inventario.listar_productos()

                elif opcion == "3":
                    self.realizar_venta()

                elif opcion == "4":
                    print("Programa finalizado.")
                    break

                else:
                    raise ValueError("Opción inválida.")

            except ValueError as e:
                print("Error:", e)


# Programa principal
if __name__ == "__main__":
    tienda = TiendaVirtual()

    # Productos de ejemplo
    try:
        tienda.inventario.agregar_producto(
            Producto("P001", "Laptop", 2500, 10)
        )

        tienda.inventario.agregar_producto(
            Producto("P002", "Mouse", 50, 30)
        )

        tienda.inventario.agregar_producto(
            Producto("P003", "Teclado", 120, 15)
        )

    except ValueError:
        pass

    tienda.menu()