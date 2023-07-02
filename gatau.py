from tkinter import *
from tkinter import ttk
from turingMachine import TuringMachine
from collections import defaultdict

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

        self.input1 = Label(self.field_frame, text="Angka 1")
        self.angka1_entry = Entry(self.field_frame)

        self.input2 = Label(self.field_frame, text="Angka 2")
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
        self.canvas_frame = Canvas(self.window, width=800, height=400)
        self.canvas_frame.grid(row=9, column=0, sticky='nsew')

        self.canvas_obj = Canvas(self.canvas_frame)
        self.canvas_obj.grid(row=9, column=0, sticky='nsew')

        self.scrollbar = Scrollbar(self.canvas_frame, orient='vertical', command=self.canvas_obj.yview)
        self.scrollbar.grid(row=9, column=0, sticky='ns')

        self.canvas_obj.configure(yscrollcommand=self.scrollbar.set)

        self.frame_output = ttk.LabelFrame(self.window, text="Output", width=600)
        self.frame_output.grid(row=9, column=0, sticky='nsew')

        self.canvas_output = Canvas(self.frame_output, width=600, height=300)
        self.canvas_output.grid(row=9, column=0, sticky='nsew')

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

        result = ''.join([tm.tape[i] for i in range(tm.head + 1, index)]).strip('0')
        self.result_label.configure(text=f"Result: {result}")

        self.drawInline(index, self.canvas_output.winfo_x(), self.canvas_output.winfo_x() + self.canvas_output.winfo_width(),
                        self.canvas_output.winfo_y(), self.canvas_output.winfo_y() + self.canvas_output.winfo_height(), 0, tm.tape, tm.head)

    def drawInline(self, index, x1, x2, y1, y2, counter, tape, head):
        self.canvas_obj.create_rectangle(x1, y1 + counter * 40, x2, y2 + counter * 40, outline='black')

        for i in range(head - 10, head + 11):
            if i == head:
                self.canvas_obj.create_rectangle(x1 + (i - head + 10) * 30, y1 + counter * 40, x1 + (i - head + 11) * 30, y2 + counter * 40, fill='lightgreen')
                self.canvas_obj.create_text(x1 + (i - head + 10) * 30 + 15, y1 + counter * 40 + (y2 - y1) / 2, text=tape[i])
            else:
                self.canvas_obj.create_rectangle(x1 + (i - head + 10) * 30, y1 + counter * 40, x1 + (i - head + 11) * 30, y2 + counter * 40)
                self.canvas_obj.create_text(x1 + (i - head + 10) * 30 + 15, y1 + counter * 40 + (y2 - y1) / 2, text=tape[i])


    def restart_program(self):
        self.window.destroy()
        TuringMachineSimulator()
    
    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    simulator = TuringMachineSimulator()
    simulator.run()