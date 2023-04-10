from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox
import os


def accion():
    global formatoSelecccionado

    if formatoSelecccionado == "MP4":
        try:
            MessageBox.showinfo(root,
                                    message="Formato " + str(formatoSelecccionado))
            enlace = videos.get()
            video = YouTube(enlace)
            descarga = video.streams.get_highest_resolution()
            descarga.download(output_path=os.path.join(os.environ['USERPROFILE'],"Videos\\"))
            MessageBox.showinfo(root, message="Descarga finalizada")
        except:
            MessageBox.showerror(root,
                                message="No se pudo obtener el video")
    elif formatoSelecccionado == "MP3":
        try:
            MessageBox.showinfo(root,
                                    message="Formato " + str(formatoSelecccionado))
            enlace = videos.get()
            video = YouTube(enlace)
            descarga = video.streams.get_audio_only()
            descarga.download(output_path=os.path.join(os.environ['USERPROFILE'],"Music\\"))
            os.rename(os.path.join(os.environ['USERPROFILE'],"Music\\" + video.title + ".mp4"), os.path.join(os.environ['USERPROFILE'],"Music\\" + video.title + ".mp3"))
            MessageBox.showinfo(root, message="Descarga finalizada")
        except:
            MessageBox.showerror(root,
                                 message="No se pudo obtener el audio")

    if formatoSelecccionado != "MP3" and formatoSelecccionado != "MP4":
        MessageBox.showerror(root, message="Error de formato")


def popup():
    MessageBox.showinfo(root, message="Creado por David Valls")


def setFormato(choice):
    global formatoSelecccionado
    formatoSelecccionado = variable.get()


root = Tk()
root.config(bd=15)
root.iconbitmap("icon.ico")
root.resizable(False, False)
root.title("Youtube downloader")

imagen = PhotoImage(file="youtube.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_command(label="Acerca de...", command=popup)
menubar.add_command(label="Salir", command=root.destroy)

instrucciones = Label(root, text="Creado en Python\n")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

formatos = ['MP4','MP3']
global formatoSelecccionado
formatoSelecccionado = "MP4"

variable = StringVar()
variable.set("MP4")

dropdown = OptionMenu(
    root,
    variable,
    *formatos,
    command=setFormato,
)
dropdown.grid(row=2, column=1)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=3, column=1)
root.mainloop()