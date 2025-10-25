from poosmarthome.dominio.dispositivo import Dispositivo
from poosmarthome.dao.dispositivo_dao import DispositivoDAO


def test_crear_dispositivo():
    dao = DispositivoDAO()
    dispositivo = Dispositivo(id=0, nombre='Test Disp', tipo='test')
    
    created = dao.create(dispositivo)
    
    assert created.id > 0
    assert created.nombre == 'Test Disp'
    
    dao.delete(created.id)


def test_obtener_dispositivo():
    #Obtener un dispositivo por ID
    dao = DispositivoDAO()
    dispositivo = Dispositivo(id=0, nombre='Test Get', tipo='test')
    created = dao.create(dispositivo)
    
    obtenido = dao.get_by_id(created.id)
    
    assert obtenido is not None
    assert obtenido.nombre == 'Test Get'
    
    dao.delete(created.id)


def test_eliminar_dispositivo():
    dao = DispositivoDAO()
    dispositivo = Dispositivo(id=0, nombre='Test Delete', tipo='test')
    created = dao.create(dispositivo)
    
    resultado = dao.delete(created.id)
    
    assert resultado is True
    assert dao.get_by_id(created.id) is None
