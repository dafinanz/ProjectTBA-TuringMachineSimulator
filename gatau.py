from tkinter import *
from tkinter import ttk
from turingMachine import TuringMachine

class TuringMachineSimulator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Turing Machine Simulator")
        self.window.geometry("600x600")

        self.create_header()

        self.label = Label(self.window, text="Pilihan:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Faktorial\n6. Pangkat\n7. Logaritma Biner\n8. Akar Kuadrat\n", justify="left")
        self.label.grid(row=1, column=0, sticky="w")

        self.field()

        self.canvas()

        self.window.mainloop()

    def field(self):
        self.field_frame = Frame(self.window, width=400, height=400)
        self.field_frame.grid(row=2, column=0, sticky='nsew')

        self.label = Label(self.field_frame, text="Pilihan:", justify="left")
        self.label.grid(row=2, column=0, sticky="w")

        self.menu_entry = Entry(self.field_frame)
        self.menu_entry.grid(row=2, column=1, sticky="w")

        self.submit_button = Button(self.field_frame, text="Submit", command=self.handle_submit)
        self.submit_button.grid(row=2, column=2, sticky="w")

        self.result_label = Label(self.field_frame, text="")

        self.angka1_entry = Entry(self.field_frame)

        self.sign = Label(self.field_frame, text="")

        self.angka2_entry = Entry(self.field_frame)

        self.submit_operation = Button(self.field_frame, text="")
        self.result_accept = Label(self.field_frame, text="")
        self.result_calculation = Label(self.field_frame, text="")

    def create_header(self):
        # Create a frame widget for the header background
        header_frame = Frame(self.window, bg="#3c8aae")
        header_frame.grid(row=0, column=0, sticky="ew")

        # Create a label widget for the header title inside the frame
        header_label = Label(header_frame, text="Turing Machine Simulator", font=("Roboto", 20, "bold"), fg="white", bg="#3c8aae", pady=10)
        header_label.grid(sticky="nsew", padx=110)

    def canvas(self):
        self.canvas_frame = Canvas(self.window)
        self.canvas_frame.grid(row=9, column=0, sticky='nsew')

        self.canvas = Canvas(self.canvas_frame, width=600, height=200)
        self.canvas.grid(row=9, column=0, sticky='nsew')

        self.scrollbar = Scrollbar(self.canvas_frame, orient='horizontal', command=self.canvas.yview)
        self.scrollbar.grid(row=9, column=0, sticky='ew')

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame_output = ttk.LabelFrame(self.window, text="Output", width=600)
        self.frame_output.grid(row=9, column=0, sticky='nsew')

        self.canvas_output = Canvas(self.frame_output, width=600, height=300)
        self.canvas_output.grid(row=9, column=0, sticky='nsew')

        # Assign self.canvas_output to self.canvas
        self.canvas = self.canvas_output


    def handle_submit(self):
        menu = self.menu_entry.get()

        if menu == '1':
            self.result_label.config(text="\nPenjumlahan")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.angka1_entry.grid(row=4, column=0, sticky="w")

            self.sign.config(text="+")
            self.sign.grid(row=4, column=1, sticky="nsew")

            self.angka2_entry.grid(row=4, column=2, sticky="w")

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_penjumlahan(self.angka1_entry.get(), self.angka2_entry.get()))
            self.submit_operation.grid(row=6, column=1, sticky="nsew", pady=10)
        elif menu == '2':
            self.result_label.config(text="\nPengurangan")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.angka1_entry.grid(row=4, column=0, sticky="w")

            self.sign.config(text="-")
            self.sign.grid(row=4, column=1, sticky="nsew")

            self.angka2_entry.grid(row=4, column=2, sticky="w")

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_pengurangan(self.angka1_entry.get(), self.angka2_entry.get()))
            self.submit_operation.grid(row=6, column=1, sticky="nsew", pady=10)
        elif menu == '3':
            self.result_label.config(text="\nPerkalian")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.angka1_entry.grid(row=4, column=0, sticky="w")

            self.sign.config(text="x")
            self.sign.grid(row=4, column=1, sticky="nsew")

            self.angka2_entry.grid(row=4, column=2, sticky="w")

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_perkalian(self.angka1_entry.get(), self.angka2_entry.get()))
            self.submit_operation.grid(row=6, column=1, sticky="nsew", pady=10)
        elif menu == '4':
            self.result_label.config(text="\nPembagian")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.angka1_entry.grid(row=4, column=0, sticky="w")

            self.sign.config(text="/")
            self.sign.grid(row=4, column=1, sticky="nsew")

            self.angka2_entry.grid(row=4, column=2, sticky="w")

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_pembagian(self.angka1_entry.get(), self.angka2_entry.get()))
            self.submit_operation.grid(row=6, column=1, sticky="nsew", pady=10)
        elif menu == '5':
            self.result_label.config(text="\nFaktorial")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.angka1_entry.grid(row=4, column=0, sticky="w")

            self.sign.config(text="!")
            self.sign.grid(row=4, column=1, sticky="nsew")

            self.angka2_entry.grid_forget()  # Menghilangkan angka2_entry dari tampilan

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_faktorial(self.angka1_entry.get()))
            self.submit_operation.grid(row=6, column=1, sticky="nsew", pady=10)
        elif menu == '6':
            self.result_label.config(text="\nPangkat")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.angka1_entry.grid(row=4, column=0, sticky="w")

            self.sign.config(text="^")
            self.sign.grid(row=4, column=1, sticky="nsew")

            self.angka2_entry.grid(row=4, column=2, sticky="w")

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry
            self.angka2_entry.delete(0, END)  # Mengosongkan nilai angka2_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_pangkat(self.angka2_entry.get(), self.angka1_entry.get()))
            self.submit_operation.grid(row=6, column=1, sticky="nsew", pady=10)
        elif menu == '7':
            self.result_label.config(text="\nLogaritma Biner")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.sign.config(text="2 log")
            self.sign.grid(row=4, column=0, sticky="nsew")

            self.angka1_entry.grid(row=4, column=1, sticky="w")

            self.angka2_entry.grid_forget()  # Menghilangkan angka2_entry dari tampilan

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_logaritma(self.angka1_entry.get()))
            self.submit_operation.grid(row=6, column=1, sticky="nsew", pady=10)
        elif menu == '8':
            self.result_label.config(text="\nAkar Kuadrat")
            self.result_label.grid(row=3, column=0, sticky="w")

            self.sign.config(text="sqrt")
            self.sign.grid(row=4, column=0, sticky="nsew")

            self.angka1_entry.grid(row=4, column=1, sticky="w")

            self.angka2_entry.grid_forget()  # Menghilangkan angka2_entry dari tampilan

            self.angka1_entry.delete(0, END)  # Mengosongkan nilai angka1_entry

            self.submit_operation.config(text="Go", command=lambda: self.calculate_akarkuadrat(self.angka1_entry.get()))
            self.submit_operation.grid(row=6, column=1, sticky="nsew", pady=10)
        else:
            self.result_label.config(text="Nomor pilihan tidak valid")
            self.result_label.pack(anchor='w')
        

    def calculate_penjumlahan(self, angka1, angka2):

        self.clearCanvas()

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
        self.result_calculation.config(text=f"Hasil = {sign + str(n)}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

        self.drawInline(index, self.canvas_output.winfo_x(), self.canvas_output.winfo_x() + self.canvas_output.winfo_width(),
                        self.canvas_output.winfo_y(), self.canvas_output.winfo_y() + self.canvas_output.winfo_height(), 0, tm.tape, tm.head)

    def calculate_pengurangan(self, angka1, angka2):

        self.clearCanvas()

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
        self.result_calculation.config(text=f"Hasil = {sign + str(n)}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

        self.drawInline(index, self.canvas_output.winfo_x(), self.canvas_output.winfo_x() + self.canvas_output.winfo_width(),
                        self.canvas_output.winfo_y(), self.canvas_output.winfo_y() + self.canvas_output.winfo_height(), 0, tm.tape, tm.head)

    def calculate_perkalian(self, angka1, angka2):

        self.clearCanvas()

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
        self.result_calculation.config(text=f"Hasil = {perkalian}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

        self.drawInline(index, self.canvas_output.winfo_x(), self.canvas_output.winfo_x() + self.canvas_output.winfo_width(),
                        self.canvas_output.winfo_y(), self.canvas_output.winfo_y() + self.canvas_output.winfo_height(), 0, tm.tape, tm.head)

    def calculate_pembagian(self, angka1, angka2):

        self.clearCanvas()

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
        self.result_calculation.config(text=f"Hasil = {sign + str(n)}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

        self.drawInline(index, self.canvas_output.winfo_x(), self.canvas_output.winfo_x() + self.canvas_output.winfo_width(),
                        self.canvas_output.winfo_y(), self.canvas_output.winfo_y() + self.canvas_output.winfo_height(), 0, tm.tape, tm.head)

    def calculate_faktorial(self, angka1):

        self.clearCanvas()

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
        self.result_calculation.config(text=f"Hasil = {faktorial}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

        self.drawInline(index, self.canvas_output.winfo_x(), self.canvas_output.winfo_x() + self.canvas_output.winfo_width(),
                        self.canvas_output.winfo_y(), self.canvas_output.winfo_y() + self.canvas_output.winfo_height(), 0, tm.tape, tm.head)

    def calculate_pangkat(self, angka2, angka1):

        self.clearCanvas()

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
        self.result_calculation.config(text=f"Hasil = {n}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

        self.drawInline(index, self.canvas_output.winfo_x(), self.canvas_output.winfo_x() + self.canvas_output.winfo_width(),
                        self.canvas_output.winfo_y(), self.canvas_output.winfo_y() + self.canvas_output.winfo_height(), 0, tm.tape, tm.head)

    def calculate_logaritma(self, angka1):

        self.clearCanvas()

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
        self.result_calculation.config(text=f"Hasil = {result}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

        self.drawInline(index, self.canvas_output.winfo_x(), self.canvas_output.winfo_x() + self.canvas_output.winfo_width(),
                        self.canvas_output.winfo_y(), self.canvas_output.winfo_y() + self.canvas_output.winfo_height(), 0, tm.tape, tm.head)

    def calculate_akarkuadrat(self, angka1):

        self.clearCanvas()

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
        self.result_calculation.config(text=f"Hasil = {result}")
        self.result_calculation.grid(row=8, column=0, sticky="w")

        self.drawInline(index, self.canvas_output.winfo_x(), self.canvas_output.winfo_x() + self.canvas_output.winfo_width(),
                        self.canvas_output.winfo_y(), self.canvas_output.winfo_y() + self.canvas_output.winfo_height(), 0, tm.tape, tm.head)

    def drawInline(self, index, x1, x2, y1, y2, counter, tape, head):
        x1 = 50  
        y1 = 50 
        x2 = 200 
        y2 = 100 
        self.canvas.create_rectangle(x1, y1 + counter * 40, x2, y2 + counter * 40, outline='black')

        for i in range(head - 20, head + 21):
            if i == head:
                self.canvas.create_rectangle(x1 + (i - head + 10) * 30, y1 + counter * 40, x1 + (i - head + 11) * 30, y2 + counter * 40, fill='lightgreen')
                self.canvas.create_text(x1 + (i - head + 10) * 30 + 15, y1 + counter * 40 + (y2 - y1) / 2, text=tape[i])
            else:
                self.canvas.create_rectangle(x1 + (i - head + 10) * 30, y1 + counter * 40, x1 + (i - head + 11) * 30, y2 + counter * 40)
                self.canvas.create_text(x1 + (i - head + 10) * 30 + 15, y1 + counter * 40 + (y2 - y1) / 2, text=tape[i])

    def clearCanvas(self):
        self.canvas.delete("all")

    def restart_program(self):
        self.window.destroy()
        TuringMachineSimulator()
    
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    simulator = TuringMachineSimulator()
    simulator.run()