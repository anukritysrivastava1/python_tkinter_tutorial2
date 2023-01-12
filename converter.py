from tkinter import *

class Converter:
    def __init__(self):
        window = Tk()
        window.title("Currency Converter")
        window.configure(bg="orange")
        Label(window, font="robotomono 12 bold", bg='orange', text='Amount to convert').grid(row=1, column=1, sticky=W)
        Label(window, font="robotomono 12 bold", bg='orange', text='Conversion Rate').grid(row=2, column=1, sticky=W)
        Label(window, font="robotomono 12 bold", bg='orange', text='Converted Amount').grid(row=3, column=1, sticky=W)


        self.amounttoConvertVar=StringVar()
        Entry(window, textvariable= self.amounttoConvertVar, justify=RIGHT).grid(row=1,column=2)
        self.conversionRateVar=StringVar()
        Entry(window, textvariable= self.conversionRateVar, justify=RIGHT).grid(row=2,column=2)
        self.convertedAmountVar = StringVar()
        lblconvertedAmount = Label(window, font='robotomono 12 bold', bg='orange', textvariable = self.convertedAmountVar).grid(row=3, column=2, sticky =E)


        lblconvertedAmount = Button(window, text='Convert', font='robotomono 12 bold', bg='red', fg='black', command=self.ConvertedAmount).grid(row=4, column=2, sticky=E)
        btdelete_all = Button(window, text='clear', font='robotomono 12 bold', bg='blue', fg='black', command=self.delete_all).grid(row=4, column=6, padx=25,pady=25,sticky=E)

        window.mainloop()


    def ConvertedAmount(self):
        amt=float(self.conversionRateVar.get())
        convertedAmountVar = float(self.amounttoConvertVar.get())*amt
        self.convertedAmountVar.set(format(convertedAmountVar,'10.2f'))
        
    def delete_all(self):
        self.amounttoConvertVar.set('')
        self.conversionRateVar.set('')
        self.convertedAmountVar.set('')

Converter()