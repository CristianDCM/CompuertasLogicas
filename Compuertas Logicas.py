from tkinter import *
import operator

root = Tk()
root.title("Compuertas Logicas")
root.geometry("400x400")

frameBtn = Frame(root, width=100, height=100, bd=1, relief="solid")
frameBtn.pack(side="left", anchor="n")
labelBtn = Label(frameBtn, text="Compuertas Logicas")
imgAND = PhotoImage(file="imgCompuertas/and.png")
btnAND = Button(frameBtn, image=imgAND)
btnAND.config(command=lambda: changeImageGate("imgCompuertas/and.png"))
imgOR = PhotoImage(file="imgCompuertas/or.png")
btnOR = Button(frameBtn, image=imgOR)
btnOR.config(command=lambda: changeImageGate("imgCompuertas/or.png"))
imgNOT = PhotoImage(file="imgCompuertas/not.png")
btnNOT = Button(frameBtn, image=imgNOT)
btnNOT.config(command=lambda: changeImageGate("imgCompuertas/not.png"))
imgNAND = PhotoImage(file="imgCompuertas/nand.png")
btnNAND = Button(frameBtn, image=imgNAND)
btnNAND.config(command=lambda: changeImageGate("imgCompuertas/nand.png"))
imgNOR = PhotoImage(file="imgCompuertas/nor.png")
btnNOR = Button(frameBtn, image=imgNOR)
btnNOR.config(command=lambda: changeImageGate("imgCompuertas/nor.png"))
imgXOR = PhotoImage(file="imgCompuertas/xor.png")
btnXOR = Button(frameBtn, image=imgXOR)
btnXOR.config(command=lambda: changeImageGate("imgCompuertas/xor.png"))
imgXNOR = PhotoImage(file="imgCompuertas/xnor.png")
btnXNOR = Button(frameBtn, image=imgXNOR)
btnXNOR.config(command=lambda: changeImageGate("imgCompuertas/xnor.png"))

labelBtn.pack()
btnAND.pack()
btnOR.pack()
btnNOT.pack()
btnNAND.pack()
btnNOR.pack()
btnXOR.pack()
btnXNOR.pack()
frameBtn.pack()

frameBoard = Frame(root, width=300, height=289, bd=1, relief="solid")
frameBoard.pack(side="left", anchor="n")
frameBoard.pack_propagate(False)

imgConstOFF = PhotoImage(file="imgCompuertas/constoff.png")
imgConstON = PhotoImage(file="imgCompuertas/conston.png")

btn1 = Button(frameBoard, image=imgConstOFF)
btn1.place(x=20, y=50)
btn2 = Button(frameBoard, image=imgConstOFF)
btn2.place(x=20, y=100)

def changeImageGate(img):
    global imgCompuertaDefault
    imgCompuertaDefault = PhotoImage(file=img)
    labelCompuertaDefault.config(image=imgCompuertaDefault)

imgCompuertaDefault = PhotoImage(file="imgCompuertas/and.png")
labelCompuertaDefault = Label(frameBoard, image=imgCompuertaDefault)
labelCompuertaDefault.place(x=90, y=75)
imgOutON = PhotoImage(file="imgCompuertas/outon.png")
imgOutOFF = PhotoImage(file="imgCompuertas/outoff.png")

def binaryGate(a, b, gate):
    logic = {"and": operator.and_, "or": operator.or_, "nand": operator.and_, "nor": operator.or_, "xor": operator.xor, "xnor": operator.xor}
    return logic[gate](a, b)

LabelOut = Label(frameBoard, image=imgOutOFF)
LabelOut.place(x=150, y=75)###Salida

btn1On = False
btn2On = False

def changeImage1():
    global btn1On
    if btn1On:
        btn1.config(image=imgConstOFF)
        btn1On = False
    else:
        btn1.config(image=imgConstON)
        btn1On = True

def changeImage2():
    global btn2On
    if btn2On:
        btn2.config(image=imgConstOFF)
        btn2On = False
    else:
        btn2.config(image=imgConstON)
        btn2On = True

btn1.config(command=changeImage1)
btn2.config(command=changeImage2)

root.mainloop()