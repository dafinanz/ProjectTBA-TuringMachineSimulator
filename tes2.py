from tkinter import Tk, Label, Entry, Button, Canvas, Scrollbar
import tkinter.ttk as ttk
from turingMachine import TuringMachine


class TuringMachineSimulator:

    def __init__(self):
        self.window = Tk()
        self.window.title("Turing Machine Simulator")

        self.label = Label(self.window, text="1. Tambah\n2. Kurang\n3. Kali\n4. Bagi\n5. Faktorial\n6. Pangkat\n7. Logaritma Biner\n8. Akar Kuadrat")
        self.label.pack()

        self.menu_entry = Entry(self.window)
        self.menu_entry.pack()

        self.submit_button = Button(self.window, text="Submit", command=self.handle_submit)
        self.submit_button.pack()

        self.result_label = Label(self.window, text="")
        self.result_label.pack()

        self.canvas_frame = Canvas(self.window, width=800, height=400)
        self.canvas_frame.pack(side='left', fill='both', expand=True)

        self.canvas = Canvas(self.canvas_frame)
        self.canvas.pack(side='left', fill='both', expand=True)

        self.scrollbar = Scrollbar(self.canvas_frame, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame_output = ttk.LabelFrame(self.window, text="Output", width=600)
        self.frame_output.pack()

        self.canvas_output = Canvas(self.frame_output, width=600, height=300)
        self.canvas_output.pack()

        self.window.mainloop()

    def handle_submit(self):
        menu = self.menu_entry.get()

        if menu == '3':
            self.result_label.configure(text="Perkalian")
            angka1_entry = Entry(self.window)
            angka1_entry.pack()
            angka2_entry = Entry(self.window)
            angka2_entry.pack()

            submit_button = Button(self.window, text="Submit", command=lambda: self.perkalian_m(angka1_entry.get(), angka2_entry.get()))
            submit_button.pack()

    def perkalian_m(self, angka1, angka2):
        index = 0
        tape = {}
        if angka1[0] == '-':
            tape[index] = '-'
            index += 1
            angka1 = angka1[1:]
        else:
            tape[index] = '+'
            index += 1

        angka1 = int(angka1)
        for i in range(angka1):
            tape[index] = '0'
            index += 1

        tape[index] = '1'
        index += 1

        if angka2[0] == '-':
            tape[index] = '-'
            index += 1
            angka2 = angka2[1:]
        else:
            tape[index] = '+'
            index += 1

        angka2 = int(angka2)
        for i in range(angka2):
            tape[index] = '0'
            index += 1

        tape[index] = '1'
        index += 1

        tm = TuringMachine()

        tm.perkalian()
        tm.initialize(tape)

        x1, x2 = 0, 40
        y1, y2 = 0, 40
        counter = 0

        while not tm.halted:
            tm.print()
            tm.step()

            self.drawInline(index, x1, x2, y1 + counter * 40, y2 + counter * 40, counter, tm.tape, tm.head)
            counter += 1

        sumOfZero = 0
        sign = 1
        for x in tm.tape.values():
            if x == '0':
                sumOfZero += 1
            elif x == '-':
                sign *= -1
        sumOfZero *= sign
        perkalian = sumOfZero

        self.result_label.configure(text=f"Hasil: {perkalian}")

    def drawInline(self, inputLength, x1, x2, y1, y2, counter, tape, head):
        box_width = 40

        for j in range(inputLength):
            x1 += box_width
            x2 += box_width
            box = self.canvas.create_rectangle(x1, y1, x2, y2, fill="white smoke")
            label = self.canvas.create_text((x1 + x2) / 2, (y1 + y2) / 2, text=tape[j])
            if head == j:
                self.canvas.itemconfig(box, fill="yellow")

        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def run(self):
        self.window.mainloop()


if __name__ == '__main__':
    simulator = TuringMachineSimulator()
    simulator.run()
