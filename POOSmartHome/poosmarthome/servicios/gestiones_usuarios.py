
try:
    from poosmarthome.dao.usuario_dao import UsuarioDAO
    from poosmarthome.dominio.usuario import Usuario
except Exception:
    try:
        from dao.usuario_dao import UsuarioDAO
        from dominio.usuario import Usuario
    except Exception:
        raise

dao = UsuarioDAO()

def registrar_usuario(username: str, password: str, nombre: str, email: str) -> Optional[Usuario]:
    u = Usuario(id=0, username=username, password=password, nombre=nombre, email=email)
    if not u.validar_email():
        raise ValueError("Email inválido")
    created = dao.create(u)
    return created

def login(username: str, password: str) -> Optional[Usuario]:
    u = dao.get_by_username(username)
    if u and u.password == password:
        return u
    return None

def listar_usuarios(print_output: bool = True) -> List[Usuario]:
    users = dao.list_all()
    if print_output:
        if not users:
            print("No hay usuarios registrados.")
        for u in users:
            print(f"ID:{u.id}  Username:{u.username}  Nombre:{u.nombre}  Email:{u.email}  Rol:{u.role}")
    return users

def cambiar_rol_usuario(user_id: int, nuevo_rol: str) -> Optional[Usuario]:
    u = dao.get_by_id(user_id)
    if not u:
        print("Usuario no encontrado.")
        return None
    if nuevo_rol not in ("standard", "admin"):
        print("Rol inválido.")
        return None
    u.role = nuevo_rol
    dao.update(u)
    print("Rol actualizado.")
    return u

def eliminar_usuario(user_id: int) -> bool:
    ok = dao.delete(user_id)
    if ok:
        print("Usuario eliminado.")
    else:
        print("Usuario no encontrado.")
    return ok

__all__ = [
    "registrar_usuario",
    "login",
    "listar_usuarios",
    "cambiar_rol_usuario",
    "eliminar_usuario",
]
