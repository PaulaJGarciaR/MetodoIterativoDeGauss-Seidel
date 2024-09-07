import customtkinter
import numpy
customtkinter.set_appearance_mode("dark")

#Creación y Configuración de la ventana principal------------------------------------------------------------------------------
app=customtkinter.CTk()
app.geometry("1280x600")
app.columnconfigure(0,weight=1)
app.rowconfigure(0,weight=1)
app.configure(fg_color="#212529")

#Creación y configuración del contenedor principal y de las subpestañas---------------------------------------------------------
tab_principal=customtkinter.CTkTabview(master=app,width=780, height=650,
                                       fg_color="#343A40",segmented_button_fg_color="#495057",
                                       segmented_button_selected_color="#ff477e",
                                       segmented_button_selected_hover_color="#ff0a54",
                                       segmented_button_unselected_color="#343A40",
                                       segmented_button_unselected_hover_color="#212529"
                                       )
tab_principal.grid(row=1,column=0,pady=10,padx=10,sticky="nsew")
tab_principal.columnconfigure(0,weight=1)
tab_principal.rowconfigure(0,weight=1)

#Creación de la pestaña para ingresar los coeficientes del sistema de ecuaciones-----------------------------------------------
tab_system_of_equations=tab_principal.add("Sistema de ecuaciones")
tab_system_of_equations.columnconfigure(0,weight=1)
#tab_system_of_equations.rowconfigure(0,weight=1)
#Titulo Principal
title=customtkinter.CTkLabel(master=tab_system_of_equations,
                             text="Método iterativo de Gauss-Seidel",
                             font=("Impact",35))
title.grid(row=0,column=0)

#Creación y configuración del frame que contiene los elementos de la pestaña sistema de ecuaciones-------------------------------
frame_box_system_of_equations=customtkinter.CTkFrame(master=tab_system_of_equations, border_width=3,
                                                     border_color="#212529",fg_color="#495057")
frame_box_system_of_equations.grid(row=1, column=0, padx=10, pady=10,sticky="nsew")
frame_box_system_of_equations.grid_columnconfigure(0,weight=1)
frame_box_system_of_equations.grid_columnconfigure(1,weight=1)
frame_box_system_of_equations.grid_rowconfigure(0,weight=1)

#Crear frame sistema de ecuaciones--------------------------------------------------------------------------------------------
frame_system_of_equations=customtkinter.CTkFrame(master=frame_box_system_of_equations,
                                                 fg_color="#343A40")
frame_system_of_equations.grid(row=2, column=0, padx=10, pady=10)
frame_system_of_equations.grid_columnconfigure(0,weight=1)
frame_system_of_equations.grid_rowconfigure(0,weight=1)

#Titulo para el sitema de ecuaciones
title=customtkinter.CTkLabel(master=frame_box_system_of_equations,
                             text="Sitema de Ecuaciones 3x3",
                             font=("Lucida Console",22,"bold"))
title.grid(row=0,columnspan=2,pady=10)

#Configuracion de los estilos de los inputs sistema de ecuaciones
style_entry = {
    "width":70,
    "font":("Lucida Console",18),
    "fg_color":"#DEE2E6",
     "border_color":"#343A40",
     "text_color":"#000"
}

#Titulo que indica que se deben ingresar los valores de los coeficientes del sistema de  ecuaciones
title_enter_values=customtkinter.CTkLabel(master=frame_box_system_of_equations,
                             text="Ingresar los coeficientes del sistema de ecuaciones.",
                             font=("Lucida Console",15,"bold"))
title_enter_values.grid(column=0,row=1)

#Ecuacion_Uno
input_a11=customtkinter.CTkEntry(master=frame_system_of_equations, **style_entry)
input_a11.grid(row=0, column=0,padx=10,pady=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="X +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=0, column=1,padx=10)
input_a12=customtkinter.CTkEntry(master=frame_system_of_equations,**style_entry)
input_a12.grid(row=0, column=2,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="Y +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=0, column=3,padx=10)
input_a13=customtkinter.CTkEntry(master=frame_system_of_equations,**style_entry)
input_a13.grid(row=0, column=4,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="Z =",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=0, column=5,padx=10)
input_b1=customtkinter.CTkEntry(master=frame_system_of_equations, **style_entry)
input_b1.grid(row=0, column=6,padx=10)

#Ecuacion_Dos
input_a21=customtkinter.CTkEntry(master=frame_system_of_equations, **style_entry)
input_a21.grid(row=1, column=0,padx=10,pady=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="X +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=1, column=1,padx=10)
input_a22=customtkinter.CTkEntry(master=frame_system_of_equations, **style_entry)
input_a22.grid(row=1, column=2,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="Y +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=1, column=3,padx=10)
input_a23=customtkinter.CTkEntry(master=frame_system_of_equations, **style_entry)
input_a23.grid(row=1, column=4,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations,
                                   text="Z =",font=("Lucida Console",18,"bold"))
label_signo.grid(row=1, column=5,padx=10)
input_b2=customtkinter.CTkEntry(master=frame_system_of_equations, **style_entry)
input_b2.grid(row=1, column=6,padx=10)

#Ecuacion_Tres
input_a31=customtkinter.CTkEntry(master=frame_system_of_equations,**style_entry)
input_a31.grid(row=2, column=0,padx=10,pady=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="X +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=2, column=1,padx=10)
input_a32=customtkinter.CTkEntry(master=frame_system_of_equations,**style_entry)
input_a32.grid(row=2, column=2,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="Y +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=2, column=3,padx=10)
input_a33=customtkinter.CTkEntry(master=frame_system_of_equations,**style_entry)
input_a33.grid(row=2, column=4,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations, text="Z =",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=2, column=5,padx=10)
input_b3=customtkinter.CTkEntry(master=frame_system_of_equations,**style_entry)
input_b3.grid(row=2, column=6,padx=10)

#Función para guardar valores y validar que no hayan campos vacios y que todos los elementos sean numericos--------------------
#estilos para los label que mostrarán mensajes de validación
style_label_error = {
    "font":("Lucida Console",15,"bold"),
    "fg_color":"#fc9ca2",
    "text_color":"#901b22",
    "corner_radius":4
}

def save_values ():
    """Funcion para guardar valores."""
    values_of_the_system_of_equations=numpy.array(
        [[input_a11.get(),input_a12.get(),input_a13.get(),input_b1.get()],
         [input_a21.get(),input_a22.get(),input_a23.get(),input_b2.get()],
         [input_a31.get(),input_a32.get(),input_a33.get(),input_b3.get()]])
    
    if numpy.any(numpy.vectorize(lambda x: x.strip() == "")(values_of_the_system_of_equations)):
        label_error.configure(text="Error: Hay elementos vacíos en la matriz.")
        label_error.configure(** style_label_error)
        return None
    
    try:
        conversion_values_of_the_system_of_equations=values_of_the_system_of_equations.astype(float)
        return conversion_values_of_the_system_of_equations
    except ValueError:
        label_error.configure(text="Error:Son permitidos solo valores numericos.")
        label_error.configure(** style_label_error)
        


frame_system_of_equations_sorted=customtkinter.CTkFrame(master=frame_box_system_of_equations,
                                                 fg_color="#343A40")
frame_system_of_equations_sorted.grid(row=2, column=1, padx=10, pady=10)
frame_system_of_equations_sorted.grid_columnconfigure(0,weight=1)
frame_system_of_equations_sorted.grid_rowconfigure(1,weight=1)

#Configuracion de los estilos de los label
style_label = {
    "width":70,
    "font":("Lucida Console",18),
    "fg_color":"#ADB5BD",
    "corner_radius":4,
     "text_color":"#000"
}
#Titulo para indicar que se va a mostrar el sistema de ecuaciones ordenado
title_show_values=customtkinter.CTkLabel(master=frame_box_system_of_equations,
                             text="Sistema de ecuaciones ordenado.",
                             font=("Lucida Console",15,"bold"))
title_show_values.grid(column=1,row=1)


#Ecuacion_Uno
label_a11=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, **style_label,text="")
label_a11.grid(row=0, column=0,padx=10,pady=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="X +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=0, column=1,padx=10)
label_a12=customtkinter.CTkLabel(master=frame_system_of_equations_sorted,**style_label,text="")
label_a12.grid(row=0, column=2,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="Y +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=0, column=3,padx=10)
label_a13=customtkinter.CTkLabel(master=frame_system_of_equations_sorted,**style_label,text="")
label_a13.grid(row=0, column=4,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="Z =",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=0, column=5,padx=10)
label_b1=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, **style_label,text="")
label_b1.grid(row=0, column=6,padx=10)

#Ecuacion_Dos
label_a21=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, **style_label,text="")
label_a21.grid(row=1, column=0,padx=10,pady=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="X +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=1, column=1,padx=10)
label_a22=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, **style_label,text="")
label_a22.grid(row=1, column=2,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="Y +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=1, column=3,padx=10)
label_a23=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, **style_label,text="")
label_a23.grid(row=1, column=4,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted,
                                   text="Z =",font=("Lucida Console",18,"bold"))
label_signo.grid(row=1, column=5,padx=10)
label_b2=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, **style_label,text="")
label_b2.grid(row=1, column=6,padx=10)

#Ecuacion_Tres
label_a31=customtkinter.CTkLabel(master=frame_system_of_equations_sorted,**style_label,text="")
label_a31.grid(row=2, column=0,padx=10,pady=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="X +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=2, column=1,padx=10)
label_a32=customtkinter.CTkLabel(master=frame_system_of_equations_sorted,**style_label,text="")
label_a32.grid(row=2, column=2,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="Y +",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=2, column=3,padx=10)
label_a33=customtkinter.CTkLabel(master=frame_system_of_equations_sorted,**style_label,text="")
label_a33.grid(row=2, column=4,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="Z =",
                                   font=("Lucida Console",18,"bold"))
label_signo.grid(row=2, column=5,padx=10)
label_b3=customtkinter.CTkLabel(master=frame_system_of_equations_sorted,**style_label,text="")
label_b3.grid(row=2, column=6,padx=10)

#Etiqueta de Texto para mostrar posibles errores al ingresar los valores---------------------------------------------------
label_error=customtkinter.CTkLabel(master=frame_box_system_of_equations,text="", 
                                         font=("Lucida Console",10))
label_error.grid(row=4,columnspan=2,pady=5)

style_entry_others_values = {
    "font":("Lucida Console",18),
    "fg_color":"#DEE2E6",
     "border_color":"#DEE2E6",
     "text_color":"#000"
}
frame_enter_other_values=customtkinter.CTkFrame(master=frame_box_system_of_equations,height=30)
frame_enter_other_values.grid(row=5,columnspan=2,pady=10,padx=10)
input_error_margin=customtkinter.CTkEntry(master=frame_enter_other_values,
                                          **style_entry_others_values)
input_error_margin.grid(row=0,column=0,padx=10,pady=5)
input_initial_value_x=customtkinter.CTkEntry(master=frame_enter_other_values,
                                             **style_entry_others_values)
input_initial_value_x.grid(row=0,column=1,padx=10,pady=5)
input_initial_value_y=customtkinter.CTkEntry(master=frame_enter_other_values,
                                             **style_entry_others_values)
input_initial_value_y.grid(row=0,column=2,padx=10,pady=5)
input_initial_value_z=customtkinter.CTkEntry(master=frame_enter_other_values,
                                             **style_entry_others_values)
input_initial_value_z.grid(row=0,column=3,padx=10,pady=5)

#Boton para ingresar los datos proporcionados a el sistema de ecuaciones-----------------------------------------------------
button_enter=customtkinter.CTkButton(master=frame_box_system_of_equations,text="Enter",
                                     font=("Lucida Console",18,"bold"),
                                     fg_color="#ff477e",hover_color="#ff0a54",
                                     command=save_values
                                     )
button_enter.grid(row=6, columnspan=2,padx=10,pady=5,ipady=5)

#Boton para limpiar los cajas de texto---------------------------------------------------------------------------------------
button_delete=customtkinter.CTkButton(master=frame_box_system_of_equations,text="Delete",
                                     font=("Lucida Console",18,"bold"),
                                     fg_color="#ff477e",hover_color="#ff0a54"
                                     )
button_delete.grid(row=7, columnspan=2,padx=10,pady=10,ipady=5)

tab_answers=tab_principal.add("Solución")


app.mainloop()
