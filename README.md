ACTIVIDAD INTEGRADORA N° 6

MODULO PROGRAMADOR

GRUPO INDENTADOS:

Facundo Sebastián Moreno – D.N.I: 46.687.918

Lucas Matías Garis – D.N.I: 28.598.726

Luciana del Milagro Mazur – D.N.I: 38.755.361

Micaela Estefanía Bustos Prelato– D.N.I: 40.295.337
# Proyecto SQL - Base de datos "poosmarthome"

## Contiene
- Inserts de datos y consultas SQL (DML)  
- Consultas simples, multitabla y subconsultas adaptadas a las tablas reales del proyecto  

## Entorno
- Motor: **MySQL**  
- DBMS online recomendado: **OneCompiler** ([https://onecompiler.com/mysql](https://onecompiler.com/mysql))  

---

## Pasos para ejecutar

1. Copiar y pegar los **inserts** en OneCompiler y ejecutar para cargar los datos iniciales en las tablas:
   - `usuarios`
   - `dispositivos`
   - `automatizaciones`

2. Ejecutar las consultas deseadas para visualizar resultados:
   - Consultas simples: listar usuarios, dispositivos o automatizaciones.
   - Consultas multitabla: relaciones entre automatizaciones y dispositivos.
   - Subconsultas: filtrado por condiciones específicas (por ejemplo, usuarios con nombres que contengan 'Juan').

---

## Notas importantes
- Las tablas ya existen en el proyecto, estos scripts sirven para cargar datos de ejemplo y probar consultas.
- Las consultas multitabla y subconsultas son pertinentes al negocio:
  - Conocer qué automatizaciones están activas por dispositivo.
  - Listar dispositivos sin automatizaciones.
  - Filtrar usuarios por ciertas condiciones.
