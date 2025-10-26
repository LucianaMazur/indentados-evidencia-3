from poosmarthome.dao.interfaces.i_dispositivo_dao import IDispositivoDAO
from poosmarthome.dominio.dispositivo import Dispositivo
from poosmarthome.conn.db_conn import DBConnection

class DispositivoDAO(IDispositivoDAO):
    
    
    def __init__(self):
        self.conn = DBConnection().get_connection()
    
    def create(self, dispositivo):
        
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO dispositivos (nombre, tipo) VALUES (%s, %s)",
            (dispositivo.nombre, dispositivo.tipo)
        )
        self.conn.commit()
        dispositivo.id = cur.lastrowid
        cur.close()
        return dispositivo
    
    def get_by_id(self, _id):
        
        cur = self.conn.cursor()
        cur.execute("SELECT id, nombre, tipo FROM dispositivos WHERE id = %s", (_id,))
        row = cur.fetchone()
        cur.close()
        return Dispositivo.from_row(row) if row else None
    
    def update(self, dispositivo):
        
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE dispositivos SET nombre = %s, tipo = %s WHERE id = %s",
            (dispositivo.nombre, dispositivo.tipo, dispositivo.id)
        )
        self.conn.commit()
        cur.close()
        return dispositivo
    
    def delete(self, _id):
        
        cur = self.conn.cursor()
        cur.execute("DELETE FROM dispositivos WHERE id = %s", (_id,))
        self.conn.commit()
        affected = cur.rowcount
        cur.close()
        return affected > 0
    
    def list_all(self):
        # Listar todos los dispositivos
        cur = self.conn.cursor()
        cur.execute("SELECT id, nombre, tipo FROM dispositivos")
        rows = cur.fetchall()
        cur.close()
        return [Dispositivo.from_row(row) for row in rows]