from poosmarthome.usuario import Usuario
from poosmarthome.automatizacion import Automatizacion

def test_crear_usuario_y_automatizacion():
    u = Usuario('u1', 'Ana', 'ana@mail')
    a = Automatizacion('a1', 'encender_luz')
    u.crear_automatizacion(a)
    assert a in u.automatizaciones
    assert a.propietario is u

def test_eliminar_automatizaciones_al_borrar_usuario():
    u = Usuario('u2', 'Luis', 'luis@mail')
    u.crear_automatizacion(Automatizacion('a2','x'))
    u.eliminar_automatizaciones()
    assert u.automatizaciones == []
