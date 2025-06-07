from gestiones_menus_dispositivos import (menu_dispositivos,menu_modo_ahorro)
from gestiones_usuarios import (registrar_usuario,menu_usuarios)
from gestiones_inicio import (iniciar_sesion)

# Estructuras de datos principales
usuarios = []
dispositivos = []
estados_anteriores = {}
modo_ahorro_activo = False
usuario_logueado = None

def menu_principal():
    global usuario_logueado, modo_ahorro_activo
    print("🔷 Bienvenido a SmartHome Solutions 🔷")

    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                print("\n--- Registro de Usuario ---")
                registrar_usuario(usuarios)
                print("se agrego sastifactoriamente")
            case "2":
                print("\n--- Iniciar Sesión ---")
                usuario_logueado = iniciar_sesion(usuarios)
                if usuario_logueado:
                    menu_usuario_logueado()
            case "3":
                print("¡Hasta luego!")
                break
            case _:
                print("❌ Opción inválida.")

def menu_usuario_logueado():
    global modo_ahorro_activo
    while True:
        print(f"\n=== MENÚ USUARIO ({usuario_logueado['nombre']}) ===")
        print("1. Gestionar Dispositivos")
        print("2. Automatizaciones")
        print("3. Gestionar Usuarios")
        print("4. Cerrar Sesión")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                menu_dispositivos(dispositivos)
            case "2":
                menu_automatizaciones()
            case "3":
                menu_usuarios(usuarios)
            case "4":
                print("🔒 Sesión cerrada.")
                break
            case _:
                print("❌ Opción inválida.")

def menu_automatizaciones():
    global modo_ahorro_activo
    while True:
        print("\n=== AUTOMATIZACIONES ===")
        print("1. Activar Modo Ahorro de Energía")
        print("2. Encender cafetera a las 7:00 am (demo)")
        print("3. Volver")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                modo_ahorro_activo = menu_modo_ahorro(dispositivos, estados_anteriores, modo_ahorro_activo)
            case "2":
                programar_cafetera()
            case "3":
                break
            case _:
                print("❌ Opción inválida.")

def programar_cafetera():
    for dispositivo in dispositivos:
        if dispositivo["nombre"].lower() == "cafetera":
            dispositivo["estado"] = "encendido"
            print("☕ Cafetera programada y encendida a las 7:00 am (simulado).")
            return
    print("⚠️ No se encontró una cafetera registrada.")

if __name__ == "__main__":
    menu_principal()