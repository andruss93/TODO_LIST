#importando packages 
from  tkinter import * 
import tkinter.messagebox
#funcion para digitar la lista de tarea
def entertask():
    #A new window to pop up to take input
    input_text=""
    def add():
        input_text=entry_task.get(1.0, "end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title="Advertencia",message="Por favor ingresar la tarea")
        else:
            listbox_task.insert(END,input_text)
            #close the root1 window
            root1.destroy()
    root1=Tk()
    root1.title("Añadir tarea")
    entry_task=Text(root1,width=40,height=4)
    entry_task.pack()
    button_temp=Button(root1,text="Añadir Tarea",command=add)
    button_temp.pack()
    root1.mainloop()
    

#funcion para eliminar tarea lista de tarea
def deletetask():
    #seleccion de item y elminarlos
    selected=listbox_task.curselection()
    listbox_task.delete(selected[0])

def markcompleted():
    marked=listbox_task.curselection()
    temp=marked[0]
    #seleccion de texto e item
    temp_marked=listbox_task.get(marked)
    #actualización
    temp_marked=temp_marked+" ✔"
    #eliminar y luego insertar
    listbox_task.delete(temp)
    listbox_task.insert(temp,temp_marked)


#Crear ventana iniciaL
window=Tk()
#giving a title
window.title("App de TO DO")


#widget del cuadro de lista y la barra de desplazamiento
frame_task=Frame(window)
frame_task.pack()

#elementos del cuadro de la lista

listbox_task = Listbox (frame_task,bg="black",fg='White',height=15,width=50, font= 'Helvetica')
listbox_task.pack(side= tkinter.LEFT)

#Extender la lista si excede el tamaño
scrollbar_task=Scrollbar (frame_task)
scrollbar_task.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

#boton del widget
entry_button=Button(window,text="Añadir Tarea",width=50,command=entertask)
entry_button.pack(pady=3)

delete_button=Button(window,text = "Eliminar Tarea",width=50,command=deletetask)
delete_button.pack(pady=3)

mark_button=Button(window,text="Lista completada",width=50, command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()