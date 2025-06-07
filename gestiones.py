
def registrar_usuario(usuarios):
    print("\n--- Registro de Usuario ---")
    nombre = input("Nombre: ")
    email = input("Email: ")
    contraseña = input("Contraseña: ")

    for usuario in usuarios:
        if usuario["email"] == email:
            print("⚠️ Ya existe un usuario con ese email.")
            return

    nuevo_usuario = {
        "nombre": nombre,
        "email": email,
        "contraseña": contraseña,
    }

    usuarios.append(nuevo_usuario)
    print(f"✅ Usuario {nombre} registrado con éxito.")


def iniciar_sesion(usuarios):
    print("\n--- Iniciar Sesión ---")
    email = input("Email: ")
    contraseña = input("Contraseña: ")

    for usuario in usuarios:
        if usuario["email"] == email and usuario["contraseña"] == contraseña:
            print(f"🔓 Bienvenido/a, {usuario['nombre']}!")
            return usuario

    print("❌ Email o contraseña incorrectos.")
    return None


def menu_dispositivos(dispositivos):
    while True:
        print("\n--- Gestión de Dispositivos ---")
        print("1. Agregar dispositivo")
        print("2. Listar dispositivos")
        print("3. Cambiar estado")
        print("4. Volver")
        opcion = input("Opción: ")

        match opcion:
            case "1":
                nombre = input("Nombre del dispositivo: ")
                es_esencial = input("¿Es esencial? (s/n): ").lower() == "s"
                dispositivos.append({"nombre": nombre, "estado": "apagado", "esencial": es_esencial})
                print("✅ Dispositivo agregado.")
            case "2":
                for d in dispositivos:
                    print(f"- {d['nombre']} ({'esencial' if d['esencial'] else 'no esencial'}) - {d['estado']}")
            case "3":
                nombre = input("Nombre del dispositivo: ")
                for d in dispositivos:
                    if d["nombre"].lower() == nombre.lower():
                        nuevo_estado = input("Nuevo estado (encendido/apagado): ").lower()
                        if nuevo_estado in ["encendido", "apagado"]:
                            d["estado"] = nuevo_estado
                            print(f"🔄 Estado de {d['nombre']} actualizado.")
                        else:
                            print("⚠️ Estado inválido.")
                        break
                else:
                    print("⚠️ Dispositivo no encontrado.")
            case "4":
                break
            case _:
                print("❌ Opción inválida.")


def menu_usuarios(usuarios):
    print("\n--- Lista de Usuarios Registrados ---")
    if not usuarios:
        print("⚠️ No hay usuarios registrados.")
    for usuario in usuarios:
        print(f"- {usuario['nombre']} ({usuario['email']})")


def menu_modo_ahorro(dispositivos, estados_anteriores, modo_ahorro_activo):
    if not modo_ahorro_activo:
        apagados = 0
        estados_anteriores.clear()
        for d in dispositivos:
            if not d.get("esencial", False) and d["estado"] == "encendido":
                estados_anteriores[d["nombre"]] = d["estado"]
                d["estado"] = "apagado"
                apagados += 1
        print(f"💡 Modo Ahorro ACTIVADO. Se apagaron {apagados} dispositivos no esenciales.")
        return True
    else:
        restaurados = 0
        for d in dispositivos:
            if d["nombre"] in estados_anteriores:
                d["estado"] = estados_anteriores[d["nombre"]]
                restaurados += 1
        estados_anteriores.clear()
        print(f"🔋 Modo Ahorro DESACTIVADO. Se restauraron {restaurados} dispositivos.")
        return False
