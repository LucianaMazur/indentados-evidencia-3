from poosmarthome.dominio.usuario import Usuario
from poosmarthome.dao.usuario_dao import UsuarioDAO


def test_crear_usuario():
    dao = UsuarioDAO()
    usuario = Usuario(id=0, username='test_user1', password='pass123',
                     nombre='Test', email='test@mail.com', role='standard', activo=True)
    
    created = dao.create(usuario)
    
    assert created.id > 0
    assert created.username == 'test_user1'
    
    dao.delete(created.id)


def test_validar_email():
    #Email válido
    u1 = Usuario(id=0, username='test', password='pass', nombre='Test',
                email='valido@mail.com', role='standard')
    assert u1.validar_email() is True
    
    # Email inválido
    u2 = Usuario(id=0, username='test', password='pass', nombre='Test',
                email='invalido', role='standard')
    assert u2.validar_email() is False


def test_es_admin():
    admin = Usuario(id=1, username='admin', password='pass', nombre='Admin',
                   email='admin@mail.com', role='admin')
    standard = Usuario(id=2, username='user', password='pass', nombre='User',
                      email='user@mail.com', role='standard')
    
    assert admin.is_admin() is True
    assert standard.is_admin() is False


def test_actualizar_usuario():
    #Actualizar datos de un usuario
    dao = UsuarioDAO()
    usuario = Usuario(id=0, username='test_user2', password='pass123',
                     nombre='Original', email='test2@mail.com', role='standard', activo=True)
    
    created = dao.create(usuario)
    created.nombre = 'Actualizado'
    dao.update(created)
    
    obtenido = dao.get_by_id(created.id)
    assert obtenido.nombre == 'Actualizado'
    
    dao.delete(created.id)
