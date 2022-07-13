import pyautogui
import keyboard
from tkinter import *
import time


class Click:
    def __init__(self, tus, var, var1, saniye=0):
        self.tus = tus
        self.var = var
        self.saniye = saniye
        self.var1 = var1
        print(var1, "1dwqawd")
        self.secim()

    def secim(self):
        print(self.var1, "qwewqeqwe")
        if self.var1 == 0:
            self.dongubc()
        elif self.var1 == 1:
            self.dongub()

    def kontrol(self):
        global clicker
        if self.var == 1:
            clicker = "right"
        elif self.var == 2:
            clicker = "left"
        return clicker

    def dongub(self):
        clicker = self.kontrol()
        while True:
            if keyboard.is_pressed(self.tus):
                print("----------------")
                pyautogui.mouseDown(button=clicker)
            elif keyboard.is_pressed("ctrl+shift+b"):
                break

    def dongubc(self):
        clicker = self.kontrol()
        print(clicker, "son clicker")
        while True:
            # print("calisiyor")
            if keyboard.is_pressed(self.tus):
                print("****************")
                i = 0
                while i < self.saniye * 6.5:
                    pyautogui.click(clicks=5, button=clicker)
                    time.sleep(0.045)
                    if keyboard.is_pressed("ctrl+shift+b"):
                        break
                    i += 1

            if keyboard.is_pressed("ctrl+shift+b"):
                break

window = Tk()
window.title("CPS Bot")
window.geometry("300x200")
window.resizable(width=False, height=False)

yazi1 = Label(window, text="Makronun çalışcağı tuş(harf): ")
yazi1.place(x=10, y=10)

yazi2 = Label(window, text="Makro basılı kalma süresi(sn): ")
yazi2.place(x=10, y=50)

makrotus = Entry(window, width=8)
makrotus.place(x=215, y=10)


makrosn = Entry(window, width=8)
makrosn.place(x=215, y=50)

yazi4 = Label(window, text="Durdurmak için: (Ctrl+Shift+B)")
yazi4.place(x=10, y=165)

intvar1 = IntVar()
sinirsiz = Checkbutton(window, text="Sürekli basılı tutma", variable=intvar1, offvalue=0, onvalue=1)
sinirsiz.place(x=150, y=80)

clicker = "null"


def baslat():
    global clicker
    Click(tus=str(makrotus.get()), saniye=int(makrosn.get()), var=intvar.get(), var1=intvar1.get())


intvar = IntVar()
sagtik = Radiobutton(window, text="Sağ Tık", variable=intvar, value=1).place(x=5, y=80)
soltik = Radiobutton(window, text="Sol Tık", variable=intvar, value=2).place(x=75, y=80)


button = Button(window, text="Başlat", command=baslat)
button.place(x=225, y=160)

window.mainloop()
