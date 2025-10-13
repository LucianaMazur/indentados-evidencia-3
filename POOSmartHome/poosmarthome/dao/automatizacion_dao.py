from poosmarthome.conn.db_conn import DBConnection
from poosmarthome.dominio.automatizacion import Automatizacion

class AutomatizacionDAO:

    def __init__(self):
        self.db = DBConnection()

    def create(self, automatizacion: Automatizacion):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        query = "INSERT INTO automatizaciones (nombre, id_dispositivo, activa) VALUES (%s, %s, %s)"
        cursor.execute(query, (automatizacion.nombre, automatizacion.id_dispositivo, automatizacion.activa))
        conn.commit()
        cursor.close()
        print("✅ Automatización guardada en la base de datos.")

    def list_all(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, id_dispositivo, activa FROM automatizaciones")
        rows = cursor.fetchall()
        cursor.close()
        automatizaciones = []
        for row in rows:
            automatizaciones.append(
                Automatizacion(id=row[0], nombre=row[1], id_dispositivo=row[2], activa=row[3])
            )
        return automatizaciones

    def delete(self, id_automatizacion):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM automatizaciones WHERE id = %s", (id_automatizacion,))
        conn.commit()
        cursor.close()
        print("🗑️ Automatización eliminada correctamente.")

    def listar_por_dispositivo(self, id_dispositivo):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, id_dispositivo, activa FROM automatizaciones WHERE id_dispositivo = %s", (id_dispositivo,))
        rows = cursor.fetchall()
        cursor.close()
        return rows

    def cambiar_estado(self, id_auto, activo):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE automatizaciones SET activa = %s WHERE id = %s", (activo, id_auto))
        conn.commit()
        cursor.close()
