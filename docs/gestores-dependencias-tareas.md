# Automatización del proyecto

## Gestor de paquetes y dependencias
Actualmente gestion-contenedores utiliza módulos de la biblioteca estándar de python y no tiene dependencias externas.

### Criterios
-Que utilice [pyproject.toml](https://packaging.python.org/en/latest/specifications/pyproject-toml/) para declarar dependencias del proyecto.
-Permite la preparación reproducible del entorno cuando se incorporen dependencias externas.
-Minimizar el tiempo de instalación de la herramienta, ya que será necesario prepararla en los futuros entornos de integración continua.

### ¿Cómo realizo las pruebas?
Para comparar las herramientas parto de una imagen de Docker con Python 3.14 y curl. Realizo 3 instalaciones de cada herramienta en contenedores nuevos, utilizando el método de instalación que indica su documentación oficial. 
Me quedo con la mediana de los tres tiempos porque la velocidad de descarga puede variar entre pruebas.

### Alternativas
#### uv
Permite declarar las dependencias en pyproject.toml y conservar antiguas resueltas en las dependencias en uv.lock.
Para instalarlo he usado el comando que aparece en su [documentación oficial](https://docs.astral.sh/uv/getting-started/installation/):
curl -LsSf https://astral.sh/uv/install.sh | sh
He ejecutado este comando en tres contenedores nuevos y he obtenido estos tiempos:
- [Primera instalación](capturas/uv-oficial-1.png): 1,631 s.
- [Segunda instalación](capturas/uv-oficial-2.png): 1,266 s.
- [Tercera instalación](capturas/uv-oficial-3.png): 2,079 s.
Mediana: 1,631 s. Versión utilizada: 0.13.10.

#### PDM
Permite declarar las dependencias en pyproject.toml y guarda versiones resueltas en pdm.lock. También permite definir y ejecutar tareas, algo que tendré en cuenta cuando estudie los gestores de tareas. 
Para instalarlo he usado el comando que aparece en su [documentación oficial](https://pdm-project.org/latest/#installation):
curl -sSL https://pdm-project.org/install.sh | bash
- [Primera instalación](capturas/pdm-oficial-1.png): 16,911 s.
- [Segunda instalación](capturas/pdm-oficial-2.png): 14,332 s.
- [Tercera instalación](capturas/pdm-oficial-3.png): 14,898 s.
Mediana: 14,898 s. Versión utilizada: 2.29.7.

#### Poetry
Permite gestionar las dependencias del proyecto mediante pyproject.toml y guarda las versiones de las liberías en poetry.lock. También permite crear entornos virtuales y empaquetar el proyecto. 
Para instalarlo he utilizado el comando que aparece en su [documentación oficial](https://python-poetry.org/docs/#installation):
curl -sSL https://install.python-poetry.org | python3 -
- [Primera instalación](capturas/poetry-oficial-1.png): 15,199 s.
- [Segunda instalación](capturas/poetry-oficial-2.png): 15,977 s.
- [Tercera instalación](capturas/poetry-oficial-3.png): 19,480 s.
Mediana: 15,977 s. Versión utilizada: 2.5.2.

#### Hatch
Permite declarar las dependencias en pyproject.toml, gestionar los entornos y definir tareas. Sigiendo las indicaciones de su [documentación oficial](https://hatch.pypa.io/latest/install/#standalone-binaries) he descargado el programa ya compilado para Linux, lo he descomprimido y he comprobado que funciona.
Tambien he incluido dentro del tiempo de instalación la primera ejecución de hatch --help para comprobar que la herramienta está lista para utilizarse. En las herramientas anteriores, la comprobación de la versión se hizo fuera del tiempo medido. 
- [Primera instalación](capturas/hatch-oficial-1.png): 5,637 s.
- [Segunda instalación](capturas/hatch-oficial-2.png): 4,176 s.
- [Tercera instalación](capturas/hatch-oficial-3.png): 4,339 s.
Mediana: 4,339 s. Versión utilizada: 1.18.2.

#### Pixi
Permite declarar las dependencias en pyproject.toml y guaradar las versiones en pixi.lock. A diferencia de otras herramientas permite gestionar tanto paquetes de Python como paquetes de otros lenguajes y también ejecutar tareas. 
Para ejecutarlo he utilizado el comando que aparece en su [documentación oficial](https://pixi.prefix.dev/latest/installation/):
curl -fsSL https://pixi.sh/install.sh | sh
- [Primera instalación](capturas/pixi-oficial-1.png): 4,987 s.
- [Segunda instalación](capturas/pixi-oficial-2.png): 2,942 s.
- [Tercera instalación](capturas/pixi-oficial-3.png): 5,319 s.
Mediana: 4,987 s. Versión utilizada: 0.85.0.

### Elección gestor de paquetes y dependencias
Tras consultar la documentación de las cinco herramientas, he visto que todas permiten utilizar pyproject.toml y conservar versiones de las dependencias. Como ahora mismo mi proyecto no utiliza librerías externas el criterio por el que puedo decidir es el tiempo que tardan en instalarse. 
Mi elección final es uv, ya que hah obtenido una mediana de 1,631 s, frente a los 4,339 s de Hatch, 4,987 s de Pixi, los 14,898 s de PDM y los 15,977 s de Poetry. Aunque Pixi permita gestionar paquetes de otros lenguajes como no necesito actualmente esa funcionalidad porque esta desarrollado únicamnete en Python mantendré uv.

## Gestor de tareas

### Criterios

### Alternativas

### Mediciones

### Elección