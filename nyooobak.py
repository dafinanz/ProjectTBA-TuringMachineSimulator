from collections import defaultdict
from tkinter import Tk, Label, Entry, Button
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

        self.output_label = Label(self.window, text="")
        self.output_label.pack()

        self.turing_machine = TuringMachine()  # Membuat objek TuringMachine
        self.window.mainloop()

    def initialize(self, input_symbols: 'dict[int, str]', initial_state: str):
        self.head = 0
        self.halted = False
        self.current_state = initial_state
        self.tape = defaultdict(lambda: self.blank_symbol, input_symbols)
        self.tape_string = []

    def step(self):
        if self.halted:
            raise RuntimeError('Cannot step halted machine')

        try:
            state, symbol, direction = self.turing_machine.transitions[(self.current_state, self.tape[self.head])]
        except KeyError:
            self.halted = True
            return

        self.tape[self.head] = symbol
        self.current_state = state
        self.head += direction

        self.print()  # Memanggil metode print
        self.window.update()  # Memperbarui tampilan GUI
        self.window.after(500)  # Jeda waktu 500 ms

    def handle_submit(self):
        menu = self.menu_entry.get()

        if menu == '3':
            self.result_label.configure(text="Perkalian")
            angka1_entry = Entry(self.window)
            angka1_entry.pack()
            angka2_entry = Entry(self.window)
            angka2_entry.pack()

            submit_button = Button(self.window, text="Submit", command=lambda: self.calculate_multiplication(angka1_entry.get(), angka2_entry.get()))
            submit_button.pack()

    def calculate_multiplication(self, angka1, angka2):
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

        tm.multiplicationMode()
        self.initialize(tape, 'q0')
        while not self.halted:
            self.step()

        sumOfZero = 0
        sign = 1
        for x in self.tape.values():
            if x == '0':
                sumOfZero += 1
            elif x == '-':
                sign *= -1
        sumOfZero *= sign
        perkalian = sumOfZero

        self.result_label.configure(text=f"Hasil: {perkalian}")

    def print(self):
        output = '... ' + ' '.join(self.tape[i] for i in range(self.head - 10, self.head + 11)) + f' ... state={self.current_state}'
        self.output_label.configure(text=output)

if __name__ == '__main__':
    simulator = TuringMachineSimulator()
