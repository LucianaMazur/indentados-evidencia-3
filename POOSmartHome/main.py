from poosmarthome.dao.usuario_dao import UsuarioDAO
from poosmarthome.dao.dispositivo_dao import DispositivoDAO
from poosmarthome.dao.automatizacion_dao import AutomatizacionDAO
from poosmarthome.dominio.usuario import Usuario
from poosmarthome.dominio.dispositivo import Dispositivo
from poosmarthome.dominio.automatizacion import Automatizacion
from poosmarthome.conn.db_conn import DBConnection

# Inicializar DAOs
usuario_dao = UsuarioDAO()
dispositivo_dao = DispositivoDAO()
automatizacion_dao = AutomatizacionDAO()

def inicializar_datos():
    # Crear usuario admin si no existe
    if usuario_dao.get_by_username('admin') is None:
        admin = Usuario(id=0, username='admin', password='admin123',
                       nombre='Administrador', email='admin@smarthome.com',
                       role='admin', activo=True)
        usuario_dao.create(admin)
        print("Usuario admin creado (username: admin, password: admin123)")

def registrar_usuario():
    # Registrar nuevo usuario estándar
    print('\n--- Registrar Nuevo Usuario ---')
    username = input('Username: ')
    
    if usuario_dao.get_by_username(username):
        print('El username ya existe.')
        return
    
    usuario = Usuario(id=0, username=username, password=input('Password: '),
                     nombre=input('Nombre completo: '), email=input('Email: '),
                     role='standard', activo=True)
    
    if not usuario.validar_email():
        print('Email inválido.')
        return
    
    usuario_dao.create(usuario)
    print(f'Usuario registrado con ID {usuario.id}')


def login():
    # Iniciar sesión
    print('\n--- Iniciar Sesion ---')
    username = input('Username: ')
    password = input('Password: ')
    user = usuario_dao.get_by_username(username)
    
    if not user or user.password != password:
        print('Credenciales incorrectas')
        return None
    
    if not user.es_activo():
        print('Usuario inactivo.')
        return None
    
    print(f'Bienvenido {user.nombre}!')
    return user

def mostrar_automatizaciones():
    # Mostrar todas las automatizaciones
    automatizaciones = automatizacion_dao.list_all()
    if not automatizaciones:
        print('No hay automatizaciones registradas.')
        return []
    
    dispositivos = {d.id: d for d in dispositivo_dao.list_all()}
    for auto in automatizaciones:
        estado = "Activa" if auto.activa else "Inactiva"
        disp_nombre = dispositivos.get(auto.id_dispositivo).nombre if auto.id_dispositivo in dispositivos else "Desconocido"
        print(f'[{auto.id}] {auto.nombre} - {disp_nombre} - {estado}')
    return automatizaciones

def menu_standard(user):
    # Menú para usuarios estandar
    while True:
        print(f'\n--- Menu Usuario Estandar ({user.username}) ---')
        print('1. Ver mis datos personales')
        print('2. Consultar dispositivos')
        print('3. Ver automatizaciones')
        print('0. Cerrar sesión')
        
        opcion = input('Opción: ')
        
        if opcion == '1':
            print(f'\n--- Mis Datos ---\nID: {user.id}\nUsername: {user.username}\n'
                  f'Nombre: {user.nombre}\nEmail: {user.email}\nRol: {user.role}')
        
        elif opcion == '2':
            print('\n--- Lista de Dispositivos ---')
            dispositivos = dispositivo_dao.list_all()
            if not dispositivos:
                print('No hay dispositivos.')
            else:
                for d in dispositivos:
                    print(f'[{d.id}] {d.nombre} - {d.tipo}')
        
        elif opcion == '3':
            print('\n--- Automatizaciones ---')
            mostrar_automatizaciones()
        
        elif opcion == '0':
            print('Cerrando sesion...')
            break
        else:
            print('Opcion invalida.')

def gestionar_dispositivos():
    # Gestión de dispositivos
    print('\n1. Listar | 2. Crear | 3. Actualizar | 4. Eliminar | 0. Volver')
    op = input('Opcion: ')
    
    if op == '1':
        print('\n--- Dispositivos ---')
        for d in dispositivo_dao.list_all():
            print(f'[{d.id}] {d.nombre} - {d.tipo}')
    
    elif op == '2':
        nuevo = Dispositivo(id=0, nombre=input('Nombre: '), tipo=input('Tipo: '))
        dispositivo_dao.create(nuevo)
        print(f'Dispositivo creado (ID: {nuevo.id})')
    
    elif op == '3':
        try:
            d = dispositivo_dao.get_by_id(int(input('ID del dispositivo: ')))
            if not d:
                print('No encontrado.')
                return
            print(f'Actual: {d.nombre} - {d.tipo}')
            nuevo_nombre = input('Nuevo nombre (Enter=mantener): ')
            nuevo_tipo = input('Nuevo tipo (Enter=mantener): ')
            if nuevo_nombre: d.nombre = nuevo_nombre
            if nuevo_tipo: d.tipo = nuevo_tipo
            dispositivo_dao.update(d)
            print('Actualizado.')
        except ValueError:
            print('ID invalido.')
    
    elif op == '4':
        try:
            id_disp = int(input('ID a eliminar: '))
            d = dispositivo_dao.get_by_id(id_disp)
            if not d:
                print('No encontrado.')
                return
            if input(f'¿Eliminar {d.nombre}? (s/n): ').lower() == 's':
                dispositivo_dao.delete(id_disp)
                print('Eliminado (automatizaciones tambien).')
        except ValueError:
            print('ID inválido.')

def gestionar_automatizaciones():
    # Gestión de automatizaciones
    print('\n1. Listar | 2. Crear | 3. Activar/Desactivar | 4. Eliminar | 0. Volver')
    op = input('Opcion: ')
    
    if op == '1':
        print('\n--- Automatizaciones ---')
        mostrar_automatizaciones()
    
    elif op == '2':
        dispositivos = dispositivo_dao.list_all()
        if not dispositivos:
            print('No hay dispositivos. Crea uno primero.')
            return
        
        print('\n--- Dispositivos ---')
        for d in dispositivos:
            print(f'[{d.id}] {d.nombre}')
        
        try:
            nombre = input('Nombre automatizacion: ')
            id_disp = int(input('ID dispositivo: '))
            if not dispositivo_dao.get_by_id(id_disp):
                print('Dispositivo no encontrado.')
                return
            activa = input('¿Activa? (s/n): ').lower() != 'n'
            nueva = Automatizacion(id=0, nombre=nombre, id_dispositivo=id_disp, activa=activa)
            automatizacion_dao.create(nueva)
            print(f'Creada (ID: {nueva.id})')
        except ValueError:
            print('ID invalido.')
    
    elif op == '3':
        autos = mostrar_automatizaciones()
        if not autos:
            return
        try:
            auto = automatizacion_dao.get_by_id(int(input('ID: ')))
            if not auto:
                print('No encontrada.')
                return
            print(f'Estado actual: {"activa" if auto.activa else "inactiva"}')
            print('1. Activar | 2. Desactivar')
            if input('Opción: ') == '1':
                auto.activar()
            else:
                auto.desactivar()
            automatizacion_dao.update(auto)
            print('Estado actualizado.')
        except ValueError:
            print('ID invalido.')
    
    elif op == '4':
        autos = mostrar_automatizaciones()
        if not autos:
            return
        try:
            id_auto = int(input('ID a eliminar: '))
            auto = automatizacion_dao.get_by_id(id_auto)
            if not auto:
                print('No encontrada.')
                return
            if input(f'¿Eliminar {auto.nombre}? (s/n): ').lower() == 's':
                automatizacion_dao.delete(id_auto)
                print('Eliminada.')
        except ValueError:
            print('ID invalido.')

def menu_admin(user):
    # Menú para administradores
    while True:
        print(f'\n--- Menu Admin ({user.username}) ---')
        print('1. Gestionar Dispositivos')
        print('2. Gestionar Automatizaciones')
        print('3. Cambiar rol de usuario')
        print('0. Cerrar sesión')
        
        opcion = input('Opción: ')
        
        if opcion == '1':
            gestionar_dispositivos()
        
        elif opcion == '2':
            gestionar_automatizaciones()
        
        elif opcion == '3':
            print('\n--- Usuarios ---')
            for u in usuario_dao.list_all():
                print(f'[{u.id}] {u.username} - {u.nombre} - {u.role}')
            
            try:
                usuario = usuario_dao.get_by_id(int(input('ID: ')))
                if not usuario:
                    print('No encontrado.')
                    continue
                print(f'Rol actual: {usuario.role}')
                print('1. Admin | 2. Standard')
                usuario.role = 'admin' if input('Opcion: ') == '1' else 'standard'
                usuario_dao.update(usuario)
                print('Rol actualizado.')
            except ValueError:
                print('ID invalido.')
        
        elif opcion == '0':
            print('Cerrando sesión...')
            break
        else:
            print('Opción invalida.')

def main():
    # Función principal
    inicializar_datos()
    while True:
        print('\n========================================')
        print('     SISTEMA SMART HOME - POO')
        print('========================================')
        print('1. Registrar usuario')
        print('2. Iniciar sesion')
        print('0. Salir')
        
        opcion = input('Opcion: ')
        
        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            user = login()
            if user:
                menu_admin(user) if user.is_admin() else menu_standard(user)
        elif opcion == '0':
            print('Chau!!!')
            break
        else:
            print('Opcion invalida.')

if __name__ == "__main__":
    main()
