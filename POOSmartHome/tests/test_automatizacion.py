from poosmarthome.automatizacion import Automatizacion
from poosmarthome.Dispositivo import Dispositivo

def test_agregar_dispositivo_a_automatizacion():
    a = Automatizacion('a3','apagar_calefactor')
    d = Dispositivo('d2','actuador')
    a.agregar_dispositivo(d)
    assert d in a.dispositivos
