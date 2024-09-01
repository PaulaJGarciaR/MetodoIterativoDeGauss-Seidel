import customtkinter
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app=customtkinter.CTk()
app.geometry("800x600")
app.columnconfigure(0,weight=1)
app.rowconfigure(0,weight=0)

#Titulo
title=customtkinter.CTkLabel(master=app,
                             text="Método iterativo de Gauss-Seidel",
                             font=("Impact",35))
title.grid(row=0,column=0,pady=10)

#Crear_frame_principal_y_configuracion_de_tamaño
frame_principal = customtkinter.CTkFrame(master=app, border_width=0)
frame_principal.grid(row=1, column=0,sticky="nsew")
frame_principal.columnconfigure(0,weight=1)
frame_principal.rowconfigure(0,weight=1)

#Crear_frame_contenedor_del_sistema_de_ecuaciones
frame_box_system_of_equations=customtkinter.CTkFrame(master=frame_principal, border_width=3,
                                                     border_color="#F2858E")
frame_box_system_of_equations.grid(row=0, column=0, padx=10, pady=10,sticky="nsew")
frame_box_system_of_equations.grid_columnconfigure(0,weight=1)
frame_box_system_of_equations.grid_rowconfigure(0,weight=0)

#Crear_frame_sistema_de_ecuaciones
frame_system_of_equations=customtkinter.CTkFrame(master=frame_box_system_of_equations)
frame_system_of_equations.grid(row=1, column=0, padx=10, pady=10)
frame_system_of_equations.grid_columnconfigure(0,weight=1)
frame_system_of_equations.grid_rowconfigure(0,weight=0)

title=customtkinter.CTkLabel(master=frame_box_system_of_equations,
                             text="Sitema de Ecuaciones 3x3",
                             font=("Lucida Console",20,"bold"))
title.grid(row=0,column=0,pady=10)

#Ecuacion_Uno
input_a11=customtkinter.CTkEntry(master=frame_system_of_equations,width=70,
                                 font=("Lucida Console",18))
input_a11.grid(row=0, column=0,padx=10,pady=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="X +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=0, column=1,padx=10)
input_a12=customtkinter.CTkEntry(master=frame_system_of_equations,width=70,
                                 font=("Lucida Console",18))
input_a12.grid(row=0, column=2,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="Y +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=0, column=3,padx=10)
input_a13=customtkinter.CTkEntry(master=frame_system_of_equations,width=70,
                                 font=("Lucida Console",18))
input_a13.grid(row=0, column=4,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="Z =",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=0, column=5,padx=10)
input_b1=customtkinter.CTkEntry(master=frame_system_of_equations,width=70,
                                font=("Lucida Console",18))
input_b1.grid(row=0, column=6,padx=10)

#Ecuacion_Dos
input_a21=customtkinter.CTkEntry(master=frame_system_of_equations,width=70,
                                 font=("Lucida Console",18))
input_a21.grid(row=1, column=0,padx=10,pady=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="X +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=1, column=1,padx=10)
input_a22=customtkinter.CTkEntry(master=frame_system_of_equations,width=70,
                                 font=("Lucida Console",18))
input_a22.grid(row=1, column=2,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="Y +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=1, column=3,padx=10)
input_a23=customtkinter.CTkEntry(master=frame_system_of_equations,width=70,
                                 font=("Lucida Console",18))
input_a23.grid(row=1, column=4,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations,
                                   text="Z =",font=("Lucida Console",18,"bold"))
label_signo.grid(row=1, column=5,padx=10)
input_b2=customtkinter.CTkEntry(master=frame_system_of_equations,width=70,
                                font=("Lucida Console",18))
input_b2.grid(row=1, column=6,padx=10)

#Ecuacion_Tres
input_a31=customtkinter.CTkEntry(master=frame_system_of_equations,width=70,
                                 font=("Lucida Console",18))
input_a31.grid(row=2, column=0,padx=10,pady=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="X +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=2, column=1,padx=10)
input_a32=customtkinter.CTkEntry(master=frame_system_of_equations,width=70,
                                 font=("Lucida Console",18))
input_a32.grid(row=2, column=2,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="Y +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=2, column=3,padx=10)
input_a33=customtkinter.CTkEntry(master=frame_system_of_equations,width=70,
                                 font=("Lucida Console",18))
input_a33.grid(row=2, column=4,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="Z =",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=2, column=5,padx=10)
input_b3=customtkinter.CTkEntry(master=frame_system_of_equations,width=70,
                                font=("Lucida Console",18))
input_b3.grid(row=2, column=6,padx=10)

#Boton_para_ingresar_los_datos_proporcionados_a_el_sistema_de_ecuaciones
button_enter=customtkinter.CTkButton(master=frame_box_system_of_equations,text="Enter",
                                     font=("Lucida Console",20,"bold"),
                                     fg_color="#F22E3E",hover_color="#A62940")
button_enter.grid(row=2, column=0,padx=10,pady=20,ipady=5)

#frame_solucion_del_sistema_de_ecuaciones

frame_answers=customtkinter.CTkFrame(master=frame_principal, border_width=3)
frame_answers.grid(row=1, column=0, padx=10, pady=10,sticky="nsew")
frame_answers.grid_columnconfigure(0,weight=1)
frame_answers.grid_rowconfigure(0,weight=0)









app.mainloop()
