import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "38755361",
    "database": "poosmarthome"
}

class DBConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)
            try:
                cls._instance._conn = mysql.connector.connect(
                    host=DB_CONFIG["host"],
                    user=DB_CONFIG["user"],
                    password=DB_CONFIG["password"]
                )
                cls._instance._initialize()
            except Error as e:
                print(f"Error conectando a MySQL: {e}")
        return cls._instance

    def _initialize(self):
        """Crea la base de datos y las tablas si no existen"""
        cur = self._conn.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS poosmarthome;")
        cur.execute("USE poosmarthome;")

    
        cur.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(100) NOT NULL
            );
        """)

    
        cur.execute("""
            CREATE TABLE IF NOT EXISTS dispositivos (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                tipo VARCHAR(50) NOT NULL
            );
        """)

    
        cur.execute("""
            CREATE TABLE IF NOT EXISTS automatizaciones (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                id_dispositivo INT,
                FOREIGN KEY (id_dispositivo) REFERENCES dispositivos(id)
                    ON DELETE CASCADE ON UPDATE CASCADE
            );
        """)

        self._conn.commit()
        cur.close()

    
        self._conn.database = "poosmarthome"

    def get_connection(self):
        return self._conn
    
    def close(self):
        conn = self.get_connection()
        if conn and conn.is_connected():
         conn.close()
        print("🔒 Conexión a MySQL cerrada correctamente.")

