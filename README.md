# 🛡️ Sistema de Incidencias y Soporte Técnico

> 🏆 **Proyecto Galardonado con el 3er Lugar** en la Hackathon de [Nombre de la Universidad/Evento].

![Estado](https://img.shields.io/badge/Estado-Terminado-success)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-4.x-green)
![Tailwind](https://img.shields.io/badge/Tailwind-CSS-38B2AC)

## 📄 Descripción

Plataforma web integral diseñada para optimizar la gestión de tickets de soporte técnico dentro de una organización. El sistema permite a los usuarios reportar incidencias y a los administradores gestionar, priorizar y resolver solicitudes de manera eficiente.

Desarrollado bajo presión en un entorno competitivo (Hackathon), este proyecto demuestra la capacidad de crear un **MVP (Producto Mínimo Viable)** funcional, escalable y con una arquitectura limpia utilizando el framework **Django**.

## 🚀 Características Principales

* **🔐 Autenticación y Roles:** Sistema robusto de gestión de usuarios con diferentes niveles de acceso (Administrador, Soporte, Cliente).
* **🎫 Gestión de Tickets:** Ciclo de vida completo de incidencias (Creación, Asignación, Proceso, Resolución).
* **🎨 Interfaz Moderna:** Diseño responsivo y amigable construido con **Tailwind CSS**, asegurando una excelente experiencia de usuario (UX).
* **📊 Panel de Administración:** Dashboard para la supervisión del estado de los tickets y métricas de resolución.
* **🗄️ Base de Datos Relacional:** Modelado eficiente de datos para mantener la integridad de la información histórica.

## 🛠️ Tecnologías Utilizadas

Este proyecto utiliza una arquitectura monolítica basada en el patrón **MVT (Model-View-Template)** de Django:

* **Backend:** Python, Django Framework.
* **Frontend:** HTML5, JavaScript, **Tailwind CSS** (para estilizado rápido y responsivo).
* **Base de Datos:** SQLite (Entorno de desarrollo) / PostgreSQL (Compatible para producción).
* **Control de Versiones:** Git & GitHub.

## 🔧 Instalación y Despliegue Local

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/AlvaroCRAK/Sistema_de_Incidencias_y_Soporte.git](https://github.com/AlvaroCRAK/Sistema_de_Incidencias_y_Soporte.git)
    cd Sistema_de_Incidencias_y_Soporte
    ```

2.  **Crear y activar un entorno virtual (Opcional pero recomendado):**
    ```bash
    python -m venv venv
    # En Windows:
    venv\Scripts\activate
    # En Mac/Linux:
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Realizar migraciones de base de datos:**
    ```bash
    python manage.py migrate
    ```

5.  **Ejecutar el servidor:**
    ```bash
    python manage.py runserver
    ```
    Visita `http://127.0.0.1:8000/` en tu navegador.

## 👥 Autores

* **Álvaro Cencia** ([@AlvaroCRAK](https://github.com/AlvaroCRAK)) - *Desarrollo Full Stack & Arquitectura*
* **[Nombre de tu compañero si deseas ponerlo]** ([@guzmdav16](https://github.com/guzmdav16)) - *Colaborador*

---
