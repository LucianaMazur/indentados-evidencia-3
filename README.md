# 🏠 Proyecto SmartHome Solutions
### Actividad Integradora N° 6 – Módulo Programador

---

## 👥 Integrantes del grupo **Indentados**

- **Facundo Sebastián Moreno** – DNI 46.687.918
- **Lucas Matías Garis** – DNI 28.598.726
- **Luciana del Milagro Mazur** – DNI 38.755.361
- **Micaela Estefanía Bustos Prelato** – DNI 40.295.337

---

## 💡 Descripción general del proyecto

El proyecto **SmartHome Solutions** es una aplicación basada en **Programación Orientada a Objetos (POO)** con conexión a una base de datos **MySQL**, cuyo objetivo es gestionar de manera integral un sistema domótico para el hogar.  
Permite administrar usuarios, dispositivos inteligentes y automatizaciones, aplicando principios de diseño escalable y buenas prácticas de desarrollo.

Este trabajo constituye la **Evidencia N° 6 del Módulo Programador**, integrando conceptos de **POO, persistencia de datos, SQL, patrones de diseño y testing automatizado.**

---

## ⚙️ Tecnologías utilizadas

| Área | Tecnología |
|------|-------------|
| Lenguaje principal | Python 3.13 |
| Base de datos | MySQL |
| Arquitectura | POO + DAO (Data Access Object) + Singleton |
| Testing | Pytest |
| Entorno online sugerido | OneCompiler (para pruebas SQL) |

---

## 🧩 Estructura del proyecto

```
POOSmartHome/
│
├── poosmarthome/
│   ├── conn/                 # Conexión a la base de datos (db_conn.py)
│   ├── dao/                  # Clases DAO (acceso a datos)
│   ├── dominio/              # Clases de dominio (Usuario, Dispositivo, etc.)
│   └── main.py               # Programa principal
│
├── scripts/
│   ├── script_DDL.sql        # Creación de tablas
│   └── script_DML.sql        # Inserción de datos y consultas
│
├── tests/                    # Pruebas unitarias con pytest
└── README.md
```

---

## 🗄️ Instrucciones para ejecutar la base de datos
## Entorno
- Motor: **MySQL**  
- DBMS online recomendado: **OneCompiler** ([https://onecompiler.com/mysql](https://onecompiler.com/mysql))  

### 1️⃣ Crear la base de datos

```sql
CREATE DATABASE poosmarthome;
USE poosmarthome;
```

### 2️⃣ Ejecutar el script DDL

Copiar y ejecutar el contenido del archivo `script_DDL.sql`.  
Este crea las tablas:
- `usuarios`
- `dispositivos`
- `automatizaciones`
- `registro_actividad`

Verificar con:

```sql
SHOW TABLES;
```

### 3️⃣ Ejecutar el script DML

Luego, ejecutar `script_DML.sql`, que:
- Inserta **10 registros por tabla**.  
- Incluye **4 consultas multitabla (JOIN)** y **2 subconsultas**.  
- Contiene consultas `SELECT` para comprobar los datos cargados.

Ejemplos:
```sql
-- Consultas multitabla
SELECT a.nombre, d.nombre
FROM automatizaciones a
JOIN dispositivos d ON a.id_dispositivo = d.id;

-- Subconsulta: usuarios sin automatizaciones activas
SELECT nombre FROM usuarios
WHERE id NOT IN (SELECT id_dispositivo FROM automatizaciones WHERE activa = 1);
```

### 4️⃣ Conectar el sistema en Python

Editar `poosmarthome/conn/db_conn.py` con tus credenciales locales:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "TU_CONTRASEÑA",
    "database": "poosmarthome"
}
```

### 5️⃣ Ejecutar la aplicación

Desde la terminal:

```bash
python main.py
```

Deberías ver:

```
✅ Conexión a MySQL establecida correctamente.
```

y luego el menú principal del sistema.

---

## 🧠 Funcionalidades principales

### 👤 Gestión de usuarios
- Registro e inicio de sesión.  
- Roles: `admin` y `standard`.  
- Activación/desactivación y modificación de usuarios.

### 💡 Gestión de dispositivos
- Alta, baja y modificación de dispositivos.  
- Campo adicional `esencial` para marcar equipos críticos.  

### 🔁 Gestión de automatizaciones
- Creación, activación/desactivación y eliminación de automatizaciones.  
- Asociación directa a cada dispositivo.  
- Eliminación en cascada: al borrar un dispositivo, sus automatizaciones también se eliminan.

### 🕓 Registro de actividad
- Cada acción relevante (crear, editar, eliminar) queda registrada en la tabla `registro_actividad` con fecha, usuario y detalle.

---

## 🧪 Testing automatizado

El proyecto incluye **11 pruebas unitarias con pytest**:

- **4 Automatización** → creación, activación, cambio de estado, eliminación en cascada  
- **3 Dispositivo** → creación, obtención, eliminación  
- **4 Usuario** → creación, validación de email, rol admin y actualización  

Ejecutar desde la raíz del proyecto:

```bash
pytest -v
```

✅ Resultado final: las 11 pruebas se ejecutan correctamente con estado PASSED,
confirmando la correcta integración entre el sistema Python y la base de datos MySQL.

---

## 🧱 Patrones de diseño aplicados

| Patrón | Aplicación |
|--------|-------------|
| **POO (Clases y objetos)** | Cada entidad (Usuario, Dispositivo, Automatización, Registro) es una clase. |
| **DAO (Data Access Object)** | Acceso a la base de datos separado de la lógica de negocio. |
| **Singleton** | Asegura una única conexión activa a MySQL mediante la clase `DBConnection`. |
| **MVC simplificado** | Separación clara entre datos (dominio), lógica (DAO) y vista (menú interactivo). |

---

## 📦 Consultas SQL incluidas

El archivo `script_DML.sql` contiene:

- **10 registros por tabla** (`usuarios`, `dispositivos`, `automatizaciones`, `registro_actividad`)  
- **4 consultas multitabla (JOIN)**  
- **2 subconsultas**  
- **Consultas de verificación y filtros**  
- Ejemplo de borrado y actualización de registros

---

## 🌱 Ética y sostenibilidad del desarrollo

El sistema se diseñó respetando **principios de responsabilidad digital**:
- Uso eficiente de recursos de hardware.  
- Promoción del acceso equitativo a la domótica.  
- Código modular y reutilizable, facilitando la ampliación sin duplicar esfuerzos.  
- Pruebas automatizadas que garantizan la confiabilidad del software.

---



Proyecto presentado como parte de la **Tecnicatura Superior en Desarrollo de Software – ISPC**,  
correspondiente al **Módulo Programador (Evidencia 6)**. 
