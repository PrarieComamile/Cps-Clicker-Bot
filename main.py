import pyautogui
import keyboard
from tkinter import *
import time

class Click:
    def dongu(self, tus, var, saniye=0):
        print(var)
        if var == 1:
            while True:
                # print("calisiyor")
                if keyboard.is_pressed(tus):
                    print("****************")
                    i = 0
                    while i < saniye * 6.5:
                        pyautogui.rightClick()
                        time.sleep(0.045)
                        if keyboard.is_pressed("ctrl+shift+b"):
                            break
                        i += 1

                if keyboard.is_pressed("ctrl+shift+b"):
                    break
        if var == 2:
            while True:
                # print("calisiyor")
                if keyboard.is_pressed(tus):
                    print("****************")
                    i = 0
                    while i < saniye * 6.5:
                        pyautogui.leftClick()
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


def baslat():
    bot = Click()
    bot.dongu(tus=str(makrotus.get()), saniye=int(makrosn.get()), var=intvar.get())


intvar = IntVar()
sagtik = Radiobutton(window, text="Sağ Tık", variable=intvar, value=1).place(x=5, y=75)
soltik = Radiobutton(window, text="Sol Tık", variable=intvar, value=2).place(x=75, y=75)

button = Button(window, text="Başlat", command=baslat)
button.place(x=225, y=160)

window.mainloop()

