from tkinter import *
import psutil

def DrawSystemWindow():
    SystemInstaller = Tk()
    SystemInstaller.title('Install SolOS Yukon (3.0)')
    SystemInstaller.geometry('800x600')

    FirstBootWindow = Toplevel()
    FirstBootWindow.title('Install SolOS Yukon (3.0)')
    FirstBootWindow.config(bg='#000000')
    FirstBootWindow.attributes('-fullscreen',True)

    def ClearRoot():
        for widget in SystemInstaller.winfo_children():
            if widget != FirstBootWindow:
                widget.destroy()

    InstallerSubTitle1 = 'Click next to continue the SolOS Installation. Close the window to exit the installer.'

    InstallerTitle = Label(SystemInstaller,text='Welcome to the SolOS Installer',font=('Piboto',40))
    InstallerTitle.pack(padx=10,pady=(20,2))
    InstallerSubTitle = Label(SystemInstaller,text=InstallerSubTitle1,font=('Piboto',15))
    InstallerSubTitle.pack(padx=10,pady=(2,20))

    def InstallScreen1():
        ClearRoot()
        InstallerSubTitle2 = 'Click on a disk, volume, or image to install SolOS to.'
        InstallerTitle = Label(SystemInstaller,text='Choose where to install SolOS',font=('Piboto',40))
        InstallerTitle.pack(padx=10,pady=(20,2))
        InstallerSubTitle = Label(SystemInstaller,text=InstallerSubTitle2,font=('Piboto',15))
        InstallerSubTitle.pack(padx=10,pady=(2,20))

        SystemInformationDiskDialog = Frame(SystemInstaller)
        SystemInformationDiskDialog.pack(padx=10,pady=20)

        for DiskObject in psutil.disk_partitions():
            print(DiskObject)

        FinishInstall = Button(SystemInstaller,text='        Next        ',command=InstallScreen1)
        FinishInstall.pack(side='bottom',padx=10,pady=20)


    
    FinishInstall = Button(SystemInstaller,text='        Next        ',command=InstallScreen1)
    FinishInstall.pack(side='bottom',padx=10,pady=20)

    SystemIcon = PhotoImage(file='SetupImage.png')
    SystemBootIcon = Label(FirstBootWindow,image=SystemIcon,bg='#000000')
    SystemBootIcon.pack()

    SystemInstaller.mainloop()

DrawSystemWindow()


