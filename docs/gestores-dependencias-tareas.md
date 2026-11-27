# Automatización del proyecto

## Gestor de paquetes y dependencias
Actualmente gestion-contenedores utiliza módulos de la biblioteca estándar de python y no tiene dependencias externas.

### Criterios
-Utiliza pyproject.toml para declarar dependencias del proyecto.
-Permite la preparación reproducible del entorno cuando se incorporen dependencias externas.
-Minimizar el tiempo de instalación de la herramienta, ya que será necesario prepararla en los futuros entornos de integración continua.

### ¿Cómo realizo las pruebas?
Para comparar las herramientas parto de una imagen de Docker con Python 3.14 y curl. Realizo 3 instalaciones de cada herramienta en contenedores nuevos, utilizando el método de instalación que indica su documentación oficial. 
Me quedo con la mediana de los tres tiempos porque la velocidad de descarga puede variar entre pruebas.

### Alternativas
#### uv
Permite declarar las dependencias en pyproject.toml y conservar antiguas versiones en uv.lock.
Para instalarlo he usado el comando que aparece en su [documentación oficial](https://docs.astral.sh/uv/getting-started/installation/):
curl -LsSf https://astral.sh/uv/install.sh | sh
He ejecutado este comando en tres contenedores nuevos y he obtenido estos tiempos:
- [Primera instalación](docs/capturas/uv-oficial-1.png): 1,631 s.
- [Segunda instalación](docs/capturas/uv-oficial-2.png): 1,266 s.
- [Tercera instalación](docs/capturas/uv-oficial-3.png): 2,079 s.
Mediana: 1,631 s. Versión utilizada: 0.13.10.

#### PDM
Permite declarar las dependencias en pyproject.toml y guarda versiones resueltas en pdm.lock. También permite definir y ejecutar tareas, algo que tendré en cuenta cuando estudie los gestores de tareas. 
Para instalarlo he usado el comando que aparece en su [documentación oficial](https://pdm-project.org/latest/#installation):
curl -sSL https://pdm-project.org/install.sh | bash
- [Primera instalación](docs/capturas/pdm-oficial-1.png): 16,911 s.
- [Segunda instalación](docs/capturas/pdm-oficial-2.png): 14,332 s.
- [Tercera instalación](docs/capturas/pdm-oficial-3.png): 14,898 s.
Mediana: 1,631 s. Versión utilizada: 2.29.7.

### Mediciones

### Elección

## Gestor de tareas

### Criterios

### Alternativas

### Mediciones

### Elección