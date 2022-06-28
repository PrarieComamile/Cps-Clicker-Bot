import pyautogui
import keyboard
from tkinter import *
import time

class Click:
    def dongu(self, tus, saniye):
        a = True
        while a:
            if keyboard.is_pressed(tus):
                i = 0
                while i < saniye * 6.5:
                    pyautogui.doubleClick()
                    time.sleep(0.045)
                    i += 1

window = Tk()
window.title("CPS Bot")
window.geometry("300x150")
window.resizable(width=False, height=False)

yazi1 = Label(window, text="Makronun çalışcağı tuş(harf): ")
yazi1.place(x=10, y=10)

yazi2 = Label(window, text="Makro basılı kalma süresi(sn): ")
yazi2.place(x=10, y=50)

makrotus = Entry(window, width=8)
makrotus.place(x=215, y=10)

makrosn = Entry(window, width=8)
makrosn.place(x=215, y=50)

def baslat():
    bot = Click()
    bot.dongu(str(makrotus.get()), int(makrosn.get()))

button = Button(window, text="Başlat", command=baslat)
button.place(x=215, y=90)

window.mainloop()

