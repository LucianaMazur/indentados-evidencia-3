class Usuario:
    
    def __init__(self, id, username, password, nombre, email, role="standard", activo=True):
        self._id = id
        self._username = username
        self._password = password
        self._nombre = nombre
        self._email = email
        self._role = role
        self._activo = activo
    
    # Getters
    @property
    def id(self):
        return self._id
    
    @property
    def username(self):
        return self._username
    
    @property
    def password(self):
        return self._password
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def email(self):
        return self._email
    
    @property
    def role(self):
        return self._role
    
    @property
    def activo(self):
        return self._activo
    
    # Setters
    @id.setter
    def id(self, value):
        self._id = value
    
    @username.setter
    def username(self, value):
        self._username = value
    
    @password.setter
    def password(self, value):
        self._password = value
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
    
    @email.setter
    def email(self, value):
        self._email = value
    
    @role.setter
    def role(self, value):
        self._role = value
    
    @activo.setter
    def activo(self, value):
        self._activo = value
    
    # Métodos de negocio
    def validar_email(self):
        #Valida que el email tenga formato correcto
        return '@' in self._email and '.' in self._email
    
    def es_activo(self):
        #Verifica si el usuario está activo
        return self._activo
    
    def is_admin(self):
        #Verifica si tiene rol de administrador
        return self._role == "admin"
    
    @staticmethod
    def from_row(row):
        #Crea un objeto Usuario desde una tupla de base de datos
        if row is None:
            return None
        return Usuario(
            id=row[0],
            username=row[1],
            password=row[2],
            nombre=row[3],
            email=row[4],
            role=row[5],
            activo=bool(row[6])
        )