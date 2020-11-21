from tkinter import *

def DrawSystemWindow():
    BootloaderWindow = Tk()
    BootloaderWindow.title('Install SolOS Yukon (3.0)')
    BootloaderWindow.geometry('800x600')
    BootloaderWindow.config(bg='black')
    BootloaderWindow.attributes('-fullscreen',True)

    BootText = Text(BootloaderWindow,font='Piboto',bg='black',fg='white')
    BootText.pack(anchor='nw')

    BootText.insert(0.1,'About to launch BootRestartGLDR.pkg')

    BootloaderWindow.mainloop()

DrawSystemWindow()


