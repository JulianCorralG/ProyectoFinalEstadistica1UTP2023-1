import pandas as pd  # Importar la biblioteca pandas para trabajar con datos de Excel
import numpy as np  # Importar la biblioteca numpy para cálculos numéricos
import matplotlib.pyplot as plt  # Importar la biblioteca matplotlib para graficar
import tkinter as tk  # Importar la biblioteca tkinter para crear la interfaz gráfica
from tkinter import filedialog, messagebox, OptionMenu  # Importar módulos específicos de tkinter
from scipy.stats import norm  # Importar la función de distribución normal de scipy.stats

from elevenlabs import generate, play, set_api_key
from ffpyplayer.player import MediaPlayer

# Crea un cuenta en elevenlabs para obtener una API key https://beta.elevenlabs.io/
# El paso anterior es necesario si quieres que el aplicativo estadistico tenga audio.
#set_api_key("<YOUR_API_KEY>") # Cambia "<YOUR_API_KEY>" por tu API key




# Función para calcular la distribución normal de la columna seleccionada
def calcular_distribucion():
    hoja_seleccionada = variable_hoja.get()
    columna_seleccionada = variable_columna.get()
    valor_x = entry_x.get()
    
    # Mensaje de alerta si la hoja es "Seleccione una hoja"
    if hoja_seleccionada == "Seleccione una hoja":
        ###ventana_principal.after(200, reproducir_audio_hojaNOvalida)  # Reproducir audio después de 1 segundo = 1000
        messagebox.showinfo("Error", "Por favor, seleccione una hoja válida.")
        return

    # Mensaje de alerta si la columna es "Seleccioine una columna"
    if columna_seleccionada == "Seleccione una columna":
        ###ventana_principal.after(200, reproducir_audio_columnaNOvalida)  # Reproducir audio después de 1 segundo = 1000
        messagebox.showinfo("Error", "Por favor, seleccione una columna válida.")
        return
    
    # Mensaje de alerta si no se ha ingresado nada en el valor de x
    if valor_x == "":
    #if isinstance(valor_x, str):
        ###ventana_principal.after(200, reproducir_audio_xNOvalida)  # Reproducir audio después de 1 segundo = 1000
        messagebox.showwarning("Valor no ingresado", "Por favor, ingresa un valor de x.")
        return
    
    # Toma el valor de x en la ventana
    valor_x = float(valor_x)


    # Datos de muestra
    datos = df[hoja_seleccionada][columna_seleccionada].values
    media = np.mean(datos)
    desviacion_estandar = np.std(datos)
    
    if valor_x not in datos:
        messagebox.showwarning("Valor no válido", "El valor de x no está en la columna seleccionada.")
        return

    #z = (valor_x - media) / desviacion_estandar
    z = round((valor_x - media) / desviacion_estandar, 2)


    # Rango de valores para Z
    z_values = np.linspace(-4, 4, 100)

    # Calcular las probabilidades para Z
    prob_values = norm.pdf(z_values)

    # Calcular el porcentaje de área sombreada de z
    probabilidad_z_left = norm.cdf(z)
    probabilidad_z_right = 1 - norm.cdf(z)

    # Calcular el porcentaje de área sombreada de z 
    area_sombreada_left = probabilidad_z_left * 100
    area_sombreada_right = probabilidad_z_right * 100

    # Crear una nueva figura y subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Gráfica 1: Campana de Gauss sin estandarizada
    x = np.linspace(media - 3 * desviacion_estandar, media + 3 * desviacion_estandar, 100)
    y = norm.pdf(x, media, desviacion_estandar)

    # Graficar la distribución normal
    ax1.plot(x, y, color = 'red', label='Distribución Normal')
    # Agregar una línea punteada en el centro de la campana
    ax1.axvline(media, color='orange', linestyle='dashed', label='Media, Mediana y Moda')
    ax1.axvline(valor_x, color='blue', linestyle='solid', linewidth=3, label='valor de x')
    ax1.fill_between(x[x <= valor_x], y[x <= valor_x], color='blue', alpha=0.3, label='Área sombreada')

    # Crear una lista de strings para el texto de la leyenda
    legend_text = [
        f'x~N(μ , σ)',
        '',
        f'{valor_x}~N({media:.4f} , {desviacion_estandar:.4f})',
        f'x = {valor_x}',
        f'Media(μ) = {media:.4f}',
        f'Desv. est.(σ) = {desviacion_estandar:.4f}',
        '',
        'Área Sombreada:',
        f'P(X <= {valor_x}) = {probabilidad_z_left:.4f}',
        f'Porcentaje Área sombreada = {area_sombreada_left:.2f}%',
        '',
        'Área SIN Sombrear:',
        f'P(X > {valor_x}) = {probabilidad_z_right:.4f}',
        f'Porcentaje Área SIN sombrear = {area_sombreada_right:.2f}%',
    ]

    # Graficar la distribución normal con la leyenda personalizada
    ax1.plot(x, y, color='red', label='\n'.join(legend_text))



    ax1.set_xlabel('X')
    ax1.set_ylabel('Densidad de probabilidad')
    ax1.set_title('Campana de Gauss sin estandarizar con área sombreada')
    ax1.legend(loc='upper right', fontsize='small')  # Ubicar la leyenda en la esquina superior derecha
    ax1.grid(True)

    # Gráfica 2: Campana de Gauss estandarizada
    ax2.plot(z_values, prob_values, color='blue', label='Distribución Normal Estandar')
    ax2.axvline(0, color='magenta', linestyle='dashed', linewidth=1, label='Media, Mediana y Moda')
    ax2.axvline(z, color='red', linestyle='solid', linewidth=3, label='valor de z')
    ax2.fill_between(z_values[z_values <= z], prob_values[z_values <= z], color='red', alpha=0.3, label='Área sombreada P(Z <= z)')
    ##ax2.text(-4, 0.10, f'x = {valor_x}\nMedia(μ) = {media:.4f}\nDesv. est.(σ) = {desviacion_estandar:.4f}\nz = (x - μ)/σ\nz =({valor_x} - {media:.4f}) / {desviacion_estandar:.4f}\nz = {z:.2f}\n\nÁrea Sombreada:\nP(Z <= {z:.2f})= {probabilidad_z_left:.4f}\nPorcentaje Área sombreada = {area_sombreada_left:.2f}%\n\nÁrea SIN Sombrear:\nP(Z > {z:.2f})= {probabilidad_z_right:.4f}\nPorcentaje Área SIN sombrear = {area_sombreada_right:.2f}%')
    #ax2.text(-4, 0.20, f'Área SIN Sombrear:\nP(Z > {z:.2f})= {probabilidad_z_right:.4f}\nPorcentaje Área SIN sombrear = {area_sombreada_right:.2f}%')
    
    
    # Crear una lista de strings para el texto de la leyenda
    legend_text = [
        f'z~N(0 , 1)',
        '',
        f'z = (x - μ)/σ',
        f'z = ({valor_x} - {media:.4f}) / {desviacion_estandar:.4f}',
        f'z = {z:.2f}',
        f'z = {z:.2f}',
        '',
        'Área Sombreada:',
        f'P(Z <= {z:.2f}) = {probabilidad_z_left:.4f}',
        f'Porcentaje Área sombreada = {area_sombreada_left:.2f}%',
        '',
        'Área SIN Sombrear:',
        f'P(Z > {z:.2f}) = {probabilidad_z_right:.4f}',
        f'Porcentaje Área SIN sombrear = {area_sombreada_right:.2f}%'
    ]

    # Graficar la distribución normal con la leyenda personalizada
    ax2.plot(z_values, prob_values, color='blue', label='\n'.join(legend_text))
    
    
    ax2.set_xlabel('Z')
    ax2.set_ylabel('Densidad de probabilidad')
    ax2.set_title('Campana de Gauss estandarizada con área sombreada')
    ax2.legend(loc='upper right', fontsize='small', handlelength=2, frameon=True)  # Ubicar la leyenda en la esquina superior derecha y letra pequeña
    ax2.grid(True)

    #ventana_principal.after(200, reproducir_audio_grafica)  # Reproducir audio después de 1 segundo = 1000


    # Mostrar las gráficas
    plt.tight_layout()
    plt.show() 

# Función para confirmar el cierre del programa
def confirmar_cierre():
    
    ###ventana_principal.after(200, reproducir_audio_confirmacioncierre)  # Reproducir audio después de 1 segundo = 1000
    ###ventana_principal.after(200, reproducir_audio_despedida)  # Reproducir audio después de 1 segundo = 1000
    if messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas cerrar el programa?"):
        ventana_principal.destroy()
        ventana_inicio.destroy()


# Función para abrir el archivo de Excel y seleccionar la hoja
def abrir_archivo():
    
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo de Excel", filetypes=[("Archivos de Excel", "*.xlsx")])
    if ruta_archivo:
        try:
            
            # Leer todas las hojas del archivo Excel
            global df
            df = pd.read_excel(ruta_archivo, sheet_name=None)
            hojas = ["Seleccione una hoja"] + list(df.keys())
            variable_hoja.set(hojas[0])  # Establecer opción "Seleccione una hoja" como opción predeterminada
            menu_hoja['menu'].delete(0, 'end')
            for hoja in hojas:
                # Agregar las hojas al menú desplegable
                menu_hoja['menu'].add_command(label=hoja, command=lambda hoja=hoja: seleccionar_hoja(hoja))

            

            seleccionar_hoja("Seleccione una hoja")  # Actualizar las columnas del menú para la opción "Seleccione una hoja"
            ventana_inicio.withdraw()  # Ocultar la primera ventana
            ventana_principal.deiconify()  # Mostrar la ventana principal
            ###ventana_principal.after(200, reproducir_audio_ventana_principal)  # Reproducir audio después de 1 segundo = 1000
        except Exception as e:
            #ventana_principal.after(200, reproducir_audio_archivoNOabierto)  # Reproducir audio después de 1 segundo = 1000
            messagebox.showinfo("Error", f"No se pudo abrir el archivo:\n{e}")

# Función para actualizar los datos mostrados en pantalla
def actualizar_datos():
    hoja_seleccionada = variable_hoja.get()
    if hoja_seleccionada != "" and hoja_seleccionada != "Seleccione una hoja":
        tabla = df[hoja_seleccionada].to_string(index=False, justify='center')
        texto_datos.delete(1.0, tk.END)
        texto_datos.insert(tk.END, tabla)

# Función para seleccionar una hoja y actualizar las columnas disponibles en el menú
def seleccionar_hoja(hoja):
    variable_hoja.set(hoja)
    if hoja != "Seleccione una hoja":
        columnas = df[hoja].columns.tolist()
        variable_columna.set(columnas[0])  # Establecer la primera columna como opción predeterminada
    else:
        columnas = []
        variable_columna.set("Seleccione una columna")  # Restablecer la opción predeterminada
    menu_columna['menu'].delete(0, 'end')
    for columna in columnas:
        menu_columna['menu'].add_command(label=columna, command=lambda columna=columna: variable_columna.set(columna))
    actualizar_datos()  # Actualizar los datos mostrados en pantalla

def reproducir_audio_bienvenida():
    audio = generate(
        text="Hola mi nombre es Martin, te doy la bienvenida a el proyecto final del estudian Julian Andres Corral Gomez (quien me dio vida), este proyecto es un aplicativo estadistico amigable con el usuario (¿a poco no he sido amable contigo?). Perdoname la introduccion un poco larga, Para iniciar, por favor busca y abre el archivo de Excel con el que deseas trabajar. Mientras tanto te estaré esperando, tomate tu tiempo",
        voice="Antoni",
        model='eleven_multilingual_v1'
    )
    play(audio)

def reproducir_audio_ventana_principal():
    audio = generate(
        text="Muy bien, ahora es necesario que selecciones una hoja de tu archivo de excel, luego deberas elejir una columna y por ultimo ingresar por teclado un valor en el rango de valores de la columna. Para ver dos gráficas, una de la distribucion normal y otra estandarizada dale click al boton calcular distribucion normal estandar",
        voice="Antoni",
        model='eleven_multilingual_v1'
    )
    play(audio)

def reproducir_audio_despedida():
    audio = generate(
        text="Para cerrar el programa debes decirme cuanto es sesenta y seis más cuarenta y cuatro jajaja, es broma y no, no es cien. Ha sido un gusto acompañarte, ya sabes donde encontrarme, hasta pronto.",
        voice="Antoni",
        model='eleven_multilingual_v1'
    )
    play(audio)

def reproducir_audio_archivoNOabierto():
    audio = generate(
        text="NOarchivo",#"Parece que hubo un problema al tratar de abrir el archivo. Por favor, intentalo de nuevo",
        voice="Antoni",
        model='eleven_multilingual_v1'
    )
    play(audio)

def reproducir_audio_confirmacioncierre():
    audio = generate(
        text="¿Estás seguro de que deseas cerrar el programa?",
        voice="Antoni",
        model='eleven_multilingual_v1'
    )
    play(audio)

def reproducir_audio_hojaNOvalida():
    audio = generate(
        text="Lo siento, pero es necesario una hoja valida para trabajar, ¿Estás seguro de que seleccionaste una hoja válida?",
        voice="Antoni",
        model='eleven_multilingual_v1'
    )
    play(audio)

def reproducir_audio_columnaNOvalida():
    audio = generate(
        text="Lo siento, pero es necesario una columna valida para trabajar, ¿Estás seguro de que elejiste una columna válida?",
        voice="Antoni",
        model='eleven_multilingual_v1'
    )
    play(audio)

def reproducir_audio_xNOvalida():
    audio = generate(
        text="Lo siento, algo esta ocasionando problemas con el valor de x, ¿Estás seguro de que el valor de x esta en la columna seleccionada?",
        voice="Antoni",
        model='eleven_multilingual_v1'
    )
    play(audio)

def reproducir_audio_grafica():
    audio = generate(
        text="En pantalla se visualizan dos gráficas, al lado izquierdo esta la gráfica de los datos sin estandarizar y al lado derecho esta la gráfica de los datos estandarizados. Como puedes ver, la grafica de la izquierda no es tan punteaguda como la gráfica de la derecha que esta estandarizada (recuerda que estandarizada significa que trabajas con una media de cero y desviacion estandar uno), además esta sombreado el área bajo la curva (esto indica la probabilidad probabilidad) Respecto a valores menores o iguales a la variable equis (gráfica de la izquierda) o zeta (gráfica de la derecha). Tambien hay una leyenda que muestra un tipo de linea de diferente color con una breve descripcion a lo que hace referencia.",
        voice="Antoni",
        model='eleven_multilingual_v1'
    )
    play(audio)




# Crear la primera ventana
ventana_inicio = tk.Tk()
ventana_inicio.title("Carga de datos de Excel")
ventana_inicio.geometry("400x300")
###ventana_inicio.after(200, reproducir_audio_bienvenida)  # Reproducir audio después de 1 segundo = 1000

# Titulo de la ventana inicio
etiqueta_inicio = tk.Label(ventana_inicio, text="Bienvenido,\npara iniciar por favor\nbusque y abra el archivo de Excel \ncon el que desea trabajar", font=("Arial", 14))
etiqueta_inicio.pack()

# Agregar un botón para buscar el archivo
boton_buscar_archivo = tk.Button(ventana_inicio, text="Buscar archivo", command=abrir_archivo)
boton_buscar_archivo.pack(pady=50)

# Asignar la función confirmar_cierre al intentar cerrar la ventana
ventana_inicio.protocol("WM_DELETE_WINDOW", confirmar_cierre)

# Crear la segunda ventana y ocultarla inicialmente
ventana_principal = tk.Toplevel()
ventana_principal.title("Distribucion Normal -> distribucion normal estandar")
ventana_principal.withdraw()

# Titulo de la ventana principal
etiqueta1 = tk.Label(ventana_principal, text="Presentación de los datos del archivo de Excel")
etiqueta1.pack()

# Se muestran los datos del archivo de Excel en la ventana principal
texto_datos = tk.Text(ventana_principal)
texto_datos.pack()

# Crear el menú desplegable para la hoja del archivo
variable_hoja = tk.StringVar(ventana_principal)
menu_hoja = OptionMenu(ventana_principal, variable_hoja, "Seleccione una hoja")
menu_hoja.pack()

# Crear el menú desplegable para seleccionar la columna deseada
variable_columna = tk.StringVar(ventana_principal)
menu_columna = OptionMenu(ventana_principal, variable_columna, "Seleccione una columna")
menu_columna.pack()

# mensaje para ingresar el valor de x mostrado en la ventana principal
etiqueta_x = tk.Label(ventana_principal, text="Valor de x:")
etiqueta_x.pack()

entry_x = tk.Entry(ventana_principal)
entry_x.pack()

# Crear el botón para calcular la distribución normal
boton_calcular = tk.Button(ventana_principal, text='Calcular Distribución Normal Estandar Z~N(0,1)', command=calcular_distribucion)
boton_calcular.pack()

# Asignar la función confirmar_cierre al intentar cerrar la ventana
ventana_principal.protocol("WM_DELETE_WINDOW", confirmar_cierre)

ventana_inicio.mainloop()
