from poosmarthome.dominio.automatizacion import Automatizacion
from poosmarthome.dominio.dispositivo import Dispositivo
from poosmarthome.dao.automatizacion_dao import AutomatizacionDAO
from poosmarthome.dao.dispositivo_dao import DispositivoDAO
from poosmarthome.dominio.usuario import Usuario
from poosmarthome.dao.usuario_dao import UsuarioDAO
from poosmarthome.dominio.automatizacion import Automatizacion
from poosmarthome.dao.automatizacion_dao import AutomatizacionDAO




def test_agregar_dispositivo_a_automatizacion():
   
    d = Dispositivo(id=0, nombre='Sensor Test', tipo='sensor')
    d = DispositivoDAO().create(d)

    
    a = Automatizacion(id=0, nombre='Activar Sensor', id_dispositivo=d.id, activa=True)
    a = AutomatizacionDAO().create(a)

    assert a.id_dispositivo == d.id


def test_crear_usuario_y_automatizacion():
    u = Usuario(id=0, username='prueba1', password='123', nombre='Ana', email='ana@mail', role='estandar', activo=True)
    u = UsuarioDAO().create(u)

    from poosmarthome.dominio.dispositivo import Dispositivo
    from poosmarthome.dao.dispositivo_dao import DispositivoDAO
    d = Dispositivo(id=0, nombre='Luz Test', tipo='iluminacion')
    d = DispositivoDAO().create(d)

    a = Automatizacion(id=0, nombre='Encender Luz', id_dispositivo=d.id, activa=True)
    a = AutomatizacionDAO().create(a)

    assert a.id_dispositivo == d.id


def test_eliminar_automatizacion():
    d = Dispositivo(id=0, nombre='Sensor Borrar', tipo='sensor')
    d = DispositivoDAO().create(d)

    a = Automatizacion(id=0, nombre='Test Delete', id_dispositivo=d.id, activa=True)
    a = AutomatizacionDAO().create(a)

    AutomatizacionDAO().delete(a.id)

    todas = AutomatizacionDAO().list_all()
    ids = [auto.id for auto in todas]
    assert a.id not in ids