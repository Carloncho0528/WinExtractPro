# WinExtractPro
WinExtractPro

WinExtractPro es una aplicación en Python diseñada para descomprimir de forma masiva archivos comprimidos en formatos WinRAR (RAR) y WinZip (ZIP). Con una interfaz gráfica intuitiva basada en tkinter, permite a los usuarios seleccionar una carpeta y extraer cada archivo comprimido en una subcarpeta con su nombre. Incluye una barra de progreso en tiempo real y un manejo robusto de errores, lo que la hace ideal para procesar cientos o miles de archivos comprimidos de manera eficiente.

Características





Soporte para WinRAR y WinZip: Compatible con archivos .rar, .RAR, .zip y .ZIP.



Interfaz gráfica amigable: Selecciona carpetas y monitorea el progreso con una barra visual.



Descompresión masiva: Procesa grandes cantidades de archivos WinRAR y WinZip sin interrupciones.



Manejo de errores: Continúa con el siguiente archivo si uno falla (por ejemplo, si está corrupto).



Cierre limpio: La aplicación se cierra automáticamente al finalizar o al cancelar manualmente.



Registro detallado: Genera logs en la consola para seguimiento y resolución de problemas.

Requisitos





Python 3.6 o superior



Librerías:





rarfile: Para descomprimir archivos WinRAR (RAR).



tkinter: Incluido en Python (puede requerir instalación en algunos sistemas Linux).



zipfile: Incluido en Python para archivos WinZip (ZIP).

Instala las dependencias con:

pip install rarfile

Instalación





Clona el repositorio:

git clone https://github.com/<tu-usuario>/WinExtractPro.git
cd WinExtractPro



Asegúrate de tener las dependencias instaladas (ver arriba).



Ejecuta el script:

python win_extract_pro.py

Uso





Ejecuta el script (python win_extract_pro.py).



Se abrirá una ventana con un botón "Seleccionar Carpeta".



Elige la carpeta que contiene los archivos WinRAR (RAR) y/o WinZip (ZIP).



La aplicación mostrará una barra de progreso y el número de archivos procesados (por ejemplo, "Progreso: 500/950 archivos").



Cada archivo comprimido se extraerá en una subcarpeta con su nombre (sin la extensión).



Al finalizar, se mostrará un mensaje con el resumen y la ventana se cerrará automáticamente.

Capturas de pantalla

(Opcional: Agrega capturas de pantalla de la interfaz gráfica. Usa una herramienta como Snipping Tool en Windows, súbelas al repositorio en una carpeta screenshots/, y enlázalas así:)

Contribuir

¡Las contribuciones son bienvenidas! Para colaborar:




Sugerencias de mejoras:





Soporte para otros formatos de compresión (por ejemplo, .7z).



Manejo de archivos protegidos con contraseña.



Opción para mover archivos comprimidos procesados a una carpeta separada.



Multiprocesamiento para acelerar la descompresión de grandes volúmenes.

Licencia

Este proyecto está licenciado bajo la Licencia MIT.

Créditos

Desarrollado por [Carlos Arturo Garzon]. Creado para simplificar la descompresión masiva de archivos WinRAR y WinZip.

Contacto sedsist@gmail.com 

Para reportar errores o sugerencias, crea un Issue o contacta a [sedsist@gmail.com].
