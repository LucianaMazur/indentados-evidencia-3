from gestiones_usuarios import registrar_usuario, agregar_usuario, inicio_sesion, modificar_rol
from gestiones_dispositivos import registrar_dispositivo, agregar_dispositivo, listar_dispositivos, editar_dispositivo, eliminar_dispositivo
from gestiones_automatizaciones import crear_automatizacion, activar_automatizacion, consultar_automatizacion

usuarios = []
dispositivos = []
automatizacion = crear_automatizacion("cafe_a_las_20", "cafetera", "20:00")

def menu_principal():
    print("----------------------------")
    print("Bienvenidos a la casa inteligente")
    print("----------------------------")
    opcion = int(input("1: Registrar usuario\n2: Iniciar sesión\n3: Salir\n"))
    return opcion

def menu_admin(usuario_actual):
    while True:
        print("1) Consultar automatizaciones activas\n2) Gestionar dispositivos\n3) Modificar rol de usuario\n4) Cerrar sesión")
        op_admin = int(input())
        if op_admin == 1:
            consultar_automatizacion(automatizacion)
        elif op_admin == 2:
            menu_dispositivos()
        elif op_admin == 3:
            mail_mod = input("Mail del usuario a modificar: ")
            rol_nuevo = input("Nuevo rol (administrador/estandar): ")
            if modificar_rol(usuarios, mail_mod, rol_nuevo):
                print("Rol modificado con éxito!")
            else:
                print("Usuario no encontrado")
        elif op_admin == 4:
            break

def menu_dispositivos():
    while True:
        print("1) Agregar\n2) Listar\n3) Editar\n4) Eliminar\n5) Volver")
        op_disp = int(input())
        if op_disp == 1:
            id_disp = input("ID: ")
            nombre_disp = input("Nombre: ")
            tipo_disp = input("Tipo: ")
            estado_disp = input("Estado (prendido/apagado): ")
            es_ess = input("Esencial (si/no): ")
            disp = registrar_dispositivo(id_disp, nombre_disp, tipo_disp, estado_disp, es_ess)
            agregar_dispositivo(dispositivos, disp)
        elif op_disp == 2:
            listar_dispositivos(dispositivos)
        elif op_disp == 3:
            nombre_edit = input("Nombre del dispositivo a editar: ")
            campo = input("Campo a modificar (estado/es_esencial): ")
            valor = input("Nuevo valor: ")
            if editar_dispositivo(dispositivos, nombre_edit, campo, valor):
                print("Dispositivo editado con éxito")
            else:
                print("Dispositivo no encontrado")
        elif op_disp == 4:
            nombre_elim = input("Nombre del dispositivo a eliminar: ")
            if eliminar_dispositivo(dispositivos, nombre_elim):
                print("Dispositivo eliminado")
            else:
                print("Dispositivo no encontrado")
        elif op_disp == 5:
            break

def menu_usuario(usuario_actual):
    while True:
        print("1) Consultar datos personales\n2) Consultar dispositivos\n3) Activar automatización\n4) Cerrar sesión")
        op_user = int(input())
        if op_user == 1:
            print(f"ID: {usuario_actual['id']}\nNombre: {usuario_actual['nombre']}\nMail: {usuario_actual['mail']}\nRol: {usuario_actual['rol']}")
        elif op_user == 2:
            listar_dispositivos(dispositivos)
        elif op_user == 3:
            activar_automatizacion(automatizacion)
        elif op_user == 4:
            break

# Crear primer administrador si no hay usuarios
if len(usuarios) == 0:
    print("Registrar el primer usuario (será administrador)")
    id = int(input("ID: "))
    nombre = input("Nombre: ")
    mail = input("Mail: ")
    contraseña = input("Contraseña: ")
    usuario_admin = registrar_usuario(id, nombre, mail, contraseña, rol="administrador")
    agregar_usuario(usuarios, usuario_admin)
    print("Usuario administrador creado con éxito!\n")

while True:
    opcion = menu_principal()
    if opcion == 1:
        id = int(input("ID: "))
        nombre = input("Nombre: ")
        mail = input("Mail: ")
        contraseña = input("Contraseña: ")
        usuario_creado = registrar_usuario(id, nombre, mail, contraseña)
        agregar_usuario(usuarios, usuario_creado)
        print("Usuario estándar creado con éxito!\n")
    elif opcion == 2:
        mail = input("Mail: ")
        contraseña = input("Contraseña: ")
        usuario_actual = inicio_sesion(usuarios, mail, contraseña)
        if usuario_actual:
            print(f"Bienvenido {usuario_actual['nombre']} ({usuario_actual['rol']})")
            if usuario_actual["rol"] == "administrador":
                menu_admin(usuario_actual)
            else:
                menu_usuario(usuario_actual)
        else:
            print("Usuario o contraseña incorrectos\n")
    elif opcion == 3:
        print("Gracias por la visita, que tengas un lindo día!!")
        break