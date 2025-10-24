from typing import List, Optional

try:
    from poosmarthome.dao.dispositivo_dao import DispositivoDAO
    from poosmarthome.dominio.dispositivo import Dispositivo
except Exception:
    try:
        from dao.dispositivo_dao import DispositivoDAO
        from dominio.dispositivo import Dispositivo
    except Exception:
        raise

dao = DispositivoDAO()

def registrar_dispositivo(nombre: str, tipo: str) -> Dispositivo:
   
    d = Dispositivo(id=0, nombre=nombre, tipo=tipo)
    created = dao.create(d)
    return created

def agregar_dispositivo() -> Optional[Dispositivo]:

    try:
        nombre = input("Nombre dispositivo: ")
        tipo = input("Tipo dispositivo: ")
        created = registrar_dispositivo(nombre, tipo)
        print(f"Dispositivo creado. ID: {created.id}")
        return created
    except Exception as e:
        print("Error creando dispositivo:", e)
        return None

def listar_dispositivos(print_output: bool = True) -> List[Dispositivo]:
  
    devices = dao.list_all()
    if print_output:
        if not devices:
            print("No hay dispositivos registrados.")
        for d in devices:
            print(f"ID:{d.id}  Nombre:{d.nombre}  Tipo:{d.tipo}")
    return devices

def editar_dispositivo(_id: Optional[int] = None) -> Optional[Dispositivo]:
 
    try:
        if _id is None:
            raw = input("ID dispositivo a editar: ")
            _id = int(raw)
        d = dao.get_by_id(_id)
        if not d:
            print("Dispositivo no encontrado.")
            return None
        nuevo_nombre = input(f"Nombre ({d.nombre}): ") or d.nombre
        nuevo_tipo = input(f"Tipo ({d.tipo}): ") or d.tipo
        d.nombre = nuevo_nombre
        d.tipo = nuevo_tipo
        dao.update(d)
        print("Dispositivo actualizado.")
        return d
    except ValueError:
        print("ID inválido.")
        return None
    except Exception as e:
        print("Error al editar dispositivo:", e)
        return None

def eliminar_dispositivo(_id: Optional[int] = None) -> bool:

    try:
        if _id is None:
            raw = input("ID dispositivo a eliminar: ")
            _id = int(raw)
        ok = dao.delete(_id)
        if ok:
            print("Dispositivo eliminado.")
        else:
            print("No se encontró dispositivo con ese ID.")
        return ok
    except ValueError:
        print("ID inválido.")
        return False
    except Exception as e:
        print("Error al eliminar dispositivo:", e)
        return False

__all__ = [
    "registrar_dispositivo",
    "agregar_dispositivo",
    "listar_dispositivos",
    "editar_dispositivo",
    "eliminar_dispositivo",
]
