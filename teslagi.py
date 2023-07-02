from tkinter import *
from tkinter import ttk
from turingMachine import TuringMachine


class TuringMachineSimulator:
    def __init__(self):
        self.window = Tk()
        self.window.title = Label(self.window, text="Turing Machine Simulator", width=500, anchor='center', background="#3c8aae", justify='center')
        self.window.title.config(font=("Roboto", 20), foreground="white", padx=10, pady=10)
        self.window.title.pack(pady=(0, 20))
        self.window.geometry("800x600")

        self.label = Label(self.window, text="Menu:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Faktorial\n6. Pangkat\n7. Logaritma Biner\n8. Akar Kuadrat\n", font=("Roboto", 10) , justify="left")
        self.label.pack(anchor='w')

        self.label = Label(self.window, text="Choose your Menu:", justify="left")
        self.label.pack(anchor='w')

        self.menu_entry = Entry(self.window)
        self.menu_entry.pack(anchor='w')

        self.submit_button = Button(self.window, text="Submit", command=self.handle_submit)
        self.submit_button.pack(side='left')

        self.restart_button = Button(self.window, text="Restart", command=self.restart_program)
        self.restart_button.pack(side='left', padx=(10, 0))

        self.canvas_frame = Canvas(self.window, width=400, height=200)
        self.canvas_frame.pack(side='left', fill='both', expand=True)

        self.canvas = Canvas(self.canvas_frame)
        self.canvas.pack(side='left', fill='both', expand=True)

        self.scrollbar = Scrollbar(self.canvas_frame, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame_output = ttk.LabelFrame(self.window, text="Output", width=600)
        self.frame_output.pack()

        self.canvas_output = Canvas(self.frame_output, width=400, height=200)
        self.canvas_output.pack()

        self.window.mainloop()

    def handle_submit(self):
        menu = self.menu_entry.get()

        if menu == '1':
            result_label = Label(self.window, text="\nPenjumlahan")
            result_label.pack(anchor='w')
            input1 = Label(self.window, text="Angka 1")
            input1.pack(anchor='w')
            angka1_entry = Entry(self.window)
            angka1_entry.pack(anchor='w')
            input2 = Label(self.window, text="Angka 2")
            input2.pack(anchor='w')
            angka2_entry = Entry(self.window)
            angka2_entry.pack(anchor='w')

            submit_operation = Button(self.window, text="Go", command=lambda: self.calculate_penjumlahan(angka1_entry.get(), angka2_entry.get()))
            submit_operation.pack(anchor='w')

        elif menu == '2':
            result_label = Label(self.window, text="\nPengurangan")
            result_label.pack(anchor='w')
            input1 = Label(self.window, text="Angka 1")
            input1.pack(anchor='w')
            angka1_entry = Entry(self.window)
            angka1_entry.pack(anchor='w')
            input2 = Label(self.window, text="Angka 2")
            input2.pack(anchor='w')
            angka2_entry = Entry(self.window)
            angka2_entry.pack(anchor='w')

            submit_operation = Button(self.window, text="Go", command=lambda: self.calculate_pengurangan(angka1_entry.get(), angka2_entry.get()))
            submit_operation.pack(anchor='w')

    def calculate_penjumlahan(self, angka1, angka2):
        angka1 = int(angka1)
        angka2 = int(angka2)
        tape = {0: 'B'}
        index = 1

        index -= 1
        if angka1 < 0:
            angka1 = angka1 * -1
            tape[index] = '-'
            index += 1
            for i in range(angka1):
                tape[index] = '0'
                index += 1
        else:
            tape[index] = '+'
            index += 1
            for i in range(angka1):
                tape[index] = '0'
                index += 1

        tape[index] = '1'
        index += 1

        if angka2 < 0:
            angka2 = angka2 * -1
            tape[index] = '-'
            index += 1
            for i in range(angka2):
                tape[index] = '0'
                index += 1
        else:
            tape[index] = '+'
            index += 1
            for i in range(angka2):
                tape[index] = '0'
                index += 1
        
        tape[index] = '1'
        index += 1

        tm = TuringMachine()

        tm.penjumlahan()
        tm.initialize(tape)

        while not tm.halted:
            tm.print()
            tm.step()

        print('Accepted : ', tm.accepted_input())
        result_accept = Label(self.window, text=f"Accepted : {tm.accepted_input()}")
        result_accept.pack(anchor='w')

        n = 0
        sign = ''
        for i in tm.tape.values():
            if i == '-':
                sign = '-'
            elif i == '+':
                sign = '+'   
            elif i == '0':
                n += 1
            elif i == '-0':
                n -= 1
        print('Hasil =', sign + str(n))
        result_calculation = Label(self.window, text=f"{angka1} + {angka2} = {sign + str(n)}")
        result_calculation.pack(anchor='w')

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

    def restart_program(self):
        self.window.destroy()
        TuringMachineSimulator()

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    simulator = TuringMachineSimulator()
    simulator.run()
