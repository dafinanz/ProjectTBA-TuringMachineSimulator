import time
from tkinter import *
from tkinter import ttk
from turingMachine import TuringMachine
from collections import defaultdict
from Perkalian import perkalian_m


class TuringMachineSimulator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Turing Machine Simulator")

        self.label = Label(self.window, text="1. Tambah\n2. Kurang\n3. Kali\n4. Bagi\n5. Faktorial\n6. Pangkat\n7. Logaritma Biner\n8. Akar Kuadrat")
        self.label.pack(anchor='w')

        self.menu_entry = Entry(self.window)
        self.menu_entry.pack(anchor='w')

        self.button_frame = Frame(self.window)
        self.button_frame.pack(anchor='w', pady=(0, 0))

        self.submit_button = Button(self.button_frame, text="Submit", command=self.handle_submit)
        self.submit_button.pack(side='left')

        self.restart_button = Button(self.button_frame, text="Restart", command=self.restart_program)
        self.restart_button.pack(side='left', padx=(10, 0))

        self.result_label = Label(self.window, text="")
        self.result_label.pack(anchor='w')

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
        tm.perkalian()
        tm.initialize(tape)

        step_transitions = []

        while not tm.halted:
            current_state = dict(tm.tape)
            current_head = tm.head
            tm.step()

            next_state = dict(tm.tape)
            next_head = tm.head

            # Append the step transition to the list
            step_transitions.append((current_state, current_head, next_state, next_head))

        result = ''.join([tm.tape[i] for i in range(tm.head + 1, index)]).strip('0')

        sumOfZero = 0
        sign = 1
        for x in tm.tape.values():
            if x == '0':
                sumOfZero += 1
            elif x == '-':
                sign *= -1
        sumOfZero *= sign
        tm.perkalian = sumOfZero

        # Update the result label with the final result
        self.result_label.configure(text=f"Result: {result}")

        for i, (current_state, current_head, next_state, next_head) in enumerate(step_transitions):
            # Call the drawInline method to visualize the tape at each step
            self.drawInline(index, self.canvas_output.winfo_x(), self.canvas_output.winfo_x() + self.canvas_output.winfo_width(),
                            self.canvas_output.winfo_y(), self.canvas_output.winfo_y() + self.canvas_output.winfo_height(),
                            i, current_state, current_head)

            # Add a small delay to slow down the visualization (optional)
            # You can adjust the value of the delay in seconds (e.g., time.sleep(0.5) for a half-second delay)
            
        
        self.drawInline(index, self.canvas_output.winfo_x(), self.canvas_output.winfo_x() + self.canvas_output.winfo_width(),
                        self.canvas_output.winfo_y(), self.canvas_output.winfo_y() + self.canvas_output.winfo_height(),
                        len(step_transitions), next_state, next_head)

    def drawInline(self, index, x1, x2, y1, y2, counter, tape, head):
        self.canvas.create_rectangle(x1, y1 + counter * 40, x2, y2 + counter * 40, outline='black')

        for i in range(head - 10, head + 11):
            if i == head:
                self.canvas.create_rectangle(x1 + (i - head + 10) * 30, y1 + counter * 40, x1 + (i - head + 11) * 30, y2 + counter * 40, fill='lightgreen')
                self.canvas.create_text(x1 + (i - head + 10) * 30 + 15, y1 + counter * 40 + (y2 - y1) / 2, text=tape.get(i, ""))
            else:
                self.canvas.create_rectangle(x1 + (i - head + 10) * 30, y1 + counter * 40, x1 + (i - head + 11) * 30, y2 + counter * 40)
                self.canvas.create_text(x1 + (i - head + 10) * 30 + 15, y1 + counter * 40 + (y2 - y1) / 2, text=tape.get(i, ""))


    def restart_program(self):
        self.window.destroy()
        TuringMachineSimulator()


if __name__ == "__main__":
    TuringMachineSimulator()
