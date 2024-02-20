import os, sys, subprocess
import platform
import customtkinter
import customtkinter as ctk
from customtkinter import *

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')


# root
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Elevator')
        self.geometry('1000x1200')

        global Base
        Base = 540

        global First
        First = 340

        global Second
        Second = 140

        # Main Canvas
        self.canvas = CTkCanvas(self, width=250, height=600, background='black')
        self.canvas.place(x=500, y=370, anchor='w')
        self.text = CTkTextbox(self.canvas, width=100, height=120, fg_color='white')

        # Floors
        for n in range(0, 600, 200):
            self.canvas.create_line(0, n, 400, n, fill="white", width=4)

        # Define the Doors/ floors button
        self.restart = CTkButton(self, text='Restart', command=self.restart)
        self.restart.grid(row=0, column=3, padx=20, pady=10)

        self.ground_floor_button = CTkButton(self, text='C', command=self.second)
        self.ground_floor_button.grid(row=1, column=1, padx=20, pady=10)

        self.first_floor_button = CTkButton(self, text='B', command=self.first)
        self.first_floor_button.grid(row=2, column=1, padx=20, pady=10)

        self.second_floor_button = CTkButton(self, text='A', command=self.ground)
        self.second_floor_button.grid(row=3, column=1, padx=20, pady=10)

        self.floors = ['Second', 'First', 'Ground']
        self.choose_floor = CTkComboBox(self, values=self.floors, corner_radius=50, command=self.get_choice)
        self.choose_floor.grid(row=1, column=0, padx=20, pady=0)

        # Labels
        self.floor_label = CTkLabel(self, text="Choose current floor", font=('Helvetica', 15, 'bold'))
        self.floor_label.grid(row=0, column=0, padx=15, pady=5)
        self.floor_label = CTkLabel(self, text="Choose target floor", font=('Helvetica', 15, 'bold'))
        self.floor_label.grid(row=0, column=1, padx=2, pady=5)

    def get_choice(self, choice):
        # print(self.choose_floor.get())
        # print(type(self.choose_floor.get()))
        return self.choose_floor.get()

    def ground(self):
        self.current_floor = self.get_choice(choice=self.choose_floor.get())

        global First
        global Base
        global Second
        # second += 20

        if self.current_floor == 'Second' and Second <= Base:
            self.text.place(x=60, y=Second, anchor='center')
            self.after(80, self.ground)
            Second += 20

        elif self.current_floor == 'First' and First <= Base:
            self.text.place(x=60, y=First, anchor='center')
            self.after(80, self.ground)
            First += 20

        elif self.current_floor == 'Ground' and Base == Base:
            self.floor_label = CTkLabel(self, text="You're on the ground floor", font=('Helvetica', 20, 'bold'))
            self.floor_label.grid(row=4, column=1, padx=2, pady=5)
            del self.floor_label

    def first(self):
        self.current_floor = self.get_choice(choice=self.choose_floor.get())

        global First
        global Base
        global Second

        if self.current_floor == 'Second' and Second <= First:
            self.text.place(x=60, y=Second, anchor='center')
            self.after(80, self.first)
            Second += 20

        elif self.current_floor == 'Ground' and Base >= First:
            self.text.place(x=60, y=Base, anchor='center')
            self.after(80, self.first)
            Base -= 20

        elif self.current_floor == 'First' and First == First:
            self.floor_label = CTkLabel(self, text="You're on the first floor", font=('Helvetica', 20, 'bold'))
            self.floor_label.grid(row=4, column=1, padx=2, pady=5)
            del self.floor_label

    def second(self):
        self.current_floor = self.get_choice(choice=self.choose_floor.get())

        global First
        global Base
        global Second

        if self.current_floor == 'Ground' and Base >= Second:
            self.text.place(x=60, y=Base, anchor='center')
            self.after(80, self.second)
            Base -= 20

        elif self.current_floor == 'First' and First >= Second:
            self.text.place(x=60, y=First, anchor='center')
            self.after(80, self.second)
            First -= 20

        elif self.current_floor == "Second" and Second == Second:
            self.floor_label = CTkLabel(self, text="You're on the second floor", font=('Helvetica', 20, 'bold'))
            self.floor_label.grid(row=4, column=1, padx=2, pady=5)
            del self.floor_label

    def restart(self):
        self.destroy()
        self.command = [sys.executable] + sys.argv
        subprocess.call(self.command)
        sys.exit()


def main():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()
