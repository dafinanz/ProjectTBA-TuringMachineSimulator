from tkinter import *

root = Tk()

w = Label(root, text='Turing Machine Simulator')
w.pack()

pilihan_text = "Pilihan:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Faktorial\n6. Pangkat\n7. Logaritma Biner\n8. Akar kuadrat"
pilihan_label = Label(root, text=pilihan_text, justify="left")
pilihan_label.pack(anchor='w')

def get_input():
    input_number = entry.get()
    if input_number == '1':
        output_label.config(text="Penjumlahan")
    elif input_number == '2':
        output_label.config(text="Pengurangan")
    elif input_number == '3':
        output_label.config(text="Perkalian")
    elif input_number == '4':
        output_label.config(text="Pembagian")
    elif input_number == '5':
        output_label.config(text="Faktorial")
    elif input_number == '6':
        output_label.config(text="Pangkat")
    elif input_number == '7':
        output_label.config(text="Logaritma Biner")
    elif input_number == '8':
        output_label.config(text="Akar kuadrat")
    else:
        output_label.config(text="Nomor pilihan tidak valid")

input_frame = Frame(root)
input_frame.pack(anchor='w')

entry = Entry(input_frame)
entry.pack(side="left")

button = Button(input_frame, text="Input", command=get_input)
button.pack(side="left")

output_label = Label(root, text="", justify="left")
output_label.pack(anchor='w')

root.mainloop()