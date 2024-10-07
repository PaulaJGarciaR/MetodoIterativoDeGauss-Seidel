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
app.configure(fg_color="#0D1B2A")
#app.resizable(False,False)

#Creación y configuración del contenedor principal y de las subpestañas---------------------------------------------------------
tab_principal=customtkinter.CTkTabview(app,width=780, height=660,text_color="#000",
                                       fg_color="#415A77",segmented_button_fg_color="#f2f4f7",
                                       segmented_button_selected_color="#FF7096",
                                       segmented_button_selected_hover_color="#FF99AC",
                                       segmented_button_unselected_color="#778DA9",
                                       segmented_button_unselected_hover_color="#8ea0b8"
                                       )
tab_principal.grid(row=1,column=0,pady=10,padx=10,sticky="nsew")
tab_principal.columnconfigure(0,weight=1)
tab_principal.rowconfigure(0,weight=1)

#Creación de la pestaña para ingresar los coeficientes del sistema de ecuaciones y otros valores-------------------------------
tab_system_of_equations=tab_principal.add("Sistema de ecuaciones")
tab_system_of_equations.columnconfigure(0,weight=1)
#tab_system_of_equations.rowconfigure(0,weight=1)

#Titulo Principal
title=customtkinter.CTkLabel(tab_system_of_equations,
                             text="Método iterativo de Gauss-Seidel",
                             font=("Impact",35),text_color="#fff")
title.grid(row=0,column=0)

#Creación y configuración del frame que contiene los elementos de la pestaña sistema de ecuaciones-------------------------------
frame_box_system_of_equations=customtkinter.CTkFrame(tab_system_of_equations,
                                                    fg_color="#778DA9")
frame_box_system_of_equations.grid(row=1, column=0, padx=10, pady=10,sticky="nsew")
frame_box_system_of_equations.grid_columnconfigure(0,weight=1)
frame_box_system_of_equations.grid_columnconfigure(1,weight=1)
frame_box_system_of_equations.grid_rowconfigure(0,weight=1)

#Crear frame que contendrá el sistema de ecuaciones------------------------------------------------------------------------------
frame_system_of_equations=customtkinter.CTkFrame(frame_box_system_of_equations,
                                                 fg_color="#415A77")
frame_system_of_equations.grid(row=2, column=0, padx=10, pady=10)
frame_system_of_equations.grid_columnconfigure(0,weight=1)
frame_system_of_equations.grid_rowconfigure(0,weight=1)

#Titulo para el sitema de ecuaciones
title=customtkinter.CTkLabel(frame_box_system_of_equations,
                             text="Sistema de Ecuaciones 3x3",
                             font=("Century Gothic",22,"bold"),
                             text_color="#212529")
title.grid(row=0,columnspan=2,pady=10)

#Estilos de los inputs que contiene el frame del sistema de ecuaciones
style_entry = {
    "width":75,
    "font":("Century Gothic",18),
    "fg_color":"#E4EBF1",
     "border_width":0,
     "text_color":"#000"
}
#Estilos para los label que contienen el frame del sistema de ecuaciones
style_label_sign = {
    "font":("Century Gothic",18,"bold"),
     "text_color":"#E0E1DD"
}

#Titulo que indica que se deben ingresar los valores de los coeficientes del sistema de  ecuaciones
title_enter_values=customtkinter.CTkLabel(frame_box_system_of_equations,
                             text="Ingresar los coeficientes del sistema de ecuaciones.",
                             font=("Century Gothic",15,"bold"),
                             text_color="#212529")
title_enter_values.grid(column=0,row=1)

#Creación de inputs para ingresar los valores del sistema de ecuaciones---------------------------------------------
entries = []
labels=[]
for i in range(3):
    row_entries = []
    row_labels=[]
    for j in range(4):
        entry = customtkinter.CTkEntry(frame_system_of_equations,**style_entry )
        entry.grid(row=i, column=j*2, padx=10, pady=10)
        row_entries.append(entry)
        if j==0:
            label = customtkinter.CTkLabel(frame_system_of_equations,text="X₁ +",**style_label_sign )
            label.grid(row=i, column=j*2+1, padx=10, pady=10)
        elif j==1:
            label = customtkinter.CTkLabel(frame_system_of_equations,text="X₂ +",**style_label_sign )
            label.grid(row=i, column=j*2+1, padx=10, pady=10)
        elif j==2:
            label = customtkinter.CTkLabel(frame_system_of_equations,text="X₃ =",**style_label_sign )
            label.grid(row=i, column=j*2+1, padx=10, pady=10)
        row_labels.append(label)
    labels.append(row_labels)
    entries.append(row_entries)
    
    #estilos para los label que mostrarán mensajes de validación
style_label_error = {
    "font":("Century Gothic",15,"bold"),
    "fg_color":"#FFCCD5",
    "text_color":"#800f2f",
    "corner_radius":4
}

#Label para mostrar errores correspondientes al sistema de ecuaciones
label_error=customtkinter.CTkLabel(frame_box_system_of_equations,text="", 
                **style_label_sign)
label_error.grid(row=4,columnspan=2,pady=5)

def save_values():
    """Funcion para guardar valores y validar datos numericos""" #------------------------------------------------------
    values = []
    for row in entries:
        row_values = []
        for entry_value in row:
            value_entry = entry_value.get()
            row_values.append(value_entry)
        values.append(row_values)
    values_of_the_system_of_equations=numpy.array(values)
        
    if numpy.any(numpy.vectorize(lambda x: x.strip() == "")(values_of_the_system_of_equations)):
        label_error.configure(text="Error: Hay elementos vacíos en el sistema de ecuaciones.")
        label_error.configure(** style_label_error)
        return None     
    try:
        conversion_values_of_the_system_of_equations=values_of_the_system_of_equations.astype(float)
        label_error.configure(text="")
        label_error.configure(fg_color="#778DA9")
        return conversion_values_of_the_system_of_equations
    
    except ValueError:
        label_error.configure(text="Error:Son permitidos solo valores numericos.")
        label_error.configure(** style_label_error)
        return None

#Frame para mostrar el sistema de ecuaciones con intercambio de filas si es necesario------------------------------------------
frame_system_of_equations_sorted=customtkinter.CTkFrame(frame_box_system_of_equations,
                                                 fg_color="#415A77")
frame_system_of_equations_sorted.grid(row=2, column=1, padx=10, pady=10)
frame_system_of_equations_sorted.grid_columnconfigure(0,weight=1)
frame_system_of_equations_sorted.grid_rowconfigure(1,weight=1)

#Configuracion de los estilos de los label
style_label = {
    "width":75,
    "font":("Century Gothic",18),
    "fg_color":"#E4EBF1",
    "corner_radius":4,
     "text_color":"#000"
}
#Titulo para indicar que se va a mostrar el sistema de ecuaciones ordenado
title_show_values=customtkinter.CTkLabel(frame_box_system_of_equations,
                             text="Sistema de ecuaciones ordenado.",
                             font=("Century Gothic",15,"bold"),
                             text_color="#212529")
title_show_values.grid(column=1,row=1)

#Creación de campos de texto para mostrar los valores del sistema de ecuaciones ordenado
labels_values = []
labels_sign=[]
for i in range(3):
    row_labels_values = []
    row_labels_sign=[]
    for j in range(4):
        label_coefficient = customtkinter.CTkLabel(frame_system_of_equations_sorted,**style_label,text="")
        label_coefficient.grid(row=i, column=j*2, padx=10, pady=10)
        row_labels_values.append(label_coefficient)
        if j==0:
            label_sign = customtkinter.CTkLabel(frame_system_of_equations_sorted,text="X₁ +",**style_label_sign )
            label_sign.grid(row=i, column=j*2+1, padx=10, pady=10)
        elif j==1:
            label_sign = customtkinter.CTkLabel(frame_system_of_equations_sorted,text="X₂ +",**style_label_sign )
            label_sign.grid(row=i, column=j*2+1, padx=10, pady=10)
        elif j==2:
            label_sign = customtkinter.CTkLabel(frame_system_of_equations_sorted,text="X₃ =",**style_label_sign )
            label_sign.grid(row=i, column=j*2+1, padx=10, pady=10)
        row_labels_sign.append(label_sign)
    labels.append(row_labels_sign)
    labels_values.append(row_labels_values)

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
        for r in range(3):
            for c in range(r+1, 3):
                if numpy.array_equal(system_of_equations[r], system_of_equations[c]):
                    label_error.configure(** style_label_error)
                    label_error.configure(text="Filas idénticas. El sistema de ecuaciones no tiene solución única.")
                    return None
    #Sistema de ecuaciones proporcional------------------------------------------------------------------------------
        n_rows = system_of_equations.shape[0]
        for r in range(n_rows):
            for c in range(r + 1, n_rows):
                # Evitar filas que sean completamente ceros
                if numpy.all(system_of_equations[r] == 0) or numpy.all(system_of_equations[c] == 0):
                    continue
            
                # Calcular el ratio entre las dos filas, manejar divisiones por 0
                with numpy.errstate(divide='ignore', invalid='ignore'):
                    ratio = numpy.divide(system_of_equations[r], system_of_equations[c])
                
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
        for r in range(3):
            row_sum = sum(abs(system_of_equations[r][c]) for c in range(3) if r != c)
            if abs(system_of_equations[i][i]) <= row_sum:
                return False
        return True
    return None

def sort_equations():
    """Funcion para ordenar las ecuaciones e intercambiar filas si es necesario"""#------------------------------------------
    system_of_equations=identical_or_proportional_rows()
    if system_of_equations is not None:
        n = len(system_of_equations)
        for r in range(n):
            max_row = r
            for c in range(r + 1, n):
                if abs(system_of_equations[c, r]) > abs(system_of_equations[max_row, r]):
                    max_row = c
            if max_row != r:
                system_of_equations[r], system_of_equations[max_row] = system_of_equations[max_row].copy(), system_of_equations[r].copy()
    return system_of_equations   

def get_dominant_diagonal_sum_absolute_values():
    """Función oara verificar si el sistema de ecuaciones con permutación, se puede obtener la diagonal dominante"""
    system_of_equations=sort_equations()
    if system_of_equations is not None:
        n = len(system_of_equations)
        for r in range(n):
            diagonal = abs(system_of_equations[r][r])
            suma_fila = sum(abs(system_of_equations[r][c]) for c in range(n) if c != r)
            if diagonal <= suma_fila:
                return system_of_equations      
        return system_of_equations 
    return None

def get_dominant_diagonal_greater_value():
    """Función para validar que los valores de la diagonal principal son mayores a los valores de la fila y columna y obtener la diagonal dominante"""
    system_of_equations=get_dominant_diagonal_sum_absolute_values()
    if system_of_equations is not None:
        rows, columns = system_of_equations.shape
        for r in range(rows):
            for c in range(columns):
                diagonal = abs(system_of_equations[r][r])
                if diagonal>abs(system_of_equations[r,c]) and diagonal>system_of_equations[c,r]:
                    return system_of_equations   
    return None

def show_system_of_equations():
    """Función para mostrar el sistema de ecuaciones valido"""
    system_of_equations=get_dominant_diagonal_greater_value()
    if system_of_equations is False:
        label_error.configure(** style_label_error)
        label_error.configure(text="No es posible obtener la diagonal dominante")
        return None
    if system_of_equations is not None:
        for r in range(3):
            for c in range(4):
                labels_values[r][c].configure(text=system_of_equations[r,c])
        return system_of_equations    
    return None

style_entry_others_values = {
    "font":("Century Gothic",20),
    "fg_color":"#E0E1DD",
     "border_width":0,
     "text_color":"#000",
}

#Estilos de los titulos de los inputs para ingresar otros valores-------------------------------------------------------------
style_label_others_values = {
    "font":("Century Gothic",15,"bold"),
     "text_color":"#c0cad8"
}

#Estilos para los botones------------------------------------------------------------------------------------------------------
style_button = {
    "font":("Century Gothic",15,"bold"),
     "text_color":"#000",
     "corner_radius":50,
     "border_width":3
}

#Boton para validar que el sistema de ecuaciones y organizar el sistema de ecuaciones si es necesario--------------------------
button_validate=customtkinter.CTkButton(frame_box_system_of_equations,text="Validar",
                                     fg_color="#FF85A1",border_color="#FF477E",
                                     hover_color="#FF477E",command=show_system_of_equations,**style_button
                                     )
button_validate.grid(row=5, columnspan=2,padx=10,pady=5,ipady=5)

#Frame para definir los valores iniciales y el valor relativo de error-------------------------------------------------------
frame_enter_others_values=customtkinter.CTkFrame(frame_box_system_of_equations,height=30,
                                                 fg_color="#415A77")
frame_enter_others_values.grid(row=6,columnspan=2,pady=10,padx=10)

#Array para almacenar los codigos para los subindices
sub_indices = ['\u2081', '\u2082', '\u2083']

#Creación de los input para ingresar los valores iniciales, el error relativo y seleccionar variable
entries_initial_values_and_error = []
labels_initial_values=[]
for i in range(1):
    row_entries_initial_values_and_error = []
    row_labels_initial_values=[]
    for j in range(4):
        if j != 3:
            label_initial_values_and_error = customtkinter.CTkLabel(frame_enter_others_values,text=f"Valor Inicial X{sub_indices[j]}",**style_label_others_values )
            label_initial_values_and_error.grid(row=i, column=j, padx=5)
            row_labels_initial_values.append(label_initial_values_and_error)
            labels_initial_values.append(row_labels_initial_values)
            
        entry_initial_values_and_error = customtkinter.CTkEntry(frame_enter_others_values,**style_entry_others_values)
        entry_initial_values_and_error.grid(row=i+1, column=j, padx=5, pady=10)
        row_entries_initial_values_and_error.append(entry_initial_values_and_error)
        
    entries_initial_values_and_error.append(row_entries_initial_values_and_error)
    
label_error_relative = customtkinter.CTkLabel(frame_enter_others_values,text="Error Relativo",
                               **style_label_others_values )
label_error_relative.grid(row=0, column=3, padx=5)
variables=["X₁","X₂","X₃"]
variable_list=customtkinter.CTkComboBox(frame_enter_others_values,values=variables,
                                        fg_color="#1B263B",text_color="#fff",
                                        border_color="#1b263b",
                                        button_color="#0D1B2A",
                                        button_hover_color="#778DA9",
                                        font=("Century Gothic",18,"bold"),dropdown_text_color="#000",
                                        dropdown_font=("Century Gothic",18),
                                        dropdown_fg_color="#E0E1DD",dropdown_hover_color="#F9BEC7",
                                        )
variable_list.grid(row=1,column=4,padx=10)
label_error_others_values=customtkinter.CTkLabel(frame_box_system_of_equations,text="", 
                **style_label_sign)
label_error_others_values.grid(row=7,columnspan=2,pady=5)

def save_initial_values_and_margin_of_error():
    """Función para guardar todos los valores que son ingresados para los valores iniciales y el maargen de error""" #-------------------------
    values = []
    for row in entries_initial_values_and_error:
        row_values = []
        for entry_value in row:
            value_entry = entry_value.get()
            row_values.append(value_entry)
        values.append(row_values)
    values_initial_values_and_margin_of_error=numpy.array(values)
    values_initial_values_and_margin_of_error[0,3]=values_initial_values_and_margin_of_error[0,3].replace('%','')
    
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
    
    for row in labels_values:
        for label_value in row:
            label_value.configure(text="")
            
    label_error.configure(text="")
    label_error.configure(fg_color="#778DA9")
    label_error_others_values.configure(text="")
    label_error_others_values.configure(fg_color="#778DA9")

frame_button=customtkinter.CTkFrame(frame_box_system_of_equations,fg_color="#778DA9")
frame_button.grid(row=8,columnspan=2,pady=2)

#Botón para limpiar los input 
button_delete=customtkinter.CTkButton(frame_button,text="Borrar",fg_color="#FF85A1",border_color="#FF477E",
                                      hover_color="#FF477E",**style_button,
                                      command=lambda:limpiar_inputs_frames(frame_system_of_equations,frame_enter_others_values))
button_delete.grid(row=0, column=1,padx=10,pady=10,ipady=5)

#Creación y configración de la pestaña para mostrar la solución del sistema de ecuaciones---------------------------------
tab_answers=tab_principal.add("Solución")
tab_answers.columnconfigure(0,weight=1)
#Titulo de la pestaña
title_answers=customtkinter.CTkLabel(tab_answers,
                             text="Solución Sistema de ecuaciones 3x3",
                             font=("Impact",35),text_color="#fff")
title_answers.grid(row=0,column=0)

#Creación y configuración del frame que contiene los elementos de la pestaña para mostrar la solución---------------------
frame_show_solutions=customtkinter.CTkFrame(tab_answers,
                                                    fg_color="#778DA9")
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
                font=("Century Gothic",18),
                 background="#F8F9FA",
                fieldbackground="#E9ECEF",
                foreground="#343A40",
                rowheight=30)

#Eliminación de los border de la tabla
style.layout("Treeview", [('Treeview.treearea', {'sticky': 'nswe'})]) 

#Configuración de los estilos de los encabezados
style.configure("Treeview.Heading",
                font=("Century Gothic",20,"bold"),
                background="#FF99AC",
                foreground="#343A40",
                relief="flat",
                padding=(5,5))

#Personalización de encabezados activos
style.map("Treeview.Heading",
          background=[('active', '#FF5C8A')])
#Personalización de filas seleccionadas
style.map("Treeview", background=[('selected', '#B8CBFF')]) 
style.map("Treeview", foreground=[('selected', '#343A40')])  
 
#Creación de la tabla con ttk
table_of_results= ttk.Treeview(frame_show_solutions, 
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
    """Función para despejar las variables de cada ecuación y realizar las correspondientes iteraciones para obtener la solución"""
    system_of_equations=show_system_of_equations()
    label_error.configure(text="")
    label_error.configure(fg_color="#778DA9")
    values_initial_values_and_margin_of_error=save_initial_values_and_margin_of_error()
    if system_of_equations is not None and values_initial_values_and_margin_of_error is not None:
        tab_principal.set("Solución")
        max_iteration=100
        tolerance=100
        decimals = 4
        for item in table_of_results.get_children():
            table_of_results.delete(item)
        x1_old,x2_old, x3_old = values_initial_values_and_margin_of_error[0,0],values_initial_values_and_margin_of_error[0,1],values_initial_values_and_margin_of_error[0,2]
        for iteration in range(max_iteration):
            if (values_initial_values_and_margin_of_error[0,3])<=tolerance:
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
button_solution=customtkinter.CTkButton(frame_button,text="=",
                                     **style_button,fg_color="#FF85A1",border_color="#FF477E",
                                     hover_color="#FF477E",command=generate_iterations)
button_solution.grid(row=0, column=0,padx=10,pady=10,ipady=5)

tab_user_manual=tab_principal.add("Manual de Uso")
tab_user_manual.columnconfigure(0,weight=1)

app.mainloop()
