from gestiones_usuarios import (registrar_usuario, menu_usuarios, datos_personales, cambiar_rol)
from gestiones_inicio import iniciar_sesion
from gestiones_menus_dispositivos import menu_dispositivos
from gestiones_automatizaciones import automatizaciones_usuario_estandar, automatizaciones_admin

usuarios = []
dispositivos = []
estados_anteriores = {}
modo_ahorro_activo = False


def menu_principal():
    usuario_actual = None

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                registrar_usuario(usuarios)
            case "2":
                usuario_actual = iniciar_sesion(usuarios)
                if usuario_actual:
                    menu_usuario_actual(usuario_actual)
            case "3":
                print("👋 ¡Hasta luego!")
                break
            case _:
                print("❌ Opción inválida.")


def menu_usuario_actual(usuario):
    global modo_ahorro_activo
    while True:
        print(f"\n--- Menú de {usuario['nombre']} ---")
        print("1. Ver mis datos")
        print("2. Gestión de dispositivos")
        print("3. Automatizaciones")
        if usuario["rol"] == "admin":
            print("4. Ver usuarios registrados")
            print("5. Cambiar rol de un usuario")
            print("6. Cerrar sesión")
        else:
            print("4. Cerrar sesión")

        opcion = input("Seleccione una opción: ")

        if usuario["rol"] == "admin":
            match opcion:
                case "1":
                    datos_personales(usuario)
                case "2":
                    menu_dispositivos(dispositivos)
                case "3":
                    modo_ahorro_activo = automatizaciones_admin(dispositivos, usuario, estados_anteriores, modo_ahorro_activo)
                case "4":
                    menu_usuarios(usuario, usuarios)
                case "5":
                    cambiar_rol(usuario, usuarios)
                case "6":
                    print("🔒 Sesión cerrada.")
                    break
                case _:
                    print("❌ Opción inválida.")
        else:
            match opcion:
                case "1":
                    datos_personales(usuario)
                case "2":
                    menu_dispositivos(dispositivos)
                case "3":
                    modo_ahorro_activo = automatizaciones_usuario_estandar(dispositivos, estados_anteriores, modo_ahorro_activo)
                case "4":
                    print("🔒 Sesión cerrada.")
                    break
                case _:
                    print("❌ Opción inválida.")


if __name__ == "__main__":
    menu_principal()