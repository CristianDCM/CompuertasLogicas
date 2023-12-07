from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import CompuertasLogicas

def validacion(Select = 1):
    if Select == 1:
        try:
            int(entrada1.get())
            if int(entrada1.get()) < 0:
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
            if varDecimal.get() == 1: # Si es binario
                int(entrada1.get(), 2)   # Se convierte a decimal
            elif varDecimal.get() == 2:   # Si es octal
                int(entrada1.get(), 8)  # Se convierte a decimal
            elif varDecimal.get() == 3:     # Si es hexadecimal
                int(entrada1.get(), 16)  # Se convierte a decimal
            return True
        except ValueError as x:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")
            entrada1.delete(0, END)
            print(x)
            return False

def conversion():
    seleccion = varOpcion.get() 
    varValor.set(opciones[seleccion]) 
    if varValor.get() == 1:
        if validacion():
            if varDecimal.get() == 1: 
                resultado = bin(int(entrada1.get()))
                resultado = resultado[2:]
                labelResultado.config(text= resultado)
            elif varDecimal.get() == 2:
                resultado = oct(int(entrada1.get()))
                resultado = resultado[2:]
                labelResultado.config(text=resultado)
            elif varDecimal.get() == 3:
                resultado = hex(int(entrada1.get()))
                resultado = resultado[2:]
                labelResultado.config(text=resultado)
    elif varValor.get() == 2:
        if validacion(varValor.get()):
            if varDecimal.get() == 1:
                resultado = int(entrada1.get(), 2)
                labelResultado.config(text=str(resultado))
            elif varDecimal.get() == 2:
                resultado = int(entrada1.get(), 8)
                labelResultado.config(text=str(resultado))
            elif varDecimal.get() == 3:
                resultado = int(entrada1.get(), 16)
                labelResultado.config(text=str(resultado))

def compuertasLogicas():
    CompuertasLogicas.main()
    
root = Tk()
root.title("Conversiones decimales a binario, octal y hexadecimal")
root.resizable(True,True)
root.geometry("500x270")
frame1 = Frame(root)
frame1.config(bd=2,relief="groove")
frame1.pack(side="left")

frame1.pack()
label = Label(frame1, text="Seleccione una conversión: ")
label.pack()
opciones = {"Decimal a digital":1, "Digital a decimal":2}
varValor = IntVar()
varOpcion = StringVar()
comboDecimal = Combobox(frame1, textvariable=varOpcion, state="readonly")
comboDecimal["values"] = list(opciones.keys()) 
comboDecimal.current(0)
comboDecimal.pack()
label1 = Label(frame1, text="Ingrese un número:")
label1.pack()
entrada1 = Entry(frame1) 
entrada1.pack()
varDecimal = IntVar()
label2 = Label(frame1, text="Seleccione una opción:")
label2.pack()
radioBinario = Radiobutton(frame1, text="Binario", variable=varDecimal, value=1)
radioBinario.select()
radioBinario.pack(anchor="w")
radioOctal = Radiobutton(frame1, text="Octal", variable=varDecimal, value=2)
radioOctal.pack(anchor="w")
radioHexadecimal = Radiobutton(frame1, text="Hexadecimal", variable=varDecimal, value=3)
radioHexadecimal.pack(anchor="w")
labelResultado = Label(frame1, text="Resultado", bd=5)
labelResultado.config(width=20, fg="blue") 
labelResultado.pack()
btnConvertir = Button(frame1, text="Conversion", command=conversion)
btnConvertir.pack()
btnCompuertasLogic = Button(frame1, text="Compuertas Logicas", command=compuertasLogicas)
btnCompuertasLogic.pack()
frame2 = Frame(root)
frame2.config(bd=2,relief="groove")
frame2.pack(side="right")
label = Label(frame2, text="Tabla de conversiones")
label.pack()
tabla = Text(frame2)
tabla.config(width=40, height=10)
tabla.pack()
tabla.insert(INSERT, "Decimal\tBinario\tOctal\tHexadecimal\n")

for i in range(1, 500):
    tabla.insert(INSERT, str(i) + "\t" + str(bin(i))[2:] + "\t" + str(oct(i))[2:] + "\t" + str(hex(i))[2:] + "\n")

root.mainloop()