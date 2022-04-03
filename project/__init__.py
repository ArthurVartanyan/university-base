from tkinter import *
from tkinter.ttk import Combobox

from tkcalendar import DateEntry

window = Tk()
window.title("ВГУ - электронная учетная книжка")
window.geometry("900x600")
window.configure(background='#cee8f5')

infoText = Label(window, text="Электронный учет студентов", font="Arial 33")
infoText.place(relx=.2, rely=.1)
infoText.configure(background='#cee8f5')

name = Entry(window)
name.place(relx=.4, rely=.25, width=140)
name_label = Label(window, text="Имя:", font="Arial 13")
name_label.place(x=301, y=143)
name_label.configure(background='#cee8f5')

last_name = Entry(window)
last_name.place(relx=.4, rely=.30, width=140)
last_name_label = Label(window, text="Фамилие:", font="Arial 13")
last_name_label.place(x=260, y=173)
last_name_label.configure(background='#cee8f5')

patronymic = Entry(window)
patronymic.place(relx=.4, rely=.35, width=140)
patronymic_label = Label(window, text="Отчество:", font="Arial 13")
patronymic_label.place(x=257, y=205)
patronymic_label.configure(background='#cee8f5')

birthday_date = DateEntry(window)
birthday_date.place(relx=.4, rely=.40, width=140)
birthday_date_label = Label(window, text="Дата рождения:", font="Arial 13")
birthday_date_label.place(x=212, y=237)
birthday_date_label.configure(background='#cee8f5')

pass_serial = Entry(window)
pass_serial.place(relx=.4, rely=.45, width=140)
pass_serial_label = Label(window, text="Серия паспорта:", font="Arial 13")
pass_serial_label.place(x=207, y=267)
pass_serial_label.configure(background='#cee8f5')

pass_num = Entry(window)
pass_num.place(relx=.4, rely=.50, width=140)
pass_num_label = Label(window, text="Номер паспорта:", font="Arial 13")
pass_num_label.place(x=207, y=296)
pass_num_label.configure(background='#cee8f5')

faculty_name = Combobox(window, values=[
    "ПММ",
    "Математический",
    "Физический",
    "Фармацевтический",
    "Юридический",
    "Экономический"])
faculty_name.place(relx=.4, rely=.55)
faculty_name_label = Label(window, text="Факультет:", font="Arial 13")
faculty_name_label.place(x=249, y=327)
faculty_name_label.configure(background='#cee8f5')

stud_num = Entry(window)
stud_num.place(relx=.4, rely=.60, width=140)
stud_num_label = Label(window, text="Номер билета:", font="Arial 13")
stud_num_label.place(x=225, y=357)
stud_num_label.configure(background='#cee8f5')

addButton = Button(window, text="Добавить!")
addButton.place(relx=.4, rely=.70, width=140)

window.mainloop()
