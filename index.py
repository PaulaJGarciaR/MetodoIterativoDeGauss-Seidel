from tkinter import ttk
import customtkinter
import numpy
import math

customtkinter.set_appearance_mode("dark")

#Creación y Configuración de la ventana principal---------------------------------------------------------------------------------
app=customtkinter.CTk()
app.geometry("1280x650")
app.columnconfigure(0,weight=1)
app.rowconfigure(0,weight=1)
app.configure(fg_color="#767b91")
#app.resizable(False,False)

#Creación y configuración del contenedor principal y de las subpestañas---------------------------------------------------------
tab_principal=customtkinter.CTkTabview(master=app,width=780, height=660,text_color="#000",
                                       fg_color="#c7ccdb",segmented_button_fg_color="#F6F6F6",
                                       segmented_button_selected_color="#FF7096",
                                       segmented_button_selected_hover_color="#FF477E",
                                       segmented_button_unselected_color="#bec5da",
                                       segmented_button_unselected_hover_color="#9BA2C0"
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
                                                    fg_color="#e1e5ee")
frame_box_system_of_equations.grid(row=1, column=0, padx=10, pady=10,sticky="nsew")
frame_box_system_of_equations.grid_columnconfigure(0,weight=1)
frame_box_system_of_equations.grid_columnconfigure(1,weight=1)
frame_box_system_of_equations.grid_rowconfigure(0,weight=1)

#Crear frame que contendrá el sistema de ecuaciones------------------------------------------------------------------------------
frame_system_of_equations=customtkinter.CTkFrame(master=frame_box_system_of_equations,
                                                 fg_color="#BEC5DA")
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
    "font":("Lucida Console",20),
    "fg_color":"#F8F9FA",
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
def save_values():
    """Funcion para guardar valores.""" #------------------------------------------------------------------------------------
    values_of_the_system_of_equations=numpy.array(
        [[input_a11.get(),input_a12.get(),input_a13.get(),input_b1.get()],
         [input_a21.get(),input_a22.get(),input_a23.get(),input_b2.get()],
         [input_a31.get(),input_a32.get(),input_a33.get(),input_b3.get()]])
       
    if numpy.any(numpy.vectorize(lambda x: x.strip() == "")(values_of_the_system_of_equations)):
        label_error.configure(text="Error: Hay elementos vacíos en el sistema de ecuaciones.")
        label_error.configure(** style_label_error)
        return None     
    try:
        conversion_values_of_the_system_of_equations=values_of_the_system_of_equations.astype(float)
        label_error.configure(text="")
        label_error.configure(fg_color="#e1e5ee")
        return conversion_values_of_the_system_of_equations
    
    except ValueError:
        label_error.configure(text="Error:Son permitidos solo valores numericos.")
        label_error.configure(** style_label_error)
        return None

#Frame para mostrar el sistema de ecuaciones con intercambio de filas si es necesario------------------------------------------
frame_system_of_equations_sorted=customtkinter.CTkFrame(master=frame_box_system_of_equations,
                                                 fg_color="#BEC5DA")
frame_system_of_equations_sorted.grid(row=2, column=1, padx=10, pady=10)
frame_system_of_equations_sorted.grid_columnconfigure(0,weight=1)
frame_system_of_equations_sorted.grid_rowconfigure(1,weight=1)

#Configuracion de los estilos de los label
style_label = {
    "width":70,
    "font":("Lucida Console",20),
    "fg_color":"#F8F9FA",
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

def zeros_main_diagonal():
    """Función para verificar que en la diagonal principal no coeficientes sean difirentes a cero""" #-------------------------
    system_of_equations=save_values()
    if system_of_equations is not None:
        if numpy.any(numpy.diag(system_of_equations==0)):
            label_error.configure(** style_label_error)
            label_error.configure(text="Valor de 0 en la diagonal dominante.")
            return None 
        return system_of_equations
    return None
    
def identical_or_proportional_rows():
    """Función para identificar las filas del sistema de ecuaciones son proporcionales o iguales""" #---------------------
    system_of_equations=zeros_main_diagonal()
    if system_of_equations is not None:
        for i in range(3):
            for j in range(i+1, 3):
                if numpy.array_equal(system_of_equations[i], system_of_equations[j]):
                    label_error.configure(** style_label_error)
                    label_error.configure(text="Filas idénticas. El sistema de ecuaciones no tiene solución única.")
                    return None
    #Sistema de ecuaciones proporcional--------------------------------------------------------------------
        n_rows = system_of_equations.shape[0]
        for i in range(n_rows):
            for j in range(i + 1, n_rows):
                # Evitar filas que sean completamente ceros
                if numpy.all(system_of_equations[i] == 0) or numpy.all(system_of_equations[j] == 0):
                    continue
            
                # Calcular el ratio entre las dos filas, manejar divisiones por 0
                with numpy.errstate(divide='ignore', invalid='ignore'):
                    ratio = numpy.divide(system_of_equations[i], system_of_equations[j])
                
                # Comparar si todos los ratios (no NaN) son iguales
                    if numpy.all(numpy.isclose(ratio[~numpy.isnan(ratio)], ratio[~numpy.isnan(ratio)][0])):
                        label_error.configure(** style_label_error)
                        label_error.configure(text="Filas Proporcionales. El sistema de ecuaciones no tiene solución")
                        return None                
        return system_of_equations
    return None        

def dominant_diagonal():
    """Función para determinar si la diagonal principal es dominante""" #-----------------------------------------------------
    system_of_equations=identical_or_proportional_rows()
    if system_of_equations is not None:
        for i in range(3):
            row_sum = sum(abs(system_of_equations[i][j]) for j in range(3) if i != j)
            if abs(system_of_equations[i][i]) <= row_sum:
                return False
        return True
    return None

def sort_equations():
    """Funcion para ordenar las ecuaciones e intercambiar filas si es necesario"""#------------------------------------------
    system_of_equations=identical_or_proportional_rows()
    if system_of_equations is not None:
        n = len(system_of_equations)
        for i in range(n):
            max_row = i
            for j in range(i + 1, n):
                if abs(system_of_equations[j, i]) > abs(system_of_equations[max_row, i]):
                    max_row = j
            if max_row != i:
                system_of_equations[i], system_of_equations[max_row] = system_of_equations[max_row].copy(), system_of_equations[i].copy()
    return system_of_equations

def get_dominant_diagonal():
    """Función oara verificar si el sistema de ecuaciones con permutación, se puede obtener la diagonal dominante"""
    system_of_equations=sort_equations()
    if system_of_equations is not None:
        n = len(system_of_equations)
        for i in range(n):
            diagonal = abs(system_of_equations[i][i])
            suma_fila = sum(abs(system_of_equations[i][j]) for j in range(n) if j != i)
            if diagonal <= suma_fila:
                return False      
        return system_of_equations 
    return None

def show_system_of_equations():
    """Función para mostrar el sistema de ecuaciones valido"""
    system_of_equations=get_dominant_diagonal()
    if system_of_equations is False:
        label_error.configure(** style_label_error)
        label_error.configure(text="No es posible obtener la diagonal dominante")
        return None
    else:
        if system_of_equations is not None:
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
    return None
        
#Etiqueta de Texto para mostrar posibles errores al ingresar los valores------------------------------------------------------
label_error=customtkinter.CTkLabel(master=frame_box_system_of_equations,text="", 
                **style_label_sign)
label_error.grid(row=4,columnspan=2,pady=5)

#Estilos de los inputs para ingresar los valores iniciales y error relativo---------------------------------------------------
style_entry_others_values = {
    "font":("Lucida Console",20),
    "fg_color":"#F8F9FA",
     "border_width":2,
     "border_color":"#BEC5DA",
     "text_color":"#000",
     "height":30,
     "corner_radius":10
}

#Estilos de los titulos de los inputs para ingresar otros valores-------------------------------------------------------------
style_label_others_values = {
    "font":("Lucida Console",12,"bold"),
     "text_color":"#495057",
}

#Estilos para los botones------------------------------------------------------------------------------------------------------
style_button = {
    "font":("Lucida Console",15,"bold"),
     "text_color":"#000",
     "corner_radius":50
}

#Boton para validar que el sistema de ecuaciones y organizar el sistema de ecuaciones si es necesario--------------------------
button_validate=customtkinter.CTkButton(master=frame_box_system_of_equations,text="Validar",
                                     **style_button,fg_color="#5682FB", hover_color="#2F67FF",command=show_system_of_equations
                                     )
button_validate.grid(row=5, columnspan=2,padx=10,pady=5,ipady=5)

#Frame para definir los valores iniciales y el valor relativo de error-------------------------------------------------------
frame_enter_others_values=customtkinter.CTkFrame(master=frame_box_system_of_equations,height=30,
                                                 fg_color="#B8CBFF")
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
                                        fg_color="#767b91",text_color="#fff",
                                        border_color="#767b91",
                                        button_color="#676C80",
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

def save_initial_values_and_margin_of_error():
    """Función para guardar todos los valores que son ingresados para los valores iniciales y el maargen de error""" #-------------------------
    values_initial_values_and_margin_of_error=numpy.array([input_initial_value_x1.get(),
                                                           input_initial_value_x2.get(),
                                                          input_initial_value_x3.get(),
                                                          input_error_margin.get()])
    values_initial_values_and_margin_of_error[3]=values_initial_values_and_margin_of_error[3].replace('%','')
    if numpy.any(numpy.vectorize(lambda x: x.strip() == "")(values_initial_values_and_margin_of_error)):
        label_error_others_values.configure(text="Error: Hay elementos vacíos.")
        label_error_others_values.configure(** style_label_error)
        return None     
    try:
        conversion_initial_values_and_margin_of_error=values_initial_values_and_margin_of_error.astype(float)
        label_error_others_values.configure(text="")
        label_error_others_values.configure(fg_color="#ced4da")
        return conversion_initial_values_and_margin_of_error
    
    except ValueError:
        label_error_others_values.configure(text="Error:Son permitidos solo valores numericos.")
        label_error_others_values.configure(** style_label_error)
        return None
  
    
def limpiar_inputs_frames(*frames):
    """Función para limpiar los input""" #-----------------------------------------------------------------------------------
    for frame in frames:
        for widget in frame.winfo_children():
            if isinstance(widget, customtkinter.CTkEntry):
                widget.delete(0, customtkinter.END)
                label_a11.configure(text="")
                label_a12.configure(text="")
                label_a13.configure(text="")
                label_b1.configure(text="")
                label_a21.configure(text="")
                label_a22.configure(text="")
                label_a23.configure(text="")
                label_b2.configure(text="")
                label_a31.configure(text="")
                label_a32.configure(text="")
                label_a33.configure(text="")
                label_b3.configure(text="")
                label_error.configure(text="")
                label_error.configure(fg_color="#e1e5ee")
                label_error_others_values.configure(text="")
                label_error_others_values.configure(fg_color="#e1e5ee")

#Creación del frame que contendrá botones------------------------------------------------------------------------------------
frame_button=customtkinter.CTkFrame(master=frame_box_system_of_equations,fg_color="#e1e5ee")
frame_button.grid(row=8,columnspan=2)

#Botón para limpiar los input 
button_delete=customtkinter.CTkButton(master=frame_button,text="Borrar",fg_color="#FF7096",
                                      hover_color="#FF477E",**style_button,
                                      command=lambda:limpiar_inputs_frames(frame_system_of_equations))
button_delete.grid(row=0, column=1,padx=10,pady=10,ipady=5)

#Creación y configración de la pestaña para mostrar la solución del sistema de ecuaciones---------------------------------
tab_answers=tab_principal.add("Solución")
tab_answers.columnconfigure(0,weight=1)
#Titulo de la pestaña
title_answers=customtkinter.CTkLabel(master=tab_answers,
                             text="Solución Sistema de ecuaciones 3x3",
                             font=("Impact",35),text_color="#212529")
title_answers.grid(row=0,column=0)

#Creación y configuración del frame que contiene los elementos de la pestaña para mostrar la solución---------------------
frame_show_solutions=customtkinter.CTkFrame(master=tab_answers,
                                                    fg_color="#e1e5ee")
frame_show_solutions.grid(row=1, column=0, padx=10, pady=10,sticky="nsew")
frame_show_solutions.grid_columnconfigure(0,weight=1)
frame_show_solutions.grid_rowconfigure(0,weight=1)

def fixed_map(option):
    """Función para solucionar los problemas para aplicar estilos a la tabla"""
    return [elm for elm in style.map('Treeview', query_opt=option)
           if elm[:2] != ('!disabled', '!selected')]
    
#Creación del objeto style para personalizar los elementos de la tabla 
style = ttk.Style()
#Definir un tema predeterminado
style.theme_use('default')

# Personalización (sobreescribe los estilos) de la tabla para el color de texto y fondo.
style.map('Treeview', foreground=fixed_map('foreground'),
          background=fixed_map('background'))

# Configuración los estilos para la tabla
style.configure("Treeview",
                font=("Lucida Console",18),
                 background="#F8F9FA",
                fieldbackground="#E9ECEF",
                foreground="#343A40",
                rowheight=30)

#Eliminación de los border de la tabla
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) 

#Configuración de los estilos de los encabezados
style.configure("Treeview.Heading",
                font=("Lucida Console",20,"bold"),
                background="#A4BDFF",
                foreground="#343A40",
                relief="flat",
                padding=(5,5))

#Personalización de encabezados activos
style.map("Treeview.Heading",
          background=[('active', '#5682FB')])
#Personalización de filas seleccionadas
style.map("Treeview", background=[('selected', '#B8CBFF')]) 
style.map("Treeview", foreground=[('selected', '#343A40')])  
 

#Creación de la tabla con ttk
table_of_results= ttk.Treeview(master=frame_show_solutions, 
                               columns=("N°", "X₁", "X₂","X₃","Error|εₐ|"), 
                               show="headings", height=5)

#Configración de los encabezados de la tabla
table_of_results.heading("N°", text="N°")
table_of_results.heading("X₁", text="X₁")
table_of_results.heading("X₂", text="X₂")
table_of_results.heading("X₃", text="X₃")
table_of_results.heading("Error|εₐ|", text="Error|εₐ|")

#Configuración del tamaño para las columnas
table_of_results.column("N°", width=200,anchor="center")
table_of_results.column("X₁", width=200,anchor="center")
table_of_results.column("X₂", width=200,anchor="center")
table_of_results.column("X₃", width=200,anchor="center")
table_of_results.column("Error|εₐ|", width=200,anchor="center")
table_of_results.grid(column=0,row=0,pady=10)

def generate_iterations():
    system_of_equations=show_system_of_equations()
    label_error.configure(text="")
    label_error.configure(fg_color="#e1e5ee")
    values_initial_values_and_margin_of_error=save_initial_values_and_margin_of_error()
    if system_of_equations is not None and values_initial_values_and_margin_of_error is not None:
        tab_principal.set("Solución")
        max_iteration=100
        tolerance=100
        decimals = 4
        for item in table_of_results.get_children():
            table_of_results.delete(item)
        x1_old,x2_old, x3_old = values_initial_values_and_margin_of_error[0],values_initial_values_and_margin_of_error[1],values_initial_values_and_margin_of_error[2]
        for iteration in range(max_iteration):
            if (values_initial_values_and_margin_of_error[3])<=tolerance:
                x1 = (system_of_equations[0][3] - system_of_equations[0][1] * x2_old - system_of_equations[0][2] * x3_old) / system_of_equations[0][0]
                x2 = (system_of_equations[1][3] - system_of_equations[1][0] * x1 - system_of_equations[1][2] * x3_old) / system_of_equations[1][1]
                x3 = (system_of_equations[2][3] - system_of_equations[2][0] * x1 - system_of_equations[2][1] * x2) / system_of_equations[2][2]
               
                x1_rounded_up = math.ceil(x1 * 10**decimals) / 10**decimals
                x2_rounded_up = math.ceil(x2 * 10**decimals) / 10**decimals
                x3_rounded_up = math.ceil(x3 * 10**decimals) / 10**decimals
                
                if variable_list.get()=="X₁":
                    tolerance=abs(((x1_rounded_up-x1_old)/x1_rounded_up)*100)
                elif variable_list.get()=="X₂":
                    tolerance=abs(((x2_rounded_up-x2_old)/x2_rounded_up)*100)
                elif variable_list.get()=="X₃":
                    tolerance=abs(((x3_rounded_up-x3_old)/x3_rounded_up)*100)
                    
                tolerance_rounded_up= math.ceil(tolerance * 10**decimals) / 10**decimals 
                table_of_results.insert('', 'end', values=(iteration + 1, x1_rounded_up,x2_rounded_up, x3_rounded_up,tolerance_rounded_up))
                x1_old, x2_old, x3_old = x1_rounded_up, x2_rounded_up, x3_rounded_up           
                
#Botón para dar solución al sistema de ecuaciones
button_solution=customtkinter.CTkButton(master=frame_button,text="=",
                                     **style_button,fg_color="#FF7096",
                                     hover_color="#FF477E",command=generate_iterations)
button_solution.grid(row=0, column=0,padx=10,pady=10,ipady=5)

tab_user_manual=tab_principal.add("Manual de Uso")
tab_user_manual.columnconfigure(0,weight=1)

app.mainloop()
