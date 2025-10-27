import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from poosmarthome.dominio.dispositivo import Dispositivo
from poosmarthome.dao.dispositivo_dao import DispositivoDAO


def test_crear_dispositivo():
    dao = DispositivoDAO()
    dispositivo = Dispositivo(id=0, nombre='Test Disp', tipo='test', esencial=True)
    
    created = dao.create(dispositivo)
    
    assert created.id > 0
    assert created.nombre == 'Test Disp'
    assert created.esencial is True
    dao.delete(created.id)


def test_obtener_dispositivo():
    #Obtener un dispositivo por ID
    dao = DispositivoDAO()
    dispositivo = Dispositivo(id=0, nombre='Test Get', tipo='test', esencial=False)
    created = dao.create(dispositivo)
    
    obtenido = dao.get_by_id(created.id)
    
    assert obtenido is not None
    assert obtenido.nombre == 'Test Get'
    assert obtenido.esencial is False
    
    dao.delete(created.id)


def test_eliminar_dispositivo():
    dao = DispositivoDAO()
    dispositivo = Dispositivo(id=0, nombre='Test Delete', tipo='test', esencial=True)
    created = dao.create(dispositivo)
    
    resultado = dao.delete(created.id)
    
    assert resultado is True
    assert dao.get_by_id(created.id) is None
