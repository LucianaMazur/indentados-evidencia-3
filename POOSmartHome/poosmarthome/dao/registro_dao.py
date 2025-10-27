from poosmarthome.conn.db_conn import DBConnection
from poosmarthome.dominio.registro_actividad import RegistroActividad

class RegistroActividadDAO:
    """Gestión de la tabla registro_actividad"""

    def registrar(self, usuario, accion, detalle):
        """Inserta una nueva acción en la tabla registro_actividad"""
        try:
            with DBConnection().cursor() as cur:
                cur.execute(
                    "INSERT INTO registro_actividad (usuario, accion, detalle) VALUES (%s, %s, %s)",
                    (usuario, accion, detalle)
                )
                DBConnection().get_connection().commit()
        except Exception as e:
            print(f"Error registrando actividad: {e}")
            DBConnection().get_connection().rollback()

    def listar(self, limite=20):
        """Devuelve las últimas N actividades"""
        try:
            with DBConnection().cursor() as cur:
                cur.execute(
                    "SELECT id, fecha, usuario, accion, detalle FROM registro_actividad "
                    "ORDER BY fecha DESC LIMIT %s", (limite,)
                )
                rows = cur.fetchall()
            return [RegistroActividad.from_row(r) for r in rows]
        except Exception as e:
            print(f"Error listando actividades: {e}")
            return []
