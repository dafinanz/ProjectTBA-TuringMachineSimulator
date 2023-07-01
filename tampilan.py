from tkinter import *

root = Tk()

w = Label(root, text='Turing Machine Simulator')
w.pack()

# text = Text(root)
# text.insert(END, "Pilihan:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Faktorial\n6. Pangkat\n7. Logaritma Biner\n8. Akar kuadrat")
# text.pack()

pilihan_text = "Pilihan:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Faktorial\n6. Pangkat\n7. Logaritma Biner\n8. Akar kuadrat"
pilihan_label = Label(root, text=pilihan_text, justify="left")
pilihan_label.pack(anchor='w')

root.mainloop()