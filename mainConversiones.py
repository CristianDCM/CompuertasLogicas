from tkinter import *; from tkinter import messagebox; from tkinter.ttk import Combobox
import subprocess; import sys 

def validacion(Select=1):
    entrada = entrada1.get()
    if Select == 1:
        try:
            num = int(entrada)
            if num < 0:
                messagebox.showerror("Error", "Por favor, ingrese un número positivo.")
                entrada1.delete(0, END)
                return False
            return True
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")
            entrada1.delete(0, END)
            return False
    if Select == 2:
        try:
            baseMap = {1: 2, 2: 8, 3: 16} # Mapa de bases
            base = baseMap.get(varDecimal.get()) # Obtiene la base seleccionada
            if base: # Si la base es valida
                int(entrada, base) # Intenta convertir la entrada a la base seleccionada
            return True # Si no hay error, retorna True
        except ValueError as x:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")
            entrada1.delete(0, END)
            print(x)
            return False

def conversion():
    entrada = entrada1.get() # Obtiene la entrada (número a convertir)
    varValor.set(opciones[varOpcion.get()]) # Obtiene el valor de la opción seleccionada(Decimal a digital o digital a decimal)
    if varValor.get() == 1: # Si la opción seleccionada es Decimal a digital
        if validacion(): # Si la entrada es válida
            conversionMap = {1: bin, 2: oct, 3: hex} # Mapa de conversiones 
            conversionFunc = conversionMap.get(varDecimal.get()) # Obtiene la función de conversión
            if conversionFunc: # Si la función es válida
                resultado = conversionFunc(int(entrada)) # Convierte la entrada a la base seleccionada
                resultado = resultado[2:] # Elimina el prefijo de la conversión 0b, 0o o 0x
                labelResultado.config(text=resultado) # Muestra el resultado en la etiqueta
                actualizarTabla() # Actualiza la tabla de conversiones
    elif varValor.get() == 2:
        if validacion(varValor.get()):
            baseMap = {1: 2, 2: 8, 3: 16}
            base = baseMap.get(varDecimal.get())
            if base:
                resultado = int(entrada, base)
                labelResultado.config(text=str(resultado))
                actualizarTabla()

def compuertasLogicas():
    subprocess.Popen([sys.executable, "CompuertasLogicas.py"])

root = Tk()
root.title("Conversiones - Compuertas Logicas")
root.resizable(False, False)
root.geometry("420x240")
barraMenu = Menu(root)
root.config(menu=barraMenu)
opcionesMenu = Menu(barraMenu, tearoff=0)
img = PhotoImage(file="img/logic.png")
opcionesMenu.add_command(label="Compuertas Logicas", command=compuertasLogicas, image=img, compound="left")
barraMenu.add_cascade(label="Menu", menu=opcionesMenu)
root.iconbitmap("img/icono.ico")
frame1 = Frame(root,relief = "groove")
frame1.pack(side="left")
opciones = {"Decimal a Digital": 1, "Digital a Decimal": 2}
varValor = IntVar() # Variable para almacenar el valor de la opción seleccionada
varOpcion = StringVar() # Variable para almacenar la opción seleccionada
varDecimal = IntVar() # Variable para almacenar la base seleccionada (1, 2 o 3)
Label(frame1, text="Seleccione una conversión").pack()
comboDecimal = Combobox(frame1, textvariable=varOpcion, state="readonly", values=list(opciones.keys()))
comboDecimal.current(0)
comboDecimal.pack()
Label(frame1, text="Ingrese un número").pack()
entrada1 = Entry(frame1)
entrada1.pack()
Label(frame1, text="Seleccione una opción").pack()
radioBinario=Radiobutton(frame1, text="Binario", variable=varDecimal, value=1)
radioBinario.select()
radioBinario.pack(anchor="w")
Radiobutton(frame1, text="Octal", variable=varDecimal, value=2).pack(anchor="w")
Radiobutton(frame1, text="Hexadecimal", variable=varDecimal, value=3).pack(anchor="w")
labelResultado = Label(frame1, text="Resultado", bd=5, width=20, fg="blue")
labelResultado.pack()
Button(frame1, text="Conversion", command=conversion).pack()
frame2 = Frame(root, relief="groove")
frame2.pack(side="left")
Label(frame2, text="Tabla de Conversiones", font=("Arial", 10, "bold")).pack()
Label(frame2, text="Decimal  \t|  Binario \t|  Octal  \t|  Hexadecimal", font=("Arial", 10)).pack(anchor="w")
tabla = Text(frame2)
tabla.config(width=32, height=11) 
tabla.pack()

def actualizarTabla():
    tabla.config(state="normal")
    tabla.delete(1.0, END)
    for i in range(1, 300):
        tabla.insert(
            INSERT,str(i)+"\t"+str(bin(i))[2:]+"\t"+str(oct(i))[2:]+"\t"+str(hex(i))[2:]+"\n",)
        #Si es la opcion de decimal a digital igualar el valor de la entrada a la fila de la tabla
        if varValor.get() == 1 and entrada1.get() == str(i):
            tabla.tag_add("colorEntrada", str(i)+".0", str(i)+".100")
            tabla.tag_config("colorEntrada", foreground="white", background="black")
        #Si es la opcion de digital a decimal igualar el valor del resultado a la fila de la tabla
        if varValor.get() == 2 and labelResultado.cget("text") == str(i):
            tabla.tag_add("colorResultado", str(i)+".0", str(i)+".100")
            tabla.tag_config("colorResultado", foreground="white", background="black")
    tabla.config(state="disabled")
actualizarTabla()
root.mainloop()
