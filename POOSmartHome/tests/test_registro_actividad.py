from poosmarthome.registro_actividad import RegistroActividad
from poosmarthome.usuario import Usuario
from poosmarthome.dispositivo import Dispositivo

def test_registro_relaciones():
    u = Usuario('u3','Carla','c@mail')
    d = Dispositivo('d3','sensor')
    r = RegistroActividad('r2','movimiento')
    u.agregar_registro(r)
    d.agregar_registro(r)
    assert r in u.registros
    assert r in d.registros
    assert r.usuario is u
    assert r.dispositivo is d

