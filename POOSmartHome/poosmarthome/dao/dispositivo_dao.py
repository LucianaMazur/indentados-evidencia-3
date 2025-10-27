from poosmarthome.dao.interfaces.i_dispositivo_dao import IDispositivoDAO
from poosmarthome.dominio.dispositivo import Dispositivo
from poosmarthome.conn.db_conn import DBConnection

class DispositivoDAO(IDispositivoDAO):
    """Gestión de dispositivos en la BD"""

    def create(self, dispositivo):
        try:
            with DBConnection().cursor() as cur:
                cur.execute(
                    "INSERT INTO dispositivos (nombre, tipo, esencial) VALUES (%s, %s, %s)",
                    (dispositivo.nombre, dispositivo.tipo, int(dispositivo.esencial))
                )
                DBConnection().get_connection().commit()
                dispositivo.id = cur.lastrowid
            return dispositivo
        except Exception as e:
            print(f"Error creando dispositivo: {e}")
            DBConnection().get_connection().rollback()
            return None

    def get_by_id(self, _id):
        try:
            with DBConnection().cursor() as cur:
                cur.execute("SELECT id, nombre, tipo, esencial FROM dispositivos WHERE id=%s", (_id,))
                row = cur.fetchone()
            return Dispositivo.from_row(row) if row else None
        except Exception as e:
            print(f"Error obteniendo dispositivo: {e}")
            return None

    def update(self, dispositivo):
        try:
            with DBConnection().cursor() as cur:
                cur.execute(
                    "UPDATE dispositivos SET nombre=%s, tipo=%s, esencial=%s WHERE id=%s",
                    (dispositivo.nombre, dispositivo.tipo,
                     int(dispositivo.esencial), dispositivo.id)
                )
                DBConnection().get_connection().commit()
            return dispositivo
        except Exception as e:
            print(f"Error actualizando dispositivo: {e}")
            DBConnection().get_connection().rollback()
            return None

    def delete(self, _id):
        try:
            with DBConnection().cursor() as cur:
                cur.execute("DELETE FROM dispositivos WHERE id=%s", (_id,))
                DBConnection().get_connection().commit()
                return cur.rowcount > 0
        except Exception as e:
            print(f"Error eliminando dispositivo: {e}")
            DBConnection().get_connection().rollback()
            return False

    def list_all(self):
        try:
            with DBConnection().cursor() as cur:
                cur.execute("SELECT id, nombre, tipo, esencial FROM dispositivos")
                rows = cur.fetchall()
            return [Dispositivo.from_row(r) for r in rows]
        except Exception as e:
            print(f"Error listando dispositivos: {e}")
            return []
