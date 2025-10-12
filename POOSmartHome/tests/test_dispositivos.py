from poosmarthome.Dispositivo import Dispositivo
from poosmarthome.registro_actividad import RegistroActividad

def test_agregar_registro():
    d = Dispositivo('d1','sensor')
    r = RegistroActividad('r1','encendiÃ³')
    d.agregar_registro(r)
    assert r in d.registros
    assert r.dispositivo is d

