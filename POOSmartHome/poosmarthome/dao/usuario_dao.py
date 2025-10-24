from typing import List, Optional
from poosmarthome.dao.interfaces.i_usuario_dao import IUsuarioDAO
from poosmarthome.dominio.usuario import Usuario
from poosmarthome.conn.db_conn import DBConnection

class UsuarioDAO(IUsuarioDAO):
    def __init__(self):
        self.conn = DBConnection().get_connection()

    def create(self, usuario: Usuario) -> Usuario:
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO usuarios (username, password, nombre, email, role, activo) VALUES (%s, %s, %s, %s, %s, %s)",
            (usuario.username, usuario.password, usuario.nombre, usuario.email, usuario.role, int(usuario.activo))
        )
        self.conn.commit()
        usuario.id = cur.lastrowid
        cur.close()
        return usuario

    def get_by_id(self, _id: int) -> Optional[Usuario]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, username, password, nombre, email, role, activo FROM usuarios WHERE id = %s", (_id,))
        row = cur.fetchone()
        cur.close()
        return Usuario.from_row(row) if row else None

    def get_by_username(self, username: str) -> Optional[Usuario]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, username, password, nombre, email, role, activo FROM usuarios WHERE username = %s", (username,))
        row = cur.fetchone()
        cur.close()
        return Usuario.from_row(row) if row else None

    def update(self, usuario: Usuario) -> Usuario:
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE usuarios SET username = %s, password = %s, nombre = %s, email = %s, role = %s, activo = %s WHERE id = %s",
            (usuario.username, usuario.password, usuario.nombre, usuario.email, usuario.role, int(usuario.activo), usuario.id)
        )
        self.conn.commit()
        cur.close()
        return usuario

    def delete(self, _id: int) -> bool:
        cur = self.conn.cursor()
        cur.execute("DELETE FROM usuarios WHERE id = %s", (_id,))
        self.conn.commit()
        affected = cur.rowcount
        cur.close()
        return affected > 0

    def list_all(self) -> List[Usuario]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, username, password, nombre, email, role, activo FROM usuarios")
        rows = cur.fetchall()
        cur.close()
        return [Usuario.from_row(row) for row in rows]
