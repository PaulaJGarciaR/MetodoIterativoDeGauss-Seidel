import customtkinter
import numpy

customtkinter.set_appearance_mode("dark")

#Creación y Configuración de la ventana principal---------------------------------------------------------------------------------
app=customtkinter.CTk()
app.geometry("1280x600")
app.columnconfigure(0,weight=1)
app.rowconfigure(0,weight=1)
app.configure(fg_color="#6c757d")

#Creación y configuración del contenedor principal y de las subpestañas---------------------------------------------------------
tab_principal=customtkinter.CTkTabview(master=app,width=780, height=650,
                                       fg_color="#adb5bd",segmented_button_fg_color="#CED4DA",
                                       segmented_button_selected_color="#1565C0",
                                       segmented_button_selected_hover_color="#0D47A1",
                                       segmented_button_unselected_color="#6c757d",
                                       segmented_button_unselected_hover_color="#212529"
                                       )
tab_principal.grid(row=1,column=0,pady=10,padx=10,sticky="nsew")
tab_principal.columnconfigure(0,weight=1)
tab_principal.rowconfigure(0,weight=1)

#Creación de la pestaña para ingresar los coeficientes del sistema de ecuaciones y otros valores-------------------------------
tab_system_of_equations=tab_principal.add("Sistema de ecuaciones")
tab_system_of_equations.columnconfigure(0,weight=1)
#tab_system_of_equations.rowconfigure(0,weight=1)

#Titulo Principal
title=customtkinter.CTkLabel(master=tab_system_of_equations,
                             text="Método iterativo de Gauss-Seidel",
                             font=("Impact",35),text_color="#212529")
title.grid(row=0,column=0)

#Creación y configuración del frame que contiene los elementos de la pestaña sistema de ecuaciones-------------------------------
frame_box_system_of_equations=customtkinter.CTkFrame(master=tab_system_of_equations,
                                                    fg_color="#ced4da")
frame_box_system_of_equations.grid(row=1, column=0, padx=10, pady=10,sticky="nsew")
frame_box_system_of_equations.grid_columnconfigure(0,weight=1)
frame_box_system_of_equations.grid_columnconfigure(1,weight=1)
frame_box_system_of_equations.grid_rowconfigure(0,weight=1)

#Crear frame que contendrá el sistema de ecuaciones------------------------------------------------------------------------------
frame_system_of_equations=customtkinter.CTkFrame(master=frame_box_system_of_equations,
                                                 fg_color="#adb5bd")
frame_system_of_equations.grid(row=2, column=0, padx=10, pady=10)
frame_system_of_equations.grid_columnconfigure(0,weight=1)
frame_system_of_equations.grid_rowconfigure(0,weight=1)

#Titulo para el sitema de ecuaciones
title=customtkinter.CTkLabel(master=frame_box_system_of_equations,
                             text="Sitema de Ecuaciones 3x3",
                             font=("Lucida Console",22,"bold"),
                             text_color="#212529")
title.grid(row=0,columnspan=2,pady=10)

#Estilos de los inputs que contiene el frame del sistema de ecuaciones
style_entry = {
    "width":70,
    "font":("Lucida Console",18),
    "fg_color":"#DEE2E6",
     "border_width":0,
     "text_color":"#000"
}
#Estilos para los label que contienen el frame del sistema de ecuaciones
style_label_sign = {
    "font":("Lucida Console",18,"bold"),
     "text_color":"#212529"
}

#Titulo que indica que se deben ingresar los valores de los coeficientes del sistema de  ecuaciones
title_enter_values=customtkinter.CTkLabel(master=frame_box_system_of_equations,
                             text="Ingresar los coeficientes del sistema de ecuaciones.",
                             font=("Lucida Console",15,"bold"),
                             text_color="#212529")
title_enter_values.grid(column=0,row=1)

#Ecuacion Uno
input_a11=customtkinter.CTkEntry(master=frame_system_of_equations, **style_entry)
input_a11.grid(row=0, column=0,padx=10,pady=10)
label_sign=customtkinter.CTkLabel(master=frame_system_of_equations, text="X₁ +",
                                   **style_label_sign)
label_sign.grid(row=0, column=1,padx=10)
input_a12=customtkinter.CTkEntry(master=frame_system_of_equations,**style_entry)
input_a12.grid(row=0, column=2,padx=10)
label_sign=customtkinter.CTkLabel(master=frame_system_of_equations, text="X₂ +",
                                   **style_label_sign)
label_sign.grid(row=0, column=3,padx=10)
input_a13=customtkinter.CTkEntry(master=frame_system_of_equations,**style_entry)
input_a13.grid(row=0, column=4,padx=10)
label_sign=customtkinter.CTkLabel(master=frame_system_of_equations, text="X₃ =",
                                   **style_label_sign)
label_sign.grid(row=0, column=5,padx=10)
input_b1=customtkinter.CTkEntry(master=frame_system_of_equations, **style_entry)
input_b1.grid(row=0, column=6,padx=10)

#Ecuacion Dos
input_a21=customtkinter.CTkEntry(master=frame_system_of_equations, **style_entry)
input_a21.grid(row=1, column=0,padx=10,pady=10)
label_sign=customtkinter.CTkLabel(master=frame_system_of_equations, text="X₁ +",
                                   **style_label_sign)
label_sign.grid(row=1, column=1,padx=10)
input_a22=customtkinter.CTkEntry(master=frame_system_of_equations, **style_entry)
input_a22.grid(row=1, column=2,padx=10)
label_sign=customtkinter.CTkLabel(master=frame_system_of_equations, text="X₂ +",
                                   **style_label_sign)
label_sign.grid(row=1, column=3,padx=10)
input_a23=customtkinter.CTkEntry(master=frame_system_of_equations, **style_entry)
input_a23.grid(row=1, column=4,padx=10)
label_sign=customtkinter.CTkLabel(master=frame_system_of_equations,
                                   text="X₃ =",**style_label_sign)
label_sign.grid(row=1, column=5,padx=10)
input_b2=customtkinter.CTkEntry(master=frame_system_of_equations, **style_entry)
input_b2.grid(row=1, column=6,padx=10)

#Ecuacion_Tres
input_a31=customtkinter.CTkEntry(master=frame_system_of_equations,**style_entry)
input_a31.grid(row=2, column=0,padx=10,pady=10)
label_sign=customtkinter.CTkLabel(master=frame_system_of_equations, text="X₁ +",
                                   **style_label_sign)
label_sign.grid(row=2, column=1,padx=10)
input_a32=customtkinter.CTkEntry(master=frame_system_of_equations,**style_entry)
input_a32.grid(row=2, column=2,padx=10)
label_sign=customtkinter.CTkLabel(master=frame_system_of_equations, text="X₂ +",
                                   **style_label_sign)
label_sign.grid(row=2, column=3,padx=10)
input_a33=customtkinter.CTkEntry(master=frame_system_of_equations,**style_entry)
input_a33.grid(row=2, column=4,padx=10)
label_sign=customtkinter.CTkLabel(master=frame_system_of_equations, text="X₃ =",
                                   **style_label_sign)
label_sign.grid(row=2, column=5,padx=10)
input_b3=customtkinter.CTkEntry(master=frame_system_of_equations,**style_entry)
input_b3.grid(row=2, column=6,padx=10)

#Función para guardar valores y validar que no hayan campos vacios y que todos los elementos sean numericos--------------------

#estilos para los label que mostrarán mensajes de validación
style_label_error = {
    "font":("Lucida Console",15,"bold"),
    "fg_color":"#FFCCD5",
    "text_color":"#800f2f",
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
        label_error.configure(text="")
        label_error.configure(fg_color="#ced4da")
        return conversion_values_of_the_system_of_equations
    
    except ValueError:
        label_error.configure(text="Error:Son permitidos solo valores numericos.")
        label_error.configure(** style_label_error)
        return None

#Frame para mostrar el sistema de ecuaciones con intercambio de filas si es necesario------------------------------------------
frame_system_of_equations_sorted=customtkinter.CTkFrame(master=frame_box_system_of_equations,
                                                 fg_color="#adb5bd")
frame_system_of_equations_sorted.grid(row=2, column=1, padx=10, pady=10)
frame_system_of_equations_sorted.grid_columnconfigure(0,weight=1)
frame_system_of_equations_sorted.grid_rowconfigure(1,weight=1)

#Configuracion de los estilos de los label
style_label = {
    "width":70,
    "font":("Lucida Console",18),
    "fg_color":"#DEE2E6",
    "corner_radius":4,
     "text_color":"#000"
}
#Titulo para indicar que se va a mostrar el sistema de ecuaciones ordenado
title_show_values=customtkinter.CTkLabel(master=frame_box_system_of_equations,
                             text="Sistema de ecuaciones ordenado.",
                             font=("Lucida Console",15,"bold"),
                             text_color="#212529")
title_show_values.grid(column=1,row=1)

#Ecuacion_Uno
label_a11=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, **style_label,text="")
label_a11.grid(row=0, column=0,padx=10,pady=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="X₁ +",
                                   **style_label_sign)
label_signo.grid(row=0, column=1,padx=10)
label_a12=customtkinter.CTkLabel(master=frame_system_of_equations_sorted,**style_label,text="")
label_a12.grid(row=0, column=2,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="X₂ +",
                                   **style_label_sign)
label_signo.grid(row=0, column=3,padx=10)
label_a13=customtkinter.CTkLabel(master=frame_system_of_equations_sorted,**style_label,text="")
label_a13.grid(row=0, column=4,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="X₃ =",
                                   **style_label_sign)
label_signo.grid(row=0, column=5,padx=10)
label_b1=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, **style_label,text="")
label_b1.grid(row=0, column=6,padx=10)

#Ecuacion_Dos
label_a21=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, **style_label,text="")
label_a21.grid(row=1, column=0,padx=10,pady=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="X₁ +",
                                   **style_label_sign)
label_signo.grid(row=1, column=1,padx=10)
label_a22=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, **style_label,text="")
label_a22.grid(row=1, column=2,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="X₂ +",
                                   **style_label_sign)
label_signo.grid(row=1, column=3,padx=10)
label_a23=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, **style_label,text="")
label_a23.grid(row=1, column=4,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted,
                                   text="X₃ =",**style_label_sign)
label_signo.grid(row=1, column=5,padx=10)
label_b2=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, **style_label,text="")
label_b2.grid(row=1, column=6,padx=10)

#Ecuacion_Tres
label_a31=customtkinter.CTkLabel(master=frame_system_of_equations_sorted,**style_label,text="")
label_a31.grid(row=2, column=0,padx=10,pady=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="X₁ +",
                                   **style_label_sign)
label_signo.grid(row=2, column=1,padx=10)
label_a32=customtkinter.CTkLabel(master=frame_system_of_equations_sorted,**style_label,text="")
label_a32.grid(row=2, column=2,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="X₂ +",
                                   **style_label_sign)
label_signo.grid(row=2, column=3,padx=10)
label_a33=customtkinter.CTkLabel(master=frame_system_of_equations_sorted,**style_label,text="")
label_a33.grid(row=2, column=4,padx=10)
label_signo=customtkinter.CTkLabel(master=frame_system_of_equations_sorted, text="X₃ =",
                                   **style_label_sign)
label_signo.grid(row=2, column=5,padx=10)
label_b3=customtkinter.CTkLabel(master=frame_system_of_equations_sorted,**style_label,text="")
label_b3.grid(row=2, column=6,padx=10)

#Función para organizar el sistema de ecuaciones para hallar la diagonal dominante---------------------------------------------
def sort_equations():
    """Funcion para ordenar las ecuaciones."""
    system_of_equations=save_values()
    #ordenar ecuacones segun la primera columna
    if system_of_equations is not None:
        column_0=system_of_equations[:,0]
        indice_fila_max_column_0=numpy.argmax(numpy.abs(column_0))
        if indice_fila_max_column_0==1:
            system_of_equations[[0,1]]=system_of_equations[[1,0]]
        else:
            if indice_fila_max_column_0==2:
                system_of_equations[[0,2]]= system_of_equations[[2,0]]
            else:
                system_of_equations[[0,0]]= system_of_equations[[0,0]]
    #ordenar ecuaciones segun la segunda columna
        column_1=system_of_equations[:,1]
        indice_fila_max_column_1=numpy.argmax(numpy.abs(column_1))
        if indice_fila_max_column_1==0:
            system_of_equations[[0,1]]=system_of_equations[[1,0]]
        else:
            if indice_fila_max_column_1==2:
                system_of_equations[[1,2]]= system_of_equations[[2,1]]
            else:
                system_of_equations[[1,1]]= system_of_equations[[1,1]]

    #ordenar ecuaciones segun la tercera columna
        column_2=system_of_equations[:,2]
        indice_fila_max_column_2=numpy.argmax(numpy.abs(column_2))
        if indice_fila_max_column_2==0:
            system_of_equations[[0,2]]=system_of_equations[[2,0]]
        else:
            if indice_fila_max_column_2==1:
                system_of_equations[[1,2]]= system_of_equations[[2,1]]
            else:
                system_of_equations[[2,2]]= system_of_equations[[2,2]]

        label_a11.configure(text=system_of_equations[0,0])
        label_a12.configure(text=system_of_equations[0,1])
        label_a13.configure(text=system_of_equations[0,2])
        label_b1.configure(text=system_of_equations[0,3])
        label_a21.configure(text=system_of_equations[1,0])
        label_a22.configure(text=system_of_equations[1,1])
        label_a23.configure(text=system_of_equations[1,2])
        label_b2.configure(text=system_of_equations[1,3])
        label_a31.configure(text=system_of_equations[2,0])
        label_a32.configure(text=system_of_equations[2,1])
        label_a33.configure(text=system_of_equations[2,2])
        label_b3.configure(text=system_of_equations[2,3])
        return system_of_equations

#Etiqueta de Texto para mostrar posibles errores al ingresar los valores------------------------------------------------------
label_error=customtkinter.CTkLabel(master=frame_box_system_of_equations,text="", 
                **style_label_sign)
label_error.grid(row=4,columnspan=2,pady=5)

#Estilos de los inputs para ingresar los valores iniciales y error relativo---------------------------------------------------
style_entry_others_values = {
    "font":("Lucida Console",20),
    "fg_color":"#DEE2E6",
     "border_width":2,
     "border_color":"#ADB5BD",
     "text_color":"#000"
}

#Estilos de los titulos de los inputs para ingresar otros valores-------------------------------------------------------------
style_label_others_values = {
    "font":("Lucida Console",12,"bold"),
     "text_color":"#495057",
}

#Estilos para los botones------------------------------------------------------------------------------------------------------
style_button = {
    "font":("Lucida Console",15,"bold"),
     "text_color":"#212529",
     "corner_radius":50
}

#Boton para validar que el sistema de ecuaciones y organizar el sistema de ecuaciones si es necesario--------------------------
button_validate=customtkinter.CTkButton(master=frame_box_system_of_equations,text="Validar",
                                     **style_button,fg_color="#42A5F5", hover_color="#1E88E5",command=sort_equations
                                     )
button_validate.grid(row=5, columnspan=2,padx=10,pady=5,ipady=5)

#Frame para definir los valores iniciales y el valor relativo de error-------------------------------------------------------
frame_enter_others_values=customtkinter.CTkFrame(master=frame_box_system_of_equations,height=30,
                                                 fg_color="#90CAF9")
frame_enter_others_values.grid(row=6,columnspan=2,pady=10,padx=10)
label_initial_value_x1=customtkinter.CTkLabel(master=frame_enter_others_values,
                                             text="Valor inicial X₁",
                                             **style_label_others_values)
label_initial_value_x1.grid(row=0,column=1,padx=5)
input_initial_value_x1=customtkinter.CTkEntry(master=frame_enter_others_values,
                                             **style_entry_others_values)

input_initial_value_x1.grid(row=1,column=1,padx=5,pady=5)
label_initial_value_x2=customtkinter.CTkLabel(master=frame_enter_others_values,
                                             text="Valor inicial X₂",
                                             **style_label_others_values)
label_initial_value_x2.grid(row=0,column=2,padx=5)
input_initial_value_x2=customtkinter.CTkEntry(master=frame_enter_others_values,
                                             **style_entry_others_values)
input_initial_value_x2.grid(row=1,column=2,padx=10)
label_initial_value_x3=customtkinter.CTkLabel(master=frame_enter_others_values,
                                             text="Valor inicial X₃",
                                             **style_label_others_values)
label_initial_value_x3.grid(row=0,column=3,padx=5)
input_initial_value_x3=customtkinter.CTkEntry(master=frame_enter_others_values,
                                             **style_entry_others_values)
input_initial_value_x3.grid(row=1,column=3,padx=10)
variables=["X₁","X₂","X₃"]
variable_list=customtkinter.CTkComboBox(master=frame_enter_others_values,values=variables,
                                        fg_color="#1976D2",text_color="#fff",
                                        border_color="#1976D2",
                                        button_hover_color="#1565C0",
                                        font=("Lucida Console",18,"bold"),dropdown_text_color="#000",
                                        dropdown_font=("Lucida Console",18),
                                        dropdown_fg_color="#DEE2E6",dropdown_hover_color="#ADB5BD",
                                        )
variable_list.grid(row=1,column=4,padx=10)
label_error_margin=customtkinter.CTkLabel(master=frame_enter_others_values,
                                             text="Error relativo",
                                             **style_label_others_values)
label_error_margin.grid(row=0,column=5,padx=5)
input_error_margin=customtkinter.CTkEntry(master=frame_enter_others_values,
                                          **style_entry_others_values)
input_error_margin.grid(row=1,column=5,padx=10)

label_error_others_values=customtkinter.CTkLabel(master=frame_box_system_of_equations,text="", 
                **style_label_sign)
label_error_others_values.grid(row=7,columnspan=2,pady=5)

def limpiar_inputs_frames(*frames):
    """Función para limpiar los input""" #-----------------------------------------------------------------------------------
    for frame in frames:
        for widget in frame.winfo_children():
            if isinstance(widget, customtkinter.CTkEntry):
                widget.delete(0, customtkinter.END)
                label_a11.configure(text="")
                label_a12.configure(text="")
                label_a13.configure(text="")
                label_a21.configure(text="")
                label_a22.configure(text="")
                label_a23.configure(text="")
                label_a31.configure(text="")
                label_a32.configure(text="")
                label_a33.configure(text="")

#Creación del frame que contendrá botones------------------------------------------------------------------------------------
frame_button=customtkinter.CTkFrame(master=frame_box_system_of_equations,fg_color="#CED4DA")
frame_button.grid(row=8,columnspan=2)

#Botón para dar solución al sistema de ecuaciones
button_solution=customtkinter.CTkButton(master=frame_button,text="=",
                                     **style_button,fg_color="#42A5F5",
                                     hover_color="#64B5F6",command=lambda:limpiar_inputs_frames(frame_system_of_equations))
button_solution.grid(row=0, column=0,padx=10,pady=10,ipady=5)

#Botón para limpiar los input 
button_delete=customtkinter.CTkButton(master=frame_button,text="Borrar",fg_color="#FF758F",
                                      hover_color="#FF8FA3",**style_button,
                                      command=lambda:limpiar_inputs_frames(frame_system_of_equations))
button_delete.grid(row=0, column=1,padx=10,pady=10,ipady=5)

tab_answers=tab_principal.add("Solución")


app.mainloop()
