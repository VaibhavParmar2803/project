import csv
from tkinter import *

def take_attendance():
    name = name_entry.get()
    status = status_var.get()
    with open('attendance.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, status])
    name_entry.delete(0, END)
    status_var.set('Present')

root = Tk()
root.title("Student Attendance System")
root.geometry("400x400")

name_label = Label(root, text="Student Name:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

status_label = Label(root, text="Attendance Status:")
status_label.pack()
status_var = StringVar()
status_var.set('Present')
status_radio_present = Radiobutton(root, text='Present', variable=status_var, value='Present')
status_radio_present.pack()
status_radio_absent = Radiobutton(root, text='Absent', variable=status_var, value='Absent')
status_radio_absent.pack()

submit_button = Button(root, text="Submit", command=take_attendance)
submit_button.pack()

root.mainloop()
