from poosmarthome.dao.usuario_dao import UsuarioDAO
from poosmarthome.dao.dispositivo_dao import DispositivoDAO
from poosmarthome.dao.automatizacion_dao import AutomatizacionDAO
from poosmarthome.dominio.usuario import Usuario
from poosmarthome.dominio.dispositivo import Dispositivo
from poosmarthome.dominio.automatizacion import Automatizacion
from poosmarthome.conn.db_conn import DBConnection

# Inicializamos los DAOs
usuario_dao = UsuarioDAO()
dispositivo_dao = DispositivoDAO()
auto_dao = AutomatizacionDAO()


def inicializar_datos():
    if usuario_dao.get_by_username('admin') is None:
        admin = Usuario(id=0, username='admin', password='admin',
                        nombre='Administrador', email='admin@local',
                        role='admin', activo=True)
        usuario_dao.create(admin)

    if not dispositivo_dao.list_all():
        dispositivos = [
            Dispositivo(id=0, nombre='Cafetera Inteligente', tipo='electrodoméstico'),
            Dispositivo(id=0, nombre='Televisor Sala', tipo='entretenimiento'),
            Dispositivo(id=0, nombre='Luz Dormitorio', tipo='iluminación'),
        ]
        for d in dispositivos:
            dispositivo_dao.create(d)

   
    if not auto_dao.list_all():
        dispositivos = dispositivo_dao.list_all()
        auto1 = Automatizacion(id=0, nombre='Modo Ahorro', id_dispositivo=dispositivos[0].id, activa=True)
        auto2 = Automatizacion(id=0, nombre='Encender Luz', id_dispositivo=dispositivos[2].id, activa=True)
        auto_dao.create(auto1)
        auto_dao.create(auto2)


def registrar_usuario():
    print('--- Registrar usuario ---')
    username = input('Username: ')
    password = input('Password: ')
    nombre = input('Nombre completo: ')
    email = input('Email: ')
    u = Usuario(id=0, username=username, password=password,
                nombre=nombre, email=email, role='estandar', activo=True)
    if not u.validar_email():
        print('Email inválido.')
        return
    created = usuario_dao.create(u)
    print(f'Usuario creado con ID {created.id}')

def login():
    username = input('Username: ')
    password = input('Password: ')
    user = usuario_dao.get_by_username(username)
    if not user or user.password != password:
        print('Credenciales incorrectas')
        return None
    return user

def menu_standard(user: Usuario):
    while True:
        print('\n--- Menú Usuario Estándar ---')
        print('1. Ver datos personales')
        print('2. Listar dispositivos')
        print('3. Ver automatizaciones de mis dispositivos')
        print('0. Salir')
        opc = input('Opción: ')
        if opc == '1':
            print(user)
        elif opc == '2':
            devices = dispositivo_dao.list_all()
            for d in devices:
                print(d)
        elif opc == '3':
            dispositivos = dispositivo_dao.list_all()
            for d in dispositivos:
                autos = auto_dao.listar_por_dispositivo(d.id)
                if autos:
                    print(f"\nDispositivo: {d.nombre}")
                    for a in autos:
                        estado = "Activa" if a[3] else "Inactiva"
                        print(f" - {a.nombre} ({estado})")
        elif opc == '0':
            break
        else:
            print('Opción no válida')


def menu_admin(user):
    while True:
        print("\n-- Menú Admin ---")
        print("1. Listar dispositivos")
        print("2. Crear dispositivo")
        print("3. Actualizar dispositivo")
        print("4. Eliminar dispositivo")
        print("5. Listar automatizaciones")
        print("6. Crear automatización")
        print("7. Activar/Desactivar automatización")
        print("8. Eliminar automatización")
        print("9. Consultas multitabla")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            dispositivos = dispositivo_dao.list_all()
            for d in dispositivos:
                print(f"[{d.id}] {d.nombre} - {d.tipo}")

        elif opcion == "2":
            nombre = input("Nombre del dispositivo: ")
            tipo = input("Tipo del dispositivo: ")
            nuevo = Dispositivo(None, nombre, tipo)
            dispositivo_dao.create(nuevo)
            print("✅ Dispositivo creado correctamente.")

        elif opcion == "3":
            _id = int(input("ID del dispositivo a actualizar: "))
            dispositivo = dispositivo_dao.get_by_id(_id)
            if dispositivo:
                nuevo_nombre = input(f"Nuevo nombre ({dispositivo.nombre}): ") or dispositivo.nombre
                nuevo_tipo = input(f"Nuevo tipo ({dispositivo.tipo}): ") or dispositivo.tipo
                dispositivo.nombre = nuevo_nombre
                dispositivo.tipo = nuevo_tipo
                dispositivo_dao.update(dispositivo)
                print("✅ Dispositivo actualizado.")
            else:
                print("❌ No se encontró el dispositivo.")

        elif opcion == "4":
            _id = int(input("ID del dispositivo a eliminar: "))
            dispositivo_dao.delete(_id)

        elif opcion == "5":
            automatizaciones = auto_dao.list_all()
            if not automatizaciones:
                print("⚠️ No hay automatizaciones registradas.")
            else:
                for a in automatizaciones:
                    estado = "Activa" if a.activa else "Inactiva"
                    print(f"[{a.id}] {a.nombre} - Dispositivo ID: {a.id_dispositivo} ({estado})")

        elif opcion == "6":
            nombre = input("Nombre de la automatización: ")
            dispositivos = dispositivo_dao.list_all()
            if not dispositivos:
                print("⚠️ No hay dispositivos disponibles.")
            else:
                for d in dispositivos:
                    print(f"[{d.id}] {d.nombre}")
                id_disp = int(input("Seleccioná el ID del dispositivo: "))
                nueva_auto = Automatizacion(id=0, nombre=nombre, id_dispositivo=id_disp, activa=True)
                auto_dao.create(nueva_auto)
                print("✅ Automatización creada correctamente.")

        elif opcion == "7":
            id_auto = int(input("ID de la automatización: "))
            nuevo_estado = input("Activar (1) / Desactivar (0): ")
            activo = True if nuevo_estado == "1" else False
            auto_dao.cambiar_estado(id_auto, activo)
            print("✅ Estado actualizado.")

        elif opcion == "8":
            id_auto = int(input("ID de la automatización a eliminar: "))
            auto_dao.delete(id_auto)
            print("✅ Automatización eliminada.")

        elif opcion == "9":
            # Ejemplo de consulta multitabla: listar dispositivos con sus automatizaciones
            print("\n--- Dispositivos con sus automatizaciones ---")
            dispositivos = dispositivo_dao.list_all()
            for d in dispositivos:
                autos = auto_dao.listar_por_dispositivo(d.id)
                if autos:
                    print(f"{d.nombre}:")
                    for a in autos:
                        estado = "Activa" if a[3] else "Inactiva"
                        print(f" - {a.nombre} ({estado})")

        elif opcion == "0":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción inválida.")


def main():
    try:
        inicializar_datos()
        while True:
            print('\n--- POOSmartHome ---')
            print('1. Registrar usuario')
            print('2. Iniciar sesión')
            print('0. Salir')
            opc = input('Opción: ')
            if opc == '1':
                registrar_usuario()
            elif opc == '2':
                user = login()
                if user:
                    if user.role == 'admin':
                        menu_admin(user)
                    else:
                        menu_standard(user)
            elif opc == '0':
                break
            else:
                print('Opción no válida')
    finally:
        DBConnection().close()


if __name__ == '__main__':
    main()
