# ProyectoHDP115 - Sistema de Gestión Automotriz 🛠️🚗

Este proyecto es un sistema de gestión para un taller automotriz, desarrollado con Django. Permite registrar vehículos, gestionar mantenimientos, tipos de mantenimiento, y repuestos. Incluye control de stock automático y panel de administración.

## 📋 Características principales

- Registro de vehículos con fotos
- Gestión de mantenimientos
- Tipos de mantenimiento personalizables
- Manejo de repuestos con control de inventario
- Interfaz de administración con Bootstrap
- Validaciones con JavaScript y jQuery
- Descuenta repuestos automáticamente al registrar mantenimientos

## 🛠️ Tecnologías utilizadas

- Python 3.11
- Django 5.2
- SQLite3
- Bootstrap 5
- HTML5, CSS3, JavaScript
- jQuery

## 🗂️ Estructura del proyecto

```
ProyectoHDP115/
├── Aplicaciones/
│   └── Taller/
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── templates/
│           └── mantenimientos.html
├── ProyectoHDP115/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── requirements.txt
```

## ⚙️ Instalación y ejecución

1. **Clonar el repositorio**

```bash
git clone https://github.com/tuusuario/ProyectoHDP115.git
cd ProyectoHDP115
```

2. **Crear entorno virtual (opcional pero recomendado)**

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

4. **Migrar base de datos**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario**

```bash
python manage.py createsuperuser
```

6. **Ejecutar el servidor**

```bash
python manage.py runserver
```

## ✅ Funcionalidades automáticas

- Al registrar un nuevo mantenimiento, se descuentan automáticamente las unidades de repuesto utilizadas.
- Validaciones con jQuery para campos numéricos y cadenas.
- Interface de usuario basada en modales.

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo libremente.

---

## ✉️ Contacto

Desarrollado por **Manuel Hernández**  
📧 manuel.hernandez28@outlook.com  
📍 El Salvador
