
usuarios = {
    "dsrueda": {"password": "3691", "rol": "admin"},
    "jjsanchez": {"password": "0321", "rol": "cliente"},
    "pPallares": {"password": "1234", "rol": "cliente"},
}
class Auto:
    def __init__(self, marca, modelo, año, precio, imagen):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio
        self.imagen = imagen
        self.vendido = False
        self.comprador = None  # <-- Nuevo atributo

    def vender(self, comprador):
        self.vendido = True
        self.comprador = comprador  # <-- Asociar el comprador


    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año}) - ${self.precio}"

class Concesionario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.inventario = []

    def agregar_auto(self, auto):
        self.inventario.append(auto)

    def mostrar_inventario(self):
        return [str(auto) for auto in self.inventario if not auto.vendido]

    def vender_auto(self, auto):
        if auto in self.inventario and not auto.vendido:
            auto.vender()
            return f"¡Felicidades! Has comprado el {auto}"
        return "El auto no está disponible o ya fue vendido."

