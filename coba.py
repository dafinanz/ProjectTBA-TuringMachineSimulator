# from tkinter import Tk, Label, Entry, Button
from tkinter import *
from turingMachine import TuringMachine

class TuringMachineSimulator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Turing Machine Simulator")
        self.window.geometry("800x600")

        self.label = Label(self.window, text="Pilihan:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Faktorial\n6. Pangkat\n7. Logaritma Biner\n8. Akar Kuadrat\n", justify="left")
        self.label.pack(anchor='w')

        self.label = Label(self.window, text="Pilihan:", justify="left")
        self.label.pack(anchor='w')

        self.menu_entry = Entry(self.window)
        self.menu_entry.pack(anchor='w')

        self.submit_button = Button(self.window, text="Submit", command=self.handle_submit)
        self.submit_button.pack(anchor='w')

        self.restart_button = Button(self.window, text="Restart", command=self.restart_program)
        self.restart_button.pack(anchor='w')

        self.result_label = Label(self.window, text="")
        self.input1 = Label(self.window, text="Angka 1")
        self.angka1_entry = Entry(self.window)
        self.input2 = Label(self.window, text="Angka 2")
        self.angka2_entry = Entry(self.window)
        self.submit_operation = Button(self.window, text="")

        self.window.mainloop()

    def handle_submit(self):
        menu = self.menu_entry.get()

        if menu == '1':
            self.result_label.config(text="\nPenjumlahan")
            self.result_label.pack(anchor='w')

            self.input1.pack(anchor='w')
            self.angka1_entry.pack(anchor='w')
            self.input2.pack(anchor='w')
            self.angka2_entry.pack(anchor='w')

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_penjumlahan(self.angka1_entry.get(), self.angka2_entry.get()))
            self.submit_operation.pack(anchor='w')
        elif menu == '2':
            self.result_label.config(text="\nPengurangan")
            self.result_label.pack(anchor='w')

            self.input1.pack(anchor='w')
            self.angka1_entry.pack(anchor='w')
            self.input2.pack(anchor='w')
            self.angka2_entry.pack(anchor='w')

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_pengurangan(self.angka1_entry.get(), self.angka2_entry.get()))
            self.submit_operation.pack(anchor='w')
        elif menu == '3':
            result_label = Label(self.window, text="\nPerkalian")
            result_label.pack(anchor='w')
            input1 = Label(self.window, text="Angka 1")
            input1.pack(anchor='w')
            angka1_entry = Entry(self.window)
            angka1_entry.pack(anchor='w')
            input2 = Label(self.window, text="Angka 2")
            input2.pack(anchor='w')
            angka2_entry = Entry(self.window)
            angka2_entry.pack(anchor='w')

            submit_operation = Button(self.window, text="Go", command=lambda: self.calculate_perkalian(angka1_entry.get(), angka2_entry.get()))
            submit_operation.pack(anchor='w')
        elif menu == '4':
            result_label = Label(self.window, text="\nPembagian")
            result_label.pack(anchor='w')
            input1 = Label(self.window, text="Angka 1")
            input1.pack(anchor='w')
            angka1_entry = Entry(self.window)
            angka1_entry.pack(anchor='w')
            input2 = Label(self.window, text="Angka 2")
            input2.pack(anchor='w')
            angka2_entry = Entry(self.window)
            angka2_entry.pack(anchor='w')

            submit_operation = Button(self.window, text="Go", command=lambda: self.calculate_pembagian(angka1_entry.get(), angka2_entry.get()))
            submit_operation.pack(anchor='w')
        elif menu == '5':
            result_label = Label(self.window, text="\nFaktorial")
            result_label.pack(anchor='w')
            input1 = Label(self.window, text="Angka 1")
            input1.pack(anchor='w')
            angka1_entry = Entry(self.window)
            angka1_entry.pack(anchor='w')

            submit_operation = Button(self.window, text="Submit", command=lambda: self.calculate_faktorial(angka1_entry.get()))
            submit_operation.pack(anchor='w')
        elif menu == '6':
            result_label = Label(self.window, text="\nPangkat")
            result_label.pack(anchor='w')
            input1 = Label(self.window, text="Angka 1")
            input1.pack(anchor='w')
            angka2_entry = Entry(self.window)
            angka2_entry.pack(anchor='w')
            input2 = Label(self.window, text="Angka 2")
            input2.pack(anchor='w')
            angka1_entry = Entry(self.window)
            angka1_entry.pack(anchor='w')

            submit_operation = Button(self.window, text="Submit", command=lambda: self.calculate_pangkat(angka2_entry.get(), angka1_entry.get()))
            submit_operation.pack(anchor='w')
        elif menu == '7':
            result_label = Label(self.window, text="\nLogaritma")
            result_label.pack(anchor='w')
            input1 = Label(self.window, text="Angka 1")
            input1.pack(anchor='w')
            angka1_entry = Entry(self.window)
            angka1_entry.pack(anchor='w')

            submit_operation = Button(self.window, text="Submit", command=lambda: self.calculate_logaritma(angka1_entry.get()))
            submit_operation.pack(anchor='w')
        elif menu == '8':
            result_label = Label(self.window, text="\nAkar Kuadrat")
            result_label.pack(anchor='w')
            input1 = Label(self.window, text="Angka 1")
            input1.pack(anchor='w')
            angka1_entry = Entry(self.window)
            angka1_entry.pack(anchor='w')

            submit_operation = Button(self.window, text="Submit", command=lambda: self.calculate_akarkuadrat(angka1_entry.get()))
            submit_operation.pack(anchor='w')
        else:
            self.result_label.configure(text="Nomor pilihan tidak valid")
        

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
        result_calculation = Label(self.window, text=f"{angka1} - {angka2} = {sign + str(n)}")
        result_calculation.pack(anchor='w')

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
        result_accept = Label(self.window, text=f"Accepted : {tm.accepted_input()}")
        result_accept.pack(anchor='w')

        print('Hasil =', perkalian)
        result_calculation = Label(self.window, text=f"{angka1} x {angka2} = {perkalian}")
        result_calculation.pack(anchor='w')

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
        result_calculation = Label(self.window, text=f"{angka1} / {angka2} = {sign + str(n)}")
        result_calculation.pack(anchor='w')

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
        result_accept = Label(self.window, text=f"Accepted : {tm.accepted_input()}")
        result_accept.pack(anchor='w')

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
        result_calculation = Label(self.window, text=f"{angka1}! = {faktorial}")
        result_calculation.pack(anchor='w')

    def calculate_pangkat(self, angka2, angka1):
        tm = TuringMachine()
        angka2 = int(angka2)
        angka1 = int(angka1)
        tape = {0: 'B'}
        index = 1

        for i in range(angka1):
            tape[index] = '0'
            index += 1

        tape[index] = '1'
        index += 1

        for i in range(angka2):
            tape[index] = '0'
            index += 1

        tape[index] = '1'
        index += 1

        tm.pangkat()
        tm.initialize(tape)

        while not tm.halted:
            tm.print()
            tm.step()

        print('Accepted : ', tm.accepted_input())
        result_accept = Label(self.window, text=f"Accepted : {tm.accepted_input()}")
        result_accept.pack(anchor='w')

        n = 0
        for i in tm.tape.values():
            if i == '0':
                n += 1
            elif i == '-0':
                n -= 1
        print('Hasil = ', n)
        result_calculation = Label(self.window, text=f"{angka2} ^ {angka1} = {n}")
        result_calculation.pack(anchor='w')

    def calculate_logaritma(self, angka1):
        tm = TuringMachine()
        angka1 = int(angka1)
        tape = {0: 'b'}
        index = 0
        for i in range(angka1):
            tape[index] = '0'
            index += 1


        tm.logaritma()
        tm.initialize(tape)

        while not tm.halted:
            tm.print()
            tm.step()

        print('Accepted : ', tm.accepted_input())
        result_accept = Label(self.window, text=f"Accepted : {tm.accepted_input()}")
        result_accept.pack(anchor='w')

        sumOfZero = 0

        for x in tm.tape.values():
            if x == '0':
                sumOfZero += 1

        result = sumOfZero
        print(f'2 Log {angka1} = {result}')
        result_calculation = Label(self.window, text=f"2 Log {angka1} = {result}")
        result_calculation.pack(anchor='w')

    def calculate_akarkuadrat(self, angka1):
        tm = TuringMachine()
        angka1 = int(angka1)
        tape = {0: 'b'}
        index = 0
        for i in range(angka1):
            tape[index] = '0'
            index += 1

            tape[index] = '1'
            index == 1

        tm.akarkuadrat()
        tm.initialize(tape)

        while not tm.halted:
            tm.print()
            tm.step()

        print('Accepted : ', tm.accepted_input())
        result_accept = Label(self.window, text=f"Accepted : {tm.accepted_input()}")
        result_accept.pack(anchor='w')

        sumOfZero = 0

        for x in tm.tape.values():
            if x == '0':
                sumOfZero += 1

        result = sumOfZero
        print(f'Hasil = {result}')
        result_calculation = Label(self.window, text=f"sqrt({angka1}) = {result}")
        result_calculation.pack(anchor='w')

    def restart_program(self):
        self.window.destroy()
        TuringMachineSimulator()
    
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    simulator = TuringMachineSimulator()
    simulator.run()