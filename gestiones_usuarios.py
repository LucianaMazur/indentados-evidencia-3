def listar_usuarios_con_roles(usuarios):
    print("\n--- Lista de Usuarios Registrados con Roles ---")
    if not usuarios:
        print("⚠️ No hay usuarios registrados.")
        return
    for usuario in usuarios:
        print(f"- Nombre: {usuario['nombre']}, Email: {usuario['email']}, Rol: {usuario['rol']}")


def modificar_rol_usuario(usuarios, usuario_logueado):
    listar_usuarios_con_roles(usuarios)
    nombre_a_modificar = input("Ingrese el nombre del usuario al que quiere cambiar el rol: ").strip()

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["nombre"].lower() == nombre_a_modificar.lower():
            usuario_encontrado = usuario
            break

    if usuario_encontrado is None:
        print("⚠️ Usuario no encontrado.")
        return

    if usuario_encontrado["nombre"] == usuario_logueado["nombre"]:
        print("⚠️ No puedes modificar tu propio rol.")
        return

    nuevo_rol = input("Ingrese el nuevo rol (admin/estandar): ").strip().lower()
    if nuevo_rol not in ["admin", "estandar"]:
        print("❌ Rol inválido. Solo 'admin' o 'estandar' son válidos.")
        return

    usuario_encontrado["rol"] = nuevo_rol
    print(f"✅ Rol de {usuario_encontrado['nombre']} modificado a '{nuevo_rol}'.")


def menu_gestion_usuarios(usuarios, usuario_logueado):
    while True:
        print("\n--- Gestión de Usuarios ---")
        print("1. Listar usuarios")
        print("2. Modificar rol de un usuario")
        print("3. Volver")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar_usuarios_con_roles(usuarios)
        elif opcion == "2":
            modificar_rol_usuario(usuarios, usuario_logueado)
        elif opcion == "3":
            break
        else:
            print("❌ Opción inválida.")


def registrar_usuario(usuarios):
    print("\n--- Registro de Usuario ---")
    nombre = input("Ingrese su nombre: ").strip()
    email = input("Ingrese su correo electrónico: ").strip()
    
    while True:
        contraseña = input("Ingrese una contraseña: ").strip()
        confirmar = input("Confirme su contraseña: ").strip()
        if contraseña != confirmar:
            print("❌ Las contraseñas no coinciden. Intente nuevamente.")
        elif not contraseña:
            print("❌ La contraseña no puede estar vacía.")
        else:
            break

    rol = input("Ingrese su rol (admin/estandar): ").strip().lower()
    if rol not in ["admin", "estandar"]:
        print("❌ Rol inválido. Se asignará 'estandar' por defecto.")
        rol = "estandar"

    nuevo_usuario = {
        "nombre": nombre,
        "email": email,
        "contraseña": contraseña,
        "rol": rol,
        "dispositivos": []
    }

    usuarios.append(nuevo_usuario)
    print(f"✅ Usuario '{nombre}' registrado exitosamente.")
    return nuevo_usuario
    
def datos_personales(usuario):
    print("\n--- Datos Personales ---")
    for clave, valor in usuario.items():
        if clave != "dispositivos":
            print(f"{clave.capitalize()}: {valor}")


def cambiar_rol(usuario_logueado, usuarios):
    modificar_rol_usuario(usuarios, usuario_logueado)


def menu_usuarios(usuario, usuarios):
    menu_gestion_usuarios(usuarios, usuario)
