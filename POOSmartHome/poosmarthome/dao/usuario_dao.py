from poosmarthome.dao.interfaces.i_usuario_dao import IUsuarioDAO
from poosmarthome.dominio.usuario import Usuario
from poosmarthome.conn.db_conn import DBConnection

class UsuarioDAO(IUsuarioDAO):
    """Gestión de usuarios en la BD"""

    def create(self, usuario):
        try:
            with DBConnection().cursor() as cur:
                cur.execute(
                    "INSERT INTO usuarios (username, password, nombre, email, role, activo) "
                    "VALUES (%s, %s, %s, %s, %s, %s)",
                    (usuario.username, usuario.password, usuario.nombre,
                     usuario.email, usuario.role, int(usuario.activo))
                )
                DBConnection().get_connection().commit()
                usuario.id = cur.lastrowid
            return usuario
        except Exception as e:
            print(f"Error creando usuario: {e}")
            DBConnection().get_connection().rollback()
            return None

    def get_by_id(self, _id):
        try:
            with DBConnection().cursor() as cur:
                cur.execute("SELECT id, username, password, nombre, email, role, activo FROM usuarios WHERE id=%s", (_id,))
                row = cur.fetchone()
            return Usuario.from_row(row) if row else None
        except Exception as e:
            print(f"Error obteniendo usuario: {e}")
            return None

    def get_by_username(self, username):
        try:
            with DBConnection().cursor() as cur:
                cur.execute("SELECT id, username, password, nombre, email, role, activo FROM usuarios WHERE username=%s", (username,))
                row = cur.fetchone()
            return Usuario.from_row(row) if row else None
        except Exception as e:
            print(f"Error obteniendo usuario por username: {e}")
            return None

    def update(self, usuario):
        try:
            with DBConnection().cursor() as cur:
                cur.execute(
                    "UPDATE usuarios SET username=%s, password=%s, nombre=%s, email=%s, role=%s, activo=%s WHERE id=%s",
                    (usuario.username, usuario.password, usuario.nombre,
                     usuario.email, usuario.role, int(usuario.activo), usuario.id)
                )
                DBConnection().get_connection().commit()
            return usuario
        except Exception as e:
            print(f"Error actualizando usuario: {e}")
            DBConnection().get_connection().rollback()
            return None

    def delete(self, _id):
        try:
            with DBConnection().cursor() as cur:
                cur.execute("DELETE FROM usuarios WHERE id=%s", (_id,))
                DBConnection().get_connection().commit()
                return cur.rowcount > 0
        except Exception as e:
            print(f"Error eliminando usuario: {e}")
            DBConnection().get_connection().rollback()
            return False

    def list_all(self):
        try:
            with DBConnection().cursor() as cur:
                cur.execute("SELECT id, username, password, nombre, email, role, activo FROM usuarios")
                rows = cur.fetchall()
            return [Usuario.from_row(r) for r in rows]
        except Exception as e:
            print(f"Error listando usuarios: {e}")
            return []
