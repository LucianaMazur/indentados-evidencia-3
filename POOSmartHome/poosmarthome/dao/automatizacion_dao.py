from poosmarthome.dao.interfaces.i_automatizacion_dao import IAutomatizacionDAO
from poosmarthome.dominio.automatizacion import Automatizacion
from poosmarthome.conn.db_conn import DBConnection

class AutomatizacionDAO(IAutomatizacionDAO):
    """Gestión de automatizaciones en la BD"""

    def create(self, automatizacion):
        try:
            with DBConnection().cursor() as cur:
                cur.execute(
                    "INSERT INTO automatizaciones (nombre, id_dispositivo, activa) VALUES (%s, %s, %s)",
                    (automatizacion.nombre, automatizacion.id_dispositivo, int(automatizacion.activa))
                )
                DBConnection().get_connection().commit()
                automatizacion.id = cur.lastrowid
            return automatizacion
        except Exception as e:
            print(f"Error creando automatización: {e}")
            DBConnection().get_connection().rollback()
            return None

    def get_by_id(self, _id):
        try:
            with DBConnection().cursor() as cur:
                cur.execute("SELECT id, nombre, id_dispositivo, activa FROM automatizaciones WHERE id=%s", (_id,))
                row = cur.fetchone()
            return Automatizacion.from_row(row) if row else None
        except Exception as e:
            print(f"Error obteniendo automatización: {e}")
            return None

    def update(self, automatizacion):
        try:
            with DBConnection().cursor() as cur:
                cur.execute(
                    "UPDATE automatizaciones SET nombre=%s, id_dispositivo=%s, activa=%s WHERE id=%s",
                    (automatizacion.nombre, automatizacion.id_dispositivo,
                     int(automatizacion.activa), automatizacion.id)
                )
                DBConnection().get_connection().commit()
            return automatizacion
        except Exception as e:
            print(f"Error actualizando automatización: {e}")
            DBConnection().get_connection().rollback()
            return None

    def delete(self, _id):
        try:
            with DBConnection().cursor() as cur:
                cur.execute("DELETE FROM automatizaciones WHERE id=%s", (_id,))
                DBConnection().get_connection().commit()
                return cur.rowcount > 0
        except Exception as e:
            print(f"Error eliminando automatización: {e}")
            DBConnection().get_connection().rollback()
            return False

    def list_all(self):
        try:
            with DBConnection().cursor() as cur:
                cur.execute("SELECT id, nombre, id_dispositivo, activa FROM automatizaciones")
                rows = cur.fetchall()
            return [Automatizacion.from_row(r) for r in rows]
        except Exception as e:
            print(f"Error listando automatizaciones: {e}")
            return []
