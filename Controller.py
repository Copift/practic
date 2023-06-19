from tkinter import *
from tkinter import ttk

from docx import Document

from AgregatorRpd import AgregatorRpd
from Builder import Builder
from Settings import Settings


class Controller():

    def __init__(self,settings: Settings) -> None:
        self.settings=settings




    def start(self):
        window = Tk()
        window.title("RPDs")
        window.geometry("1000x800")


        for c in range(10): window.columnconfigure(index=c, weight=1)
        for r in range(10): window.rowconfigure(index=r, weight=1)
        selectRpd = ttk.Label(text='Выберите нужную РПД')
        selectRpd.grid(row=1,column=1)
        selected_elem =StringVar(value='Choose')
        combobox = ttk.Combobox(values=self.settings.RPDsNames,textvariable=selected_elem)
        combobox.grid(row=1, column=2, columnspan=2)
        selected = ttk.Label()


        def callback(event):
            selected = selected_elem.get()
            s = ''
            select=ttk.Label()
            select.configure(text=selected_elem.get())
            select.grid(row=1, column=2)
            ag = AgregatorRpd(self.settings)
            try:
                result = ag.readDocx(self.settings.ini["PATHS"]["RPDs"] + selected)

                for key in result:
                        s+=f"{key.replace('input.','')} - {result[key]}\n"
                info = ttk.Label()
                info.configure(text=s)
                info.grid(row=3, column=2)
                indexess=[]
                i=0
                for indexes in result['table1']:
                    for index in indexes['indexes']:
                        i+=1
                        indexess.append(index['index'])
                count=i
                i=0











            except Exception as err:
                print(err)

            def build(self):
                builder = Builder(insertData=result, settings=self.settings)
                builder.build()

            build = ttk.Button(text="build", command=build(self))

            build.grid(row=5, column=4)
        combobox.bind("<<ComboboxSelected>>", callback)



        window.mainloop()



