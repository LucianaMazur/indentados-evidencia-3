def listar_usuarios_con_roles(usuarios):
    print("\n--- Lista de Usuarios Registrados con Roles ---")
    if not usuarios:
        print("⚠️ No hay usuarios registrados.")
        return

    print(f"{'Nombre':<20} | {'Email':<30} | {'Rol':<10}")
    print("-" * 65)
    for usuario in usuarios:
        print(
            f"{usuario['nombre']:<20} | {usuario['email']:<30} | {usuario['rol']:<10}")


def modificar_rol_usuario(usuarios, usuario_logueado):
    print("\n--- Modificar Rol de Usuario ---")
    listar_usuarios_con_roles(usuarios)

    nombre_a_modificar = input(
        "\nIngrese el nombre del usuario al que quiere cambiar el rol: ").strip()

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

    while True:
        nuevo_rol = input(
            "Ingrese el nuevo rol (admin/estandar): ").strip().lower()
        if nuevo_rol in ["admin", "estandar"]:
            break
        print("❌ Rol inválido. Intente nuevamente.")

    usuario_encontrado["rol"] = nuevo_rol
    print(
        f"✅ Rol de '{usuario_encontrado['nombre']}' modificado a '{nuevo_rol}'.")


def menu_gestion_usuarios(usuarios, usuario_logueado):
    while True:
        print("\n" + "="*35)
        print("» Gestión de Usuarios «".center(35))
        print("="*35)
        print("1. Listar usuarios")
        print("2. Modificar rol de un usuario")
        print("3. Volver")
        print("="*35)
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            listar_usuarios_con_roles(usuarios)
        elif opcion == "2":
            modificar_rol_usuario(usuarios, usuario_logueado)
        elif opcion == "3":
            break
        else:
            print("\n❌ Opción inválida. Intente nuevamente.\n")


def registrar_usuario(usuarios):
    print("\n" + "="*30)
    print("» Registro de Usuario «".center(30))
    print("="*30)

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
    print(f"\n✅ Usuario '{nombre}' registrado exitosamente.")
    print("="*30)

    return nuevo_usuario


def datos_personales(usuario):
    print("\n" + "="*30)
    print("» Datos Personales «".center(30))
    print("="*30)
    for clave, valor in usuario.items():
        if clave != "dispositivos":
            print(f"{clave.capitalize():<12}: {valor}")
    print("="*30)


def resumen_sistema(usuarios, dispositivos):
    print("\n" + "="*40)
    print("» Resumen del Sistema «".center(40))
    print("="*40)

    total_usuarios = len(usuarios)
    admins = sum(1 for u in usuarios if u["rol"] == "admin")
    estandar = total_usuarios - admins

    print(f"{'Usuarios registrados:':<25} {total_usuarios:>10}")
    print(f"{'Usuarios admin:':<25} {admins:>10}")
    print(f"{'Usuarios estándar:':<25} {estandar:>10}")
    print("-"*40)

    total_dispositivos = len(dispositivos)
    encendidos = sum(1 for d in dispositivos if d["estado"] == "encendido")
    esenciales = sum(1 for d in dispositivos if d.get("esencial", False))
    no_esenciales = total_dispositivos - esenciales

    print(f"{'Dispositivos registrados:':<25} {total_dispositivos:>10}")
    print(f"{'Dispositivos encendidos:':<25} {encendidos:>10}")
    print(f"{'Dispositivos esenciales:':<25} {esenciales:>10}")
    print(f"{'Dispositivos no esenciales:':<25} {no_esenciales:>10}")
    print("="*40)


def cambiar_rol(usuario_logueado, usuarios):
    modificar_rol_usuario(usuarios, usuario_logueado)


def menu_usuarios(usuario, usuarios):
    menu_gestion_usuarios(usuarios, usuario)
