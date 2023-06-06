# ProyectoFinalEstadistica1UTP2023-1
repositorio donde estará almacenado el proyecto final de estadistica 1 del semestre 1 del 2023. Aqui se encontrara el codigo del aplicativo estadistico elaborado en python con ayuda de chatGPT, imagenes para tener una idea de la visualizacion del aplicativo y el archivo de excel que se utilizo de prueba.

La lista de bibliotecas que se deben instalar incluye:

- pandas: `pip install pandas`
- numpy: `pip install numpy`
- matplotlib: `pip install matplotlib`
- tkinter: No se requiere instalación adicional, ya que es una biblioteca estándar de Python.
- scipy: `pip install scipy`
- elevenlabs: La biblioteca `elevenlabs` no está disponible en el índice de paquetes de Python. Asegúrate de que estás utilizando el nombre correcto y, si es un paquete personalizado, asegúrate de tenerlo disponible en tu entorno.
- ffpyplayer: `pip install ffpyplayer`

Recuerda utilizar el gestor de paquetes `pip` para instalar las bibliotecas necesarias.



# README

Este repositorio contiene un aplicativo estadístico desarrollado en Python que permite calcular y visualizar la distribución normal de una columna de datos en un archivo de Excel. El aplicativo utiliza las siguientes bibliotecas y módulos:

- **pandas**: Biblioteca utilizada para trabajar con datos de Excel.
- **numpy**: Biblioteca utilizada para cálculos numéricos.
- **matplotlib**: Biblioteca utilizada para graficar.
- **tkinter**: Biblioteca utilizada para crear la interfaz gráfica.
- **scipy.stats**: Módulo utilizado para calcular la distribución normal.
- **elevenlabs**: Módulo utilizado para generar audio (se requiere una API key de Eleven Labs).
- **ffpyplayer**: Módulo utilizado para reproducir audio.

## Instrucciones de uso

1. Antes de utilizar el aplicativo, es necesario crear una cuenta en Eleven Labs para obtener una API key. Puedes crear una cuenta en [https://beta.elevenlabs.io/](https://beta.elevenlabs.io/). Una vez que tengas la API key, debes reemplazar `"<YOUR_API_KEY>"` en el código por tu API key.

2. El aplicativo requiere un archivo de Excel (.xlsx) como entrada. Para abrir un archivo, selecciona la opción "Archivo" en la barra de menú y luego selecciona "Abrir archivo". Se abrirá un cuadro de diálogo para que puedas seleccionar el archivo de Excel.

3. Después de abrir el archivo de Excel, se mostrará una ventana con las hojas disponibles en el archivo. Selecciona una hoja y luego selecciona una columna de la lista desplegable correspondiente.

4. Una vez seleccionada la hoja y la columna, ingresa un valor en el campo "Valor de x" y presiona el botón "Calcular distribución normal estandar" para generar y mostrar las gráficas de la distribución normal y la distribución normal estandarizada.

5. Para cerrar el aplicativo, puedes seleccionar la opción "Archivo" en la barra de menú y luego seleccionar "Cerrar".

## Notas

- El aplicativo utiliza la biblioteca `ffpyplayer` para reproducir audio en algunos eventos, como la apertura del archivo, la selección de hojas y columnas, y el cierre del programa. Si no se desea utilizar el audio, se pueden comentar las líneas correspondientes en el código.

- El aplicativo está diseñado para trabajar con archivos de Excel que contengan una o más hojas con datos. Cada hoja se representa como una tabla en la interfaz gráfica (tabla optimizada para 3 columnas).

- El cálculo de la distribución normal se realiza utilizando la función `norm.pdf` de la biblioteca `scipy.stats`, y el cálculo de la distribución normal estandarizada se realiza utilizando la función `norm.cdf`.

- Las gráficas generadas muestran la distribución normal y la distribución normal estandarizada, con el valor ingresado resaltado y el área sombreada correspondiente.

- El aplicativo es solo para fines educativos y no garantiza la precisión o validez de los resultados obtenidos.

¡Disfruta usando el aplicativo estadístico y explorando la distribución normal de tus datos!
