from typing import List, Optional
from poosmarthome.dao.interfaces.i_dispositivo_dao import IDispositivoDAO
from poosmarthome.dominio.dispositivo import Dispositivo
from poosmarthome.conn.db_conn import DBConnection

class DispositivoDAO(IDispositivoDAO):
    def __init__(self):
        self.conn = DBConnection().get_connection()

    def create(self, dispositivo: Dispositivo) -> Dispositivo:
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO dispositivos (nombre, tipo) VALUES (%s, %s)",
            (dispositivo.nombre, dispositivo.tipo)
        )
        self.conn.commit()
        dispositivo.id = cur.lastrowid
        cur.close()
        return dispositivo

    def get_by_id(self, _id: int) -> Optional[Dispositivo]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, nombre, tipo FROM dispositivos WHERE id = %s", (_id,))
        row = cur.fetchone()
        cur.close()
        return Dispositivo.from_row(row) if row else None

    def update(self, dispositivo: Dispositivo) -> Dispositivo:
        cur = self.conn.cursor()
        cur.execute(
            "UPDATE dispositivos SET nombre = %s, tipo = %s WHERE id = %s",
            (dispositivo.nombre, dispositivo.tipo, dispositivo.id)
        )
        self.conn.commit()
        cur.close()
        return dispositivo

    def delete(self, _id: int) -> bool:
        cur = self.conn.cursor()
        cur.execute("DELETE FROM dispositivos WHERE id = %s", (_id,))
        self.conn.commit()
        affected = cur.rowcount
        cur.close()
        return affected > 0

    def list_all(self) -> List[Dispositivo]:
        cur = self.conn.cursor()
        cur.execute("SELECT id, nombre, tipo FROM dispositivos")
        rows = cur.fetchall()
        cur.close()
        return [Dispositivo.from_row(row) for row in rows]


def listar_dispositivos():
    dao = DispositivoDAO()
    dispositivos = dao.list_all()
    if not dispositivos:
        print("No hay dispositivos registrados.")
    else:
        print("\n--- Lista de Dispositivos ---")
        for d in dispositivos:
            print(f"[{d.id}] {d.nombre} - {d.tipo}")

def agregar_dispositivo():
    dao = DispositivoDAO()
    nombre = input("Nombre del dispositivo: ")
    tipo = input("Tipo de dispositivo: ")
    dispositivo = Dispositivo(id=0, nombre=nombre, tipo=tipo)
    dao.create(dispositivo)
    print("✅ Dispositivo agregado correctamente.")

def editar_dispositivo():
    dao = DispositivoDAO()
    try:
        id_disp = int(input("ID del dispositivo a editar: "))
        d = dao.get_by_id(id_disp)
        if d is None:
            print("❌ Dispositivo no encontrado.")
            return
        nuevo_nombre = input(f"Nuevo nombre ({d.nombre}): ") or d.nombre
        nuevo_tipo = input(f"Nuevo tipo ({d.tipo}): ") or d.tipo
        d.nombre = nuevo_nombre
        d.tipo = nuevo_tipo
        dao.update(d)
        print("✅ Dispositivo actualizado correctamente.")
    except ValueError:
        print("❌ ID inválido.")

def eliminar_dispositivo():
    dao = DispositivoDAO()
    try:
        id_disp = int(input("ID del dispositivo a eliminar: "))
        if dao.delete(id_disp):
            print("✅ Dispositivo eliminado correctamente.")
        else:
            print("❌ No se encontró el dispositivo.")
    except ValueError:
        print("❌ ID inválido.")
