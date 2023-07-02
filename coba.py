from tkinter import *
from turingMachine import TuringMachine

class TuringMachineSimulator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Turing Machine Simulator")
        self.window.title = Label(self.window, text="Turing Machine Simulator", width=500, anchor='center', background="#3c8aae", justify='center')
        self.window.title.config(font=("Roboto", 20), foreground="white", padx=10, pady=10)
        self.window.title.pack(pady=(0, 20))
        self.window.geometry("800x600")

        self.label = Label(self.window, text="Pilihan:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Faktorial\n6. Pangkat\n7. Logaritma Biner\n8. Akar Kuadrat\n", justify="left")
        self.label.grid(row=0, column=0, sticky="w")

        self.label = Label(self.window, text="Pilihan:", justify="left")
        self.label.grid(row=1, column=0, sticky="w")

        self.menu_entry = Entry(self.window)
        self.menu_entry.grid(row=1, column=1, sticky="w")

        self.submit_button = Button(self.window, text="Submit", command=self.handle_submit)
        self.submit_button.grid(row=2, column=0, sticky="w")

        self.restart_button = Button(self.window, text="Restart", command=self.restart_program)
        self.restart_button.grid(row=2, column=1, sticky="w")

        self.result_label = Label(self.window, text="")

        self.input1 = Label(self.window, text="Angka 1")
        self.angka1_entry = Entry(self.window)

        self.input2 = Label(self.window, text="Angka 2")
        self.angka2_entry = Entry(self.window)

        self.submit_operation = Button(self.window, text="")
        self.result_accept = Label(self.window, text="")
        self.result_calculation = Label(self.window, text="")

        self.window.mainloop()

    def handle_submit(self):
        menu = self.menu_entry.get()

        if menu == '1':
            self.result_label.config(text="\nPenjumlahan")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.input1.grid(row=4, column=0, sticky="w")
            self.angka1_entry.grid(row=4, column=1, sticky="w")

            self.input2.grid(row=5, column=0, sticky="w")
            self.angka2_entry.grid(row=5, column=1, sticky="w")

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_penjumlahan(self.angka1_entry.get(), self.angka2_entry.get()))
            self.submit_operation.grid(row=6, column=0, sticky="w")
        elif menu == '2':
            self.result_label.config(text="\nPengurangan")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.input1.grid(row=4, column=0, sticky="w")
            self.angka1_entry.grid(row=4, column=1, sticky="w")

            self.input2.grid(row=5, column=0, sticky="w")
            self.angka2_entry.grid(row=5, column=1, sticky="w")

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_pengurangan(self.angka1_entry.get(), self.angka2_entry.get()))
            self.submit_operation.grid(row=6, column=0, sticky="w")
        elif menu == '3':
            self.result_label.config(text="\nPerkalian")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.input1.grid(row=4, column=0, sticky="w")
            self.angka1_entry.grid(row=4, column=1, sticky="w")

            self.input2.grid(row=5, column=0, sticky="w")
            self.angka2_entry.grid(row=5, column=1, sticky="w")

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_perkalian(self.angka1_entry.get(), self.angka2_entry.get()))
            self.submit_operation.grid(row=6, column=0, sticky="w")
        elif menu == '4':
            self.result_label.config(text="\nPembagian")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.input1.grid(row=4, column=0, sticky="w")
            self.angka1_entry.grid(row=4, column=1, sticky="w")

            self.input2.grid(row=5, column=0, sticky="w")
            self.angka2_entry.grid(row=5, column=1, sticky="w")

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_pembagian(self.angka1_entry.get(), self.angka2_entry.get()))
            self.submit_operation.grid(row=6, column=0, sticky="w")
        elif menu == '5':
            self.result_label.config(text="\nFaktorial")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.input1.grid(row=4, column=0, sticky="w")
            self.angka1_entry.grid(row=4, column=1, sticky="w")

            self.input2.grid_forget()  # Menghilangkan input2 dari tampilan
            self.angka2_entry.grid_forget()  # Menghilangkan angka2_entry dari tampilan

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_faktorial(self.angka1_entry.get()))
            self.submit_operation.grid(row=6, column=0, sticky="w")
        elif menu == '6':
            self.result_label.config(text="\nPangkat")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.input1.grid(row=4, column=0, sticky="w")
            self.angka1_entry.grid(row=4, column=1, sticky="w")

            self.input2.grid(row=5, column=0, sticky="w")
            self.angka2_entry.grid(row=5, column=1, sticky="w")

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_pangkat(self.angka1_entry.get(), self.angka2_entry.get()))
            self.submit_operation.grid(row=6, column=0, sticky="w")
        elif menu == '7':
            self.result_label.config(text="\nLogaritma Biner")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.input1.grid(row=4, column=0, sticky="w")
            self.angka1_entry.grid(row=4, column=1, sticky="w")

            self.input2.grid_forget()  # Menghilangkan input2 dari tampilan
            self.angka2_entry.grid_forget()  # Menghilangkan angka2_entry dari tampilan

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_logaritma(self.angka1_entry.get()))
            self.submit_operation.grid(row=6, column=0, sticky="w")
        elif menu == '8':
            self.result_label.config(text="\nAkar Kuadrat")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.input1.grid(row=4, column=0, sticky="w")
            self.angka1_entry.grid(row=4, column=1, sticky="w")

            self.input2.grid_forget()  # Menghilangkan input2 dari tampilan
            self.angka2_entry.grid_forget()  # Menghilangkan angka2_entry dari tampilan

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_akarkuadrat(self.angka1_entry.get()))
            self.submit_operation.grid(row=6, column=0, sticky="w")
        else:
            self.result_label.config(text="Nomor pilihan tidak valid")
            self.result_label.pack(anchor='w')
        

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
        self.result_accept.config(text=f"Accepted : {tm.accepted_input()}")
        self.result_accept.grid(row=7, column=0, sticky="w")

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
        self.result_calculation.config(text=f"{angka1} + {angka2} = {sign + str(n)}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

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
        self.result_accept.config(text=f"Accepted : {tm.accepted_input()}")
        self.result_accept.grid(row=7, column=0, sticky="w")

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
        self.result_calculation.config(text=f"{angka1} - {angka2} = {sign + str(n)}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

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
        self.result_accept.config(text=f"Accepted : {tm.accepted_input()}")
        self.result_accept.grid(row=7, column=0, sticky="w")

        print('Hasil =', perkalian)
        self.result_calculation.config(text=f"{angka1} x {angka2} = {perkalian}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

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
        self.result_accept.config(text=f"Accepted : {tm.accepted_input()}")
        self.result_accept.grid(row=7, column=0, sticky="w")

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
        self.result_calculation.config(text=f"{angka1} / {angka2} = {sign + str(n)}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

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
        self.result_accept.config(text=f"Accepted : {tm.accepted_input()}")
        self.result_accept.grid(row=7, column=0, sticky="w")

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
        self.result_calculation.config(text=f"{angka1}! = {faktorial}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

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
        self.result_accept.config(text=f"Accepted : {tm.accepted_input()}")
        self.result_accept.grid(row=7, column=0, sticky="w")

        n = 0
        for i in tm.tape.values():
            if i == '0':
                n += 1
            elif i == '-0':
                n -= 1
        print('Hasil = ', n)
        self.result_calculation.config(text=f"{angka2} ^ {angka1} = {n}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

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
        self.result_accept.config(text=f"Accepted : {tm.accepted_input()}")
        self.result_accept.grid(row=7, column=0, sticky="w")

        sumOfZero = 0

        for x in tm.tape.values():
            if x == '0':
                sumOfZero += 1

        result = sumOfZero
        print(f'2 Log {angka1} = {result}')
        self.result_calculation.config(text=f"2 Log {angka1} = {result}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

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
        self.result_accept.config(text=f"Accepted : {tm.accepted_input()}")
        self.result_accept.grid(row=7, column=0, sticky="w")

        sumOfZero = 0

        for x in tm.tape.values():
            if x == '0':
                sumOfZero += 1

        result = sumOfZero
        print(f'Hasil = {result}')
        self.result_calculation.config(text=f"sqrt({angka1}) = {result}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

    def restart_program(self):
        self.window.destroy()
        TuringMachineSimulator()
    
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    simulator = TuringMachineSimulator()
    simulator.run()