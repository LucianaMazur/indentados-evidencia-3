import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "40295337", # <- Hay que poner la contraseña del MySQL
    "database": "poosmarthome"
}

class DBConnection:
    # Singleton para manejar conexión a BD
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)
            try:
                cls._instance._conn = mysql.connector.connect(
                    host=DB_CONFIG["host"],
                    user=DB_CONFIG["user"],
                    password=DB_CONFIG["password"],
                    database=DB_CONFIG["database"]
                )
                print("Conexión a MySQL establecida correctamente.")
            except Error as e:
                print(f"Error conectando a MySQL: {e}")
                cls._instance._conn = None
        return cls._instance
    
    def get_connection(self):
        # Devolver conexión activa
        return self._conn
    
    def close(self):
        # Cerrar conexión a BD
        if self._conn and self._conn.is_connected():
            self._conn.close()
            print("Conexión a MySQL cerrada correctamente.")