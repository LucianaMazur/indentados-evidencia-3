from gestiones_usuarios import (
    registrar_usuario, menu_usuarios, datos_personales, cambiar_rol, resumen_sistema)
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
        print("\n" + "="*40)
        print("🌟  MENÚ PRINCIPAL - SMART HOME SOLUTIONS  🌟")
        print("="*40)
        print("| {:<2} | {:<30} |".format("1", "Registrarse"))
        print("| {:<2} | {:<30} |".format("2", "Iniciar sesión"))
        print("| {:<2} | {:<30} |".format("3", "Salir"))
        print("="*40)

        opcion = input("👉 Seleccione una opción: ")

        match opcion:
            case "1":
                registrar_usuario(usuarios)
            case "2":
                usuario_actual = iniciar_sesion(usuarios)
                if usuario_actual:
                    menu_usuario_actual(usuario_actual)
            case "3":
                print("\n👋 ¡Hasta luego! Gracias por usar Smart Home Solutions.")
                break
            case _:
                print("❌ Opción inválida. Por favor intente nuevamente.")


def menu_usuario_actual(usuario):
    global modo_ahorro_activo
    while True:
        print("\n" + "="*50)
        print("|{:^48}|".format(
            f" MENÚ DE {usuario['nombre'].upper()} ({usuario['rol'].upper()}) "))
        print("="*50)
        print("| {:<2} | {:<43} |".format("1", "Ver mis datos"))
        print("| {:<2} | {:<43} |".format("2", "Gestión de dispositivos"))
        print("| {:<2} | {:<43} |".format("3", "Automatizaciones"))

        if usuario["rol"] == "admin":
            print("| {:<2} | {:<43} |".format("4", "Ver usuarios registrados"))
            print("| {:<2} | {:<43} |".format("5", "Ver resumen del sistema"))
            print("| {:<2} | {:<43} |".format(
                "6", "Cambiar rol de un usuario"))
            print("| {:<2} | {:<43} |".format("7", "Cerrar sesión"))
        else:
            print("| {:<2} | {:<43} |".format("4", "Cerrar sesión"))

        print("="*50)

        opcion = input("👉 Seleccione una opción: ")

        if usuario["rol"] == "admin":
            match opcion:
                case "1":
                    datos_personales(usuario)
                case "2":
                    menu_dispositivos(dispositivos)
                case "3":
                    modo_ahorro_activo = automatizaciones_admin(
                        dispositivos, usuario, estados_anteriores, modo_ahorro_activo)
                case "4":
                    menu_usuarios(usuario, usuarios)
                case "5":
                    resumen_sistema(usuarios, dispositivos)
                case "6":
                    cambiar_rol(usuario, usuarios)
                case "7":
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
                    modo_ahorro_activo = automatizaciones_usuario_estandar(
                        dispositivos, estados_anteriores, modo_ahorro_activo)
                case "4":
                    print("🔒 Sesión cerrada.")
                    break
                case _:
                    print("❌ Opción inválida.")


if __name__ == "__main__":
    menu_principal()
