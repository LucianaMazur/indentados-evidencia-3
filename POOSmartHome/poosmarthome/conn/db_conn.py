import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "38755361",  #reemplazá por la tuya
    "database": "poosmarthome"
}


class DBConnection:
    """Maneja una única conexión MySQL (patrón Singleton)."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)
            cls._instance._conn = None
            cls._instance.connect()
        return cls._instance

    def connect(self):
        """Establece la conexión a MySQL."""
        try:
            self._conn = mysql.connector.connect(**DB_CONFIG)
            if self._conn.is_connected():
                print("✅ Conexión a MySQL establecida correctamente.")
        except Error as e:
            print(f"❌ Error conectando a MySQL: {e}")
            self._conn = None

    def get_connection(self):
        """Devuelve una conexión activa, reconectando si es necesario."""
        if not self._conn or not self._conn.is_connected():
            self.connect()
        return self._conn

    def cursor(self, buffered=True):
        """
        Devuelve un cursor seguro y bufferizado.
        Usar: with DBConnection().cursor() as cur:
        """
        conn = self.get_connection()
        return conn.cursor(buffered=buffered)

    def close(self):
        """Cierra la conexión global."""
        if self._conn and self._conn.is_connected():
            self._conn.close()
            self._conn = None
            print("🔒 Conexión a MySQL cerrada correctamente.")
