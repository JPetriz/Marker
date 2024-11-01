from tkinter import *

FILA_0_HEIGHT = 50
FILA_1_HEIGHT = 80
FILA_2_HEIGHT = 80
FILA_3_HEIGHT = 150
FILA_4_HEIGHT = 50


root = Tk()
root.title("Verificacion de Cordones")
root.geometry("800x600")

# Frames Fila 0
frame_fila_0 = Frame(root, width=800, height=FILA_0_HEIGHT, borderwidth=1, relief="flat")
frame_fila_0.pack_propagate(False)
frame_fila_0.pack()

encabezado = Label(frame_fila_0, text="Verificacion de cordones y marcado de pieza", font=("Arial", 20))
encabezado.pack()


# Frames Fila 1
frame_fila_1 = Frame(root, width=800, height=FILA_1_HEIGHT, borderwidth=1, relief="flat")
frame_fila_1.pack_propagate(False)
frame_fila_1.pack()

frame_fila_1_0 = Frame(frame_fila_1, width=400, height=FILA_1_HEIGHT, borderwidth=1, relief="flat")
frame_fila_1_0.pack_propagate(False)
frame_fila_1_0.pack(side="left")

label_header_num_cordon = Label(frame_fila_1_0, text="Ciclo de Soldadura", font=("Arial", 14))
label_header_num_cordon.pack()

label_num_cordon = Label(frame_fila_1_0, text="12345", font=("Arial", 14), width=30, bg="white", fg="black", borderwidth=1, relief="sunken")
label_num_cordon.pack()

frame_fila_1_1 = Frame(frame_fila_1, width=400, height=FILA_1_HEIGHT, borderwidth=1, relief="flat")
frame_fila_1_1.pack_propagate(False)
frame_fila_1_1.pack(side="right")

label_header_conteo_piezas = Label(frame_fila_1_1, text="Piezas Producidas", font=("Arial", 14))
label_header_conteo_piezas.pack()

label_conteo_piezas = Label(frame_fila_1_1, text="12345", font=("Arial", 14), width=30, bg="white", fg="black", borderwidth=1, relief="sunken")
label_conteo_piezas.pack()



# Frames Fila 2
frame_fila_2 = Frame(root, width=800, height=FILA_2_HEIGHT, borderwidth=1, relief="flat")
frame_fila_2.pack_propagate(False)
frame_fila_2.pack()

frame_fila_2_0 = Frame(frame_fila_2, width=400, height=FILA_2_HEIGHT, borderwidth=1, relief="flat")
frame_fila_2_0.pack_propagate(False)
frame_fila_2_0.pack(side="left")

label_header_fecha_pieza = Label(frame_fila_2_0, text="Fecha", font=("Arial", 14))
label_header_fecha_pieza.pack()

label_fecha_pieza = Label(frame_fila_2_0, text="2024-10-16 12:00", font=("Arial", 14), width=30, bg="white", fg="black", borderwidth=1, relief="sunken")
label_fecha_pieza.pack()

frame_fila_2_1 = Frame(frame_fila_2, width=400, height=FILA_2_HEIGHT, borderwidth=1, relief="flat")
frame_fila_2_1.pack_propagate(False)
frame_fila_2_1.pack(side="right")

label_header_plataforma = Label(frame_fila_2_1, text="Plataforma", font=("Arial", 14))
label_header_plataforma.pack()

label_plataforma = Label(frame_fila_2_1, text="MAZDA", font=("Arial", 14), width=30, bg="white", fg="black", borderwidth=1, relief="sunken")
label_plataforma.pack()

# Frames Fila 3
frame_fila_3 = Frame(root, width=800, height=FILA_3_HEIGHT, borderwidth=1, relief="flat")
frame_fila_3.pack_propagate(False)
frame_fila_3.pack()

frame_fila_3_0 = Frame(frame_fila_3, width=400, height=FILA_3_HEIGHT, borderwidth=1, relief="flat")
frame_fila_3_0.pack_propagate(False)
frame_fila_3_0.pack(side="left")

label_header_lista_espera_= Label(frame_fila_3_0, text="Lista de Espera", font=("Arial", 14))
label_header_lista_espera_.pack()

frame_fila_3_0_1 = Frame(frame_fila_3_0, width=350, height=FILA_3_HEIGHT, borderwidth=1, bg="white", relief="sunken")
frame_fila_3_0_1.pack_propagate(False)
frame_fila_3_0_1.pack()

label_lista_espera = Label(frame_fila_3_0_1, text="-", font=("Arial", 14), bg="white")
label_lista_espera.pack(side="top")

frame_fila_3_1 = Frame(frame_fila_3, width=400, height=FILA_3_HEIGHT, borderwidth=1, relief="flat")
frame_fila_3_1.pack_propagate(False)
frame_fila_3_1.pack(side="right")

label_header_eventos = Label(frame_fila_3_1, text="Eventos", font=("Arial", 14))
label_header_eventos.pack()

frame_fila_3_1_1 = Frame(frame_fila_3_1, width=350, height=FILA_3_HEIGHT, borderwidth=1, bg="white", relief="sunken")
frame_fila_3_1_1.pack_propagate(False)
frame_fila_3_1_1.pack()

label_eventos = Label(frame_fila_3_1_1, text="Sin Novedad", font=("Arial", 14), bg="white")
label_eventos.pack(side="top")

button_quit = Button(root, text="Quit", command=root.quit)
button_quit.pack()

root.mainloop()