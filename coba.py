from tkinter import Tk, Label, Entry, Button
from turingMachine import TuringMachine


class TuringMachineSimulator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Turing Machine Simulator")

        self.label = Label(self.window, text="1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Faktorial\n6. Pangkat\n7. Logaritma Biner\n8. Akar Kuadrat")
        self.label.pack()

        self.menu_entry = Entry(self.window)
        self.menu_entry.pack()

        self.submit_button = Button(self.window, text="Submit", command=self.handle_submit)
        self.submit_button.pack()

        self.result_label = Label(self.window, text="")
        self.result_label.pack()

        self.window.mainloop()

    def handle_submit(self):
        menu = self.menu_entry.get()

        if menu == '1':
            self.result_label.configure(text="Penjumlahan")
            angka1_entry = Entry(self.window)
            angka1_entry.pack()
            angka2_entry = Entry(self.window)
            angka2_entry.pack()

            submit_button = Button(self.window, text="Submit", command=lambda: self.calculate_penjumlahan(angka1_entry.get(), angka2_entry.get()))
            submit_button.pack()
        elif menu == '2':
            self.result_label.configure(text="Pengurangan")
            angka1_entry = Entry(self.window)
            angka1_entry.pack()
            angka2_entry = Entry(self.window)
            angka2_entry.pack()

            submit_button = Button(self.window, text="Submit", command=lambda: self.calculate_pengurangan(angka1_entry.get(), angka2_entry.get()))
            submit_button.pack()
        elif menu == '3':
            self.result_label.configure(text="Perkalian")
            angka1_entry = Entry(self.window)
            angka1_entry.pack()
            angka2_entry = Entry(self.window)
            angka2_entry.pack()

            submit_button = Button(self.window, text="Submit", command=lambda: self.calculate_perkalian(angka1_entry.get(), angka2_entry.get()))
            submit_button.pack()
        elif menu == '4':
            self.result_label.configure(text="Pembagian")
            angka1_entry = Entry(self.window)
            angka1_entry.pack()
            angka2_entry = Entry(self.window)
            angka2_entry.pack()

            submit_button = Button(self.window, text="Submit", command=lambda: self.calculate_pembagian(angka1_entry.get(), angka2_entry.get()))
            submit_button.pack()
        elif menu == '5':
            self.result_label.configure(text="Faktorial")
            angka1_entry = Entry(self.window)
            angka1_entry.pack()

            submit_button = Button(self.window, text="Submit", command=lambda: self.calculate_faktorial(angka1_entry.get()))
            submit_button.pack()

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
        self.result_label.configure(text=f"Hasil: {sign + str(n)}")

    def calculate_pengurangan(self, angka1, angka2):
        tm = TuringMachine()
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

        tm.pengurangan()
        tm.initialize(tape)

        while not tm.halted:
            tm.print()
            tm.step()

        print('Accepted : ', tm.accepted_input())

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
        self.result_label.configure(text=f"Hasil: {sign + str(n)}")

    def calculate_perkalian(self, angka1, angka2):
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

        while not tm.halted:
            tm.print()
            tm.step()

        sumOfZero = 0
        sign = 1
        for x in tm.tape.values():
            if x == '0':
                sumOfZero += 1
            elif x == '-':
                sign *= -1
        sumOfZero *= sign
        perkalian = sumOfZero

        print('Accepted : ', tm.accepted_input())

        self.result_label.configure(text=f"Hasil: {perkalian}")

    def calculate_pembagian(self, angka1, angka2):
        tm = TuringMachine()
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

        tm.pembagian()
        tm.initialize(tape)

        while not tm.halted:
            tm.print()
            tm.step()

        print('Accepted : ', tm.accepted_input())

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
        self.result_label.configure(text=f"Hasil: {sign + str(n)}")

    def calculate_faktorial(self, angka1):
        tm = TuringMachine()
        angka1 = int(angka1)
        tape = {0: 'B'}
        index = 0

        tape[index] = '1'
        index += 1

        for i in range(angka1):
            tape[index] = '0'
            index += 1
        
        tape[index] = '1'
        index += 1


        tm.faktorial()
        tm.initialize(tape)

        while not tm.halted:
            tm.print()
            tm.step()

        print('Accepted : ', tm.accepted_input())

        sumOfZero = 0
        sign = 1
        for x in tm.tape.values():
            if x == '0':
                sumOfZero += 1
            elif x == '-':
                sign *= -1
        sumOfZero *= sign
        faktorial = sumOfZero
        print(f'Hasil: {faktorial}')
        self.result_label.configure(text=f"Hasil: {faktorial}")

    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    simulator = TuringMachineSimulator()
    simulator.run()