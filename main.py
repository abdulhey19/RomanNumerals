import tkinter
import romanNumerals as rm

screen=tkinter.Tk()
screen.title("Roman Rakamlarını Sayıya Çevirme")
screen.geometry("300x100")


# input alanı
inputNumber=tkinter.Entry(width=30)
inputNumber.config()
# sonuc
labelResult=tkinter.Label(width=35)
labelResult.configure()

# button
buttonResult= tkinter.Button()
buttonResult.config(text="Çevir", command= lambda: convertToRomen(inputNumber, labelResult))

def convertToRomen(inputNumber, labelResult):
    metin=inputNumber.get().strip()
    result = rm.romanConvertToInteger(metin)
    labelResult.configure(text="")
    labelResult.configure(text=result)


inputNumber.place(x=10, y=10)
buttonResult.place(x=200, y=10)
labelResult.place(x=10, y=40)

screen.mainloop()








