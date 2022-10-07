from ast import Try
from ctypes.wintypes import DOUBLE
import tkinter as tk
from tkinter import ttk
from tkinter import *

from tkinter import messagebox as msn
from tokenize import Double
import dicc


clientes = { #DNI -> Datos
    "71950641":{"Nombre": "Steve Rogers", "Apellidos": "Grant Hamilton", "Direccion": " 180 North Michigan Ave., Suite 1500, Chicago, IL 60611", "Telefono": 958625781},
    "71950642":{"Nombre": "María Hill", "Apellidos": "Duff Ferguson", "Direccion": "2375 Pennsylvania Av. NW, 20037 Washington DC", "Telefono": 958625782},
    "71950643":{"Nombre": "Natasha Romanoff", "Apellidos": "Smith Jones", "Direccion": "31 St. James Avenue, Suite 905, Boston, MA 02116", "Telefono": 958625783},
    "71950644":{"Nombre": "Bruce Banner", "Apellidos": "Taylor Brown", "Direccion": "180 North Michigan Ave., Suite 1500, Chicago, IL 60611", "Telefono": 958625784},
    "71950645":{"Nombre": "Thor odinson", "Apellidos": "Johnson Davies", "Direccion": "2655 Le Jeune Road, Suite 203, Miami, FL 33134", "Telefono": 958625785},
    "71950646":{"Nombre": "Jean Steve", "Apellidos": " Wood Harris", "Direccion": "150 East 58th St., 30th Floor, New York, N.Y. 10155", "Telefono": 958625786},
    "71950647":{"Nombre": "Iván Drago", "Apellidos": "Turner Cooper", "Direccion": "1800 Bering Drive, Suite 660, Houston. Texas 77057", "Telefono": 958625787},
    "71950648":{"Nombre": "Clint Barton", "Apellidos": "Ward Hughes", "Direccion": "700, 5TH Avenue, 35th Floor, New York, NY 10103", "Telefono": 958625788},
    "71950649":{"Nombre": "Peggy Carte", "Apellidos": "Bennett Watson", "Direccion": "3160 W Fox Run Way San Diego, florida", "Telefono": 958625789},
    "71950650":{"Nombre": "Tony Stark", "Apellidos": "Downey Jr", "Direccion": "4532 Brian Head StLas Vegas, Las Vegas", "Telefono": 958625780}
}

productos = {
    "COD-001": {
        "NomPro": "Martillo", "Precio": 20
    },
    "COD-002": {
        "NomPro": "Destornillador", "Precio": 15
    },
    "COD-003": {
        "NomPro": "Alicate", "Precio": 21
    },
    "COD-004": {
        "NomPro": "Llave inglesa", "Precio": 16
    },
    "COD-005": {
        "NomPro": "Clavo", "Precio": 0.50
    },
    "COD-006": {
        "NomPro": "Tornillo", "Precio": 0.60
    },
    "COD-007": {
        "NomPro": "Wincha", "Precio": 5
    },
    "COD-008": {
        "NomPro": "Lija", "Precio": 2
    },
    "COD-009": {
        "NomPro": "Foco", "Precio": 9,
    },
    "COD-010": {
        "NomPro": "Serrucho", "Precio": 44.50
    }
}

detalle = {}

# FUNCIONES
def buscarCliente():
    dni = txtDNI.get()
    if dni in dicc.clientes:
        
        txtNombre.delete(0, tk.END)
        txtApe.delete(0, tk.END)
        txtDic.delete(0, tk.END)
        txtTel.delete(0, tk.END)
        

        txtNombre.insert(0, dicc.clientes[dni]["Nombre"])
        txtApe.insert(0, dicc.clientes[dni]["Apellidos"])
        txtDic.insert(0, dicc.clientes[dni]["Direccion"])
        txtTel.insert(0, dicc.clientes[dni]["Telefono"])
    else:
        return msn.showerror("Error", "Cliente no encontrado")

def buscarCliente_(event):
    dni = txtDNI.get()
    if dni in dicc.clientes:
        
        txtNombre.delete(0, tk.END)
        txtApe.delete(0, tk.END)
        txtDic.delete(0, tk.END)
        txtTel.delete(0, tk.END)
        

        txtNombre.insert(0, dicc.clientes[dni]["Nombre"])
        txtApe.insert(0, dicc.clientes[dni]["Apellidos"])
        txtDic.insert(0, dicc.clientes[dni]["Direccion"])
        txtTel.insert(0, dicc.clientes[dni]["Telefono"])
    else:
        return msn.showerror("Error", "Cliente no encontrado")
#
#
# cant = int(cant)

def BusCalSub(event):
    try:
        cod = txtCod1.get()
        cant = int(txtCan1.get())
        
        if cod in dicc.productos:
            txtDes1.delete(0, tk.END)
            txtPre1.delete(0, tk.END)
            txtSub1.delete(0, tk.END)

            txtDes1.insert(0, dicc.productos[cod]["NomPro"])
            txtPre1.insert(0, dicc.productos[cod]["Precio"])

            prec = dicc.productos[cod]["Precio"]
            subTotal = prec * cant
        
            txtSub1.insert(0, subTotal)
        else:
            return msn.showerror("Error", "Producto no encontrado")
    except:
        return msn.showerror("Error", "Falta Código o Cantidad")
        

def BusCalSub2(event):
    try:
        cod = txtCod2.get()
        cant = int(txtCan2.get())
        
        if cod in dicc.productos:
            txtDes2.delete(0, tk.END)
            txtPre2.delete(0, tk.END)
            txtSub2.delete(0, tk.END)

            txtDes2.insert(0, dicc.productos[cod]["NomPro"])
            txtPre2.insert(0, dicc.productos[cod]["Precio"])

            prec = dicc.productos[cod]["Precio"]
            subTotal = prec * cant
        
            txtSub2.insert(0, subTotal)
        else:
            return msn.showerror("Error", "Producto no encontrado")
    except:
        return msn.showerror("Error", "Falta Código o Cantidad")


def BusCalSub3(event):
    try:
        cod = txtCod3.get()
        cant = int(txtCan3.get())
        
        if cod in dicc.productos:
            txtDes3.delete(0, tk.END)
            txtPre3.delete(0, tk.END)
            txtSub3.delete(0, tk.END)
            
            txtDes3.insert(0, dicc.productos[cod]["NomPro"])
            txtPre3.insert(0, dicc.productos[cod]["Precio"])

            prec = dicc.productos[cod]["Precio"]
            subTotal = prec * cant
        
            txtSub3.insert(0, subTotal)
        else:
            return msn.showerror("Error", "Producto no encontrado")
    except:
        return msn.showerror("Error", "Falta Código o Cantidad")

def Guardar():
    dicc.detalle['P-1'] = {"Codigo" :txtCod1.get(), "Nombre": txtDes1.get(), "Precio": txtPre1.get(), "Cantidad": txtCan1.get(), "SubTotal": txtSub1.get()}
    dicc.detalle['P-2'] = {"Codigo" :txtCod2.get(), "Nombre": txtDes2.get(), "Precio": txtPre2.get(), "Cantidad": txtCan3.get(), "SubTotal": txtSub2.get()}
    dicc.detalle['P-3'] = {"Codigo" :txtCod3.get(), "Nombre": txtDes3.get(), "Precio": txtPre3.get(), "Cantidad": txtCan3.get(), "SubTotal": txtSub3.get()}

# eso 1 2 3
def totalVenta():
    txtTotal.delete(0, tk.END)
    sub1 = float(txtSub1.get())
    sub2 = float(txtSub2.get())
    sub3 = float(txtSub3.get())
    Total =  sub1 + sub2 + sub3
    txtTotal.insert(0, Total)
    

def limpiarCliente():
    txtDNI.delete(0, tk.END)
    txtNombre.delete(0, tk.END)
    txtApe.delete(0, tk.END)
    txtDic.delete(0, tk.END)
    txtTel.delete(0, tk.END)


def limpiar1():
    txtCod1.delete(0, tk.END)
    txtDes1.delete(0, tk.END)
    txtPre1.delete(0, tk.END)
    txtCan1.delete(0, tk.END)
    txtSub1.delete(0, tk.END)

def limpiar2():
    txtCod2.delete(0, tk.END)
    txtDes2.delete(0, tk.END)
    txtPre2.delete(0, tk.END)
    txtCan2.delete(0, tk.END)
    txtSub2.delete(0, tk.END)

def limpiar3():
    txtCod3.delete(0, tk.END)
    txtDes3.delete(0, tk.END)
    txtPre3.delete(0, tk.END)
    txtCan3.delete(0, tk.END)
    txtSub3.delete(0, tk.END)


# RAIZ
raiz = Tk()

raiz.title("Ferrretería 'El Tornillo Feliz'")
raiz.iconbitmap("./Semana3/logo.ico")
#raiz.config(bg="grey")

#raiz.config(relief="groove")
#raiz.config(bd=100)

# FRAME
miFrame = Frame(raiz)
miFrame.pack(fill='both', expand="True")

color = "#82E0AA"
miFrame.config(bg=color)
miFrame.config(width="700", height="350")

# LABEL Y txt Cliente
lblTitulo = ttk.Label(miFrame, text="Ferrretería 'El Tornillo Feliz'", font='Currier')
lblTitulo.grid(padx=5, pady=5, column=0, row=0, columnspan=7)

lblDNI = ttk.Label(miFrame, text="DNI:", width=20)
lblDNI.grid(padx=5, pady=5, column=0, row=1, sticky="e")
txtDNI = ttk.Entry(miFrame, width=45)
txtDNI.grid(padx=5, pady=5, column=1, row=1, columnspan=2,sticky="w")
txtDNI.bind('<Return>', buscarCliente_)



lblNombre = ttk.Label(miFrame, text="Nombres:", width=20)
lblNombre.grid(padx=5, pady=5, column=0, row=2, sticky="e")
txtNombre = ttk.Entry(miFrame, width=45)
txtNombre.grid(padx=5, pady=5, column=1, row=2, columnspan=2, sticky="w")

lblApe = ttk.Label(miFrame, text="Apellidos:", width=20)
lblApe.grid(padx=5, pady=5, column=3, row=2, sticky="e")
txtApe = ttk.Entry(miFrame, width=45)
txtApe.grid(padx=5, pady=5, column=4, row=2, columnspan=2,sticky="w")

lblDic = ttk.Label(miFrame, text="Dirección:", width=20)
lblDic.grid(padx=5, pady=5, column=0, row=3, sticky="e")
txtDic = ttk.Entry(miFrame, width=95)
txtDic.grid(padx=5, pady=5, column=1, row=3, columnspan=4, sticky="w")

lblTel = ttk.Label(miFrame, text="Teléfono:", width=20)
lblTel.grid(padx=5, pady=5, column=3, row=1, sticky="e")
txtTel = ttk.Entry(miFrame, width=45)
txtTel.grid(padx=5, pady=5, column=4, row=1, columnspan=2,sticky="w")

btnDellimpclien = ttk.Button(
    miFrame, text="Limpiar", width=20, command=lambda: limpiarCliente())
btnDellimpclien.grid(padx=5, pady=5, column=5, row=3, sticky="w")
# PRODUCTOS

lblTitulo = ttk.Label(miFrame, text="Lista de productos")
lblTitulo.grid(padx=5, pady=5, column=0, row=4, columnspan=6)


lblCod = ttk.Label(miFrame, text="Cod. Prod", width=20)
lblCod.grid(padx=5, pady=5, column=0, row=5, sticky="e")

lblDes = ttk.Label(miFrame, text="Descripción", width=20)
lblDes.grid(padx=5, pady=5, column=1, row=5, sticky="e")


lblPre = ttk.Label(miFrame,text="Precio", width=20)
lblPre.grid(padx=5, pady=5, column=2, row=5, sticky="e")

lblCan = ttk.Label(miFrame,text="Cantidad", width=20)
lblCan.grid(padx=5, pady=5, column=3, row=5, sticky="e")

lblSub = ttk.Label(miFrame, text="SubTotal", width=20)
lblSub.grid(padx=5, pady=5, column=4, row=5, sticky="e")


# Fila de Productos
# FILA 1
btnDel1 = ttk.Button(miFrame, text="Limpiar", width=20, command=lambda: limpiar1())
btnDel1.grid(padx=5, pady=5, column=5, row=7, sticky="w")

txtCod1 = ttk.Entry(miFrame, width=20)
txtCod1.grid(padx=5, pady=5, column=0, row=7, sticky="e")
txtCod1.bind('<Return>', BusCalSub)

txtDes1 = ttk.Entry(miFrame, width=20)
txtDes1.grid(padx=5, pady=5, column=1, row=7, sticky="e")

txtPre1 = ttk.Entry(miFrame, width=20)
txtPre1.grid(padx=5, pady=5, column=2, row=7, sticky="e")

txtCan1 = ttk.Entry(miFrame, width=20)
txtCan1.grid(padx=5, pady=5, column=3, row=7, sticky="e")
txtCan1.bind('<Return>', BusCalSub)

txtSub1 = ttk.Entry(miFrame, width=20)
txtSub1.grid(padx=5, pady=5, column=4, row=7, sticky="e")


# FILA 2
btnDel2 = ttk.Button(miFrame, text="Limpiar", width=20, command=lambda: limpiar2())
btnDel2.grid(padx=5, pady=5, column=5, row=8, sticky="w")

txtCod2 = ttk.Entry(miFrame, width=20)
txtCod2.grid(padx=5, pady=5, column=0, row=8, sticky="e")
txtCod2.bind('<Return>', BusCalSub2)

txtDes2 = ttk.Entry(miFrame, width=20)
txtDes2.grid(padx=5, pady=5, column=1, row=8, sticky="e")

txtPre2 = ttk.Entry(miFrame, width=20)
txtPre2.grid(padx=5, pady=5, column=2, row=8, sticky="e")

txtCan2 = ttk.Entry(miFrame, width=20)
txtCan2.grid(padx=5, pady=5, column=3, row=8, sticky="e")
txtCan2.bind('<Return>', BusCalSub2)

txtSub2 = ttk.Entry(miFrame, width=20)
txtSub2.grid(padx=5, pady=5, column=4, row=8, sticky="e")

# FILA 3
btnDel3 = ttk.Button(miFrame, text="Limpiar", width=20, command=lambda: limpiar3())
btnDel3.grid(padx=5, pady=5, column=5, row=9, sticky="w")

txtCod3 = ttk.Entry(miFrame, width=20)
txtCod3.grid(padx=5, pady=5, column=0, row=9, sticky="e")
txtCod3.bind('<Return>', BusCalSub3)

txtDes3 = ttk.Entry(miFrame, width=20)
txtDes3.grid(padx=5, pady=5, column=1, row=9, sticky="e")

txtPre3 = ttk.Entry(miFrame, width=20)
txtPre3.grid(padx=5, pady=5, column=2, row=9, sticky="e")

txtCan3 = ttk.Entry(miFrame, width=20)
txtCan3.grid(padx=5, pady=5, column=3, row=9, sticky="e")
txtCan3.bind('<Return>', BusCalSub3)

txtSub3 = ttk.Entry(miFrame, width=20)
txtSub3.grid(padx=5, pady=5, column=4, row=9, sticky="e")

#TOTAL
lblTotal = ttk.Label(miFrame, text="Total", width=20)
lblTotal.grid(padx=5, pady=5, column=5, row=10, sticky="e")

txtTotal = ttk.Entry(miFrame, width=20)
txtTotal.grid(padx=5, pady=5, column=5, row=11, sticky="e")


btnTotal = ttk.Button(miFrame, text='Calcular', command=lambda:totalVenta())
btnTotal.grid(padx=5, pady=5, column=4, row=11)


btnBuscar = ttk.Button(miFrame, text='Buscar', command=lambda:buscarCliente())
btnBuscar.grid(padx=5, pady=5, column=0, row=11)

btnGuardar = ttk.Button(miFrame, text='Guardar', command=lambda: Guardar())
btnGuardar.grid(padx=5, pady=5, column=2, row=11)

# Guardar, Borrar, Salir




raiz.mainloop()