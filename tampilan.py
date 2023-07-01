from tkinter import *

root = Tk()

w = Label(root, text='Turing Machine Simulator')
w.pack()

# T = Text(root, height=2, width=100)
# T.pack()
# T.insert(END, 'GeeksforGeeks\nBEST WEBSITE\n')

text = Text(root)
text.insert(END, "Pilihan:\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian\n5. Faktorial\n6. Pangkat\n7. Logaritma Biner\n8. Akar kuadrat")
text.pack()

mainloop( )