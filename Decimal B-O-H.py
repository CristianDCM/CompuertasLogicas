from tkinter import *

root = Tk()
root.title("Conversiones decimales a binario, octal y hexadecimal")
root.geometry("500x250")
root.resizable(False,False)

#Frame para convertir de decimal a binario
frame1 = Frame(root)
frame1.pack()
frame1.config(width=500, height=250)
label1 = Label(frame1, text="Decimal a Binario")
label1.pack()
entrada1 = Entry(frame1)
entrada1.pack()

def converDecBin():
    numero = int(entrada1.get())
    binario = bin(numero)
    salida1.config(text=binario[2:])

boton1 = Button(frame1, text="Convertir", command=converDecBin)
boton1.pack()
salida1 = Label(frame1, text="")
salida1.pack()

#Frame para convertir de decimal a octal
frame2 = Frame(root)
frame2.config()
frame2.pack()
frame2.config(width=500, height=250)
label2 = Label(frame2, text="Decimal a Octal")
label2.pack()
entrada2 = Entry(frame2)
entrada2.pack()

def converDecOct():
    numero = int(entrada2.get())
    octal = oct(numero)
    salida2.config(text=octal[2:])

boton2 = Button(frame2, text="Convertir", command=converDecOct)
boton2.pack()
salida2 = Label(frame2, text="")
salida2.pack()

#Frame para convertir de decimal a hexadecimal
frame3 = Frame(root)
frame3.pack()
frame3.config(width=500, height=250)
label3 = Label(frame3, text="Decimal a Hexadecimal")
label3.pack()
entrada3 = Entry(frame3)
entrada3.pack()

def converDecHex():
    numero = int(entrada3.get())
    hexadecimal = hex(numero)
    salida3.config(text=hexadecimal[2:])

boton3 = Button(frame3, text="Convertir", command=converDecHex)
boton3.pack()
salida3 = Label(frame3, text="")
salida3.pack()

root.mainloop()