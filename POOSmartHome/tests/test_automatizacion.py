import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from poosmarthome.dominio.automatizacion import Automatizacion
from poosmarthome.dominio.dispositivo import Dispositivo
from poosmarthome.dao.automatizacion_dao import AutomatizacionDAO
from poosmarthome.dao.dispositivo_dao import DispositivoDAO


def test_crear_automatizacion():
    disp_dao = DispositivoDAO()
    auto_dao = AutomatizacionDAO()
    
    # Crear dispositivo
    dispositivo = Dispositivo(id=0, nombre='Test Disp Auto', tipo='test', esencial=True)
    disp = disp_dao.create(dispositivo)
    
    # Crear automatización
    automatizacion = Automatizacion(id=0, nombre='Test Auto', 
                                   id_dispositivo=disp.id, activa=True)
    auto = auto_dao.create(automatizacion)
    
    assert auto.id > 0
    assert auto.nombre == 'Test Auto'
    
    # Limpiar
    auto_dao.delete(auto.id)
    disp_dao.delete(disp.id)


def test_activar_desactivar():
    auto = Automatizacion(id=1, nombre='Test', id_dispositivo=1, activa=False)
    
    auto.activar()
    assert auto.activa is True
    
    auto.desactivar()
    assert auto.activa is False


def test_cambiar_estado():
    auto = Automatizacion(id=1, nombre='Test', id_dispositivo=1, activa=True)
    
    auto.cambiar_estado()
    assert auto.activa is False
    
    auto.cambiar_estado()
    assert auto.activa is True


def test_cascade_delete():
    #Eliminar dispositivo elimina sus automatizaciones
    disp_dao = DispositivoDAO()
    auto_dao = AutomatizacionDAO()
    
    # Crear dispositivo y automatización
    dispositivo = Dispositivo(id=0, nombre='Test Cascade', tipo='test', esencial=False)
    disp = disp_dao.create(dispositivo)
    
    automatizacion = Automatizacion(id=0, nombre='Auto Cascade',
                                   id_dispositivo=disp.id, activa=True)
    auto = auto_dao.create(automatizacion)
    id_auto = auto.id
    
    # Eliminar dispositivo
    disp_dao.delete(disp.id)
    
    # Verificar que automatización también se eliminó
    assert auto_dao.get_by_id(id_auto) is None