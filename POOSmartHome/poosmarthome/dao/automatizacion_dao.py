from poosmarthome.dao.interfaces.i_automatizacion_dao import IAutomatizacionDAO
from poosmarthome.dominio.automatizacion import Automatizacion
from poosmarthome.conn.db_conn import DBConnection

class AutomatizacionDAO(IAutomatizacionDAO):
    
    def __init__(self):
        self.conn = DBConnection().get_connection()
    
    def create(self, automatizacion):
        
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO automatizaciones (nombre, id_dispositivo, activa) VALUES (%s, %s, %s)",
            (automatizacion.nombre, automatizacion.id_dispositivo, int(automatizacion.activa))
        )
        self.conn.commit()
        automatizacion.id = cur.lastrowid
        cur.close()
        return automatizacion
    
    def get_by_id(self, _id):
        
        cur = self.conn.cursor()
        cur.execute("SELECT id, nombre, id_dispositivo, activa FROM automatizaciones WHERE id = %s", (_id,))
        row = cur.fetchone()
        cur.close()
        return Automatizacion.from_row(row) if row else None
    
    def update(self, automatizacion):
    
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE automatizaciones SET nombre = %s, id_dispositivo = %s, activa = %s WHERE id = %s",
            (automatizacion.nombre, automatizacion.id_dispositivo, int(automatizacion.activa), automatizacion.id)
        )
        self.conn.commit()
        cur.close()
        return automatizacion
    
    def delete(self, _id):
        
        cur = self.conn.cursor()
        cur.execute("DELETE FROM automatizaciones WHERE id = %s", (_id,))
        self.conn.commit()
        affected = cur.rowcount
        cur.close()
        return affected > 0
    
    def list_all(self):
        
        cur = self.conn.cursor()
        cur.execute("SELECT id, nombre, id_dispositivo, activa FROM automatizaciones")
        rows = cur.fetchall()
        cur.close()
        return [Automatizacion.from_row(row) for row in rows]
    
    def listar_por_dispositivo(self, id_dispositivo):
        
        cur = self.conn.cursor()
        cur.execute(
            "SELECT id, nombre, id_dispositivo, activa FROM automatizaciones WHERE id_dispositivo = %s", 
            (id_dispositivo,)
        )
        rows = cur.fetchall()
        cur.close()
        return [Automatizacion.from_row(row) for row in rows]
    
    def cambiar_estado(self, id_auto, activa):
        
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE automatizaciones SET activa = %s WHERE id = %s",
            (int(activa), id_auto)
        )
        self.conn.commit()
        affected = cur.rowcount
        cur.close()
        return affected > 0