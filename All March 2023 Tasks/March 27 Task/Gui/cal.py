from tkinter import *
import calendar
import datetime

def show_calender():
    gui=Tk()
    gui.config(background='skyBlue')
    gui.title("CALENDER FOR THE YEAR")
    gui.geometry("630x500")
    
    year=datetime.date.today().year
    cal=calendar.calendar(year)
    calenderYear = Label(gui, text= cal, font= "bold",width=70)
    calenderYear.grid(row=3, column=1,padx=300)
    gui.mainloop()
    
#Driver code
if __name__=='__main__':
        new = Tk()
        new.title("Calender")
        new.geometry("350x240")
        text=Text(new)
        cal = Label(new, text="Calender",bg='yellow',font=("times", 24, "bold"))
        year = Label(new, text="Enter year",)
        year_field=Entry(new)
        button = Button(new, text='Show Calender',
        fg='Black',bg='orange',command=show_calender)


        cal.grid(row=1, column=2)
        year.grid(row=2, column=2)
        year_field.grid(row=3, column=2)
        button.grid(row=4, column=2)
        new.mainloop()
