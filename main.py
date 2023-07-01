from turingMachine import TuringMachine
from Penjumlahan import additionMode
from Pengurangan import substraction
from Perkalian import multiplicationMode
from Pembagian import division
from Faktorial import faktorialMode
from AkarKuadrat import squareroot
from LogaritmaBiner import logaritmaMode
from Pangkat import powerMode

if __name__ == '__main__':
    print('Turing Machine Simulator\n\n1. Tambah\n2. Kurang\n3. Kali\n4. Bagi\n5. Faktorial\n6. Pangkat\n7. Logaritma Biner\n8. Akar Kuadrat\n')
    menu = input('pilihan : ')

    if menu == '1':
        print('\n\nPertambahan')
        tm = TuringMachine()
        angka1 = int(input('\nangka 1 : '))
        angka2 = int(input('angka 2 : '))
        tape = {0: 'b'}
        index = 1

        if angka1 < 0:
            angka1 = angka1 * -1
            for i in range(angka1):
                tape[index] = '-0'
                index += 1
        else:
            for i in range(angka1):
                tape[index] = '0'
                index += 1

        tape[index] = '1'
        index += 1

        if angka2 < 0:
            angka2 = angka2 * -1
            for i in range(angka2):
                tape[index] = '-0'
                index += 1
        else:
            for i in range(angka2):
                tape[index] = '0'
                index += 1

        tm.additionMode()
        tm.initialize(tape)

        while not tm.halted:
            tm.print()
            tm.step()

        print('Accepted : ', tm.accepted_input())

        n = 0
        for i in tm.tape.values():
            if i == '0':
                n += 1
            elif i == '-0':
                n -= 1
        print('Hasil = ', n)

    elif menu == '2':
        print('\n\nPengurangan')
        tm = TuringMachine()
        angka1 = int(input('\nangka 1 : '))
        angka2 = int(input('angka 2 : '))
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
            for i in range(angka2):
                tape[index] = '0'
                index += 1

        tm.substraction()
        tm.initialize(tape)

        while not tm.halted:
            tm.print()
            tm.step()

        print('Accepted : ', tm.accepted_input())

    elif menu == '3':
        print('\n\nPerkalian')
        tm = TuringMachine()
        angka1 = input('angka 1 : ')
        angka2 = input('angka 2 : ')
        index = 0
        tape = {}
        if angka1[0] == '-':
            tape[index] = '-'
            index += 1
            angka1 = angka1[1 : : ]
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
            angka2 = angka2[1 : : ]
        else:
            tape[index] = '+'
            index += 1

        angka2 = int(angka2)
        for i in range(angka2):
            tape[index] = '0'
            index += 1

        tm.multiplicationMode()
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
        perkalian = sumOfZero
        print(f'Hasil: {perkalian}')

    elif menu == '4':
        print('\n\nPembagian')
        tm = TuringMachine()
        angka1 = int(input('\nangka 1 : '))
        angka2 = int(input('angka 2 : '))
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

        tm.division()
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

    elif menu == '5':
        print('\n\nFaktorial')
        tm = TuringMachine()
        angka1 = int(input('\ninput : '))
        tape = {0: 'B'}
        index = 0

        tape[index] = '1'
        index += 1

        for i in range(angka1):
            tape[index] = '0'
            index += 1
        
        tape[index] = '1'
        index += 1


        tm.faktorialMode()
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

    elif menu == '6':
        print('\n\nPangkat')
        tm = TuringMachine()
        angka2 = int(input('angka : '))
        angka1 = int(input('\npangkat : '))
        tape = {0: 'b'}
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

        tm.powerMode()
        tm.initialize(tape)

        while not tm.halted:
            tm.print()
            tm.step()

        print('Accepted : ', tm.accepted_input())

        n = 0
        for i in tm.tape.values():
            if i == '0':
                n += 1
            elif i == '-0':
                n -= 1
        print('Hasil = ', n)

    elif menu == '7':
        print('\n\nLogaritma Biner')
        tm = TuringMachine()
        angka1 = int(input('\n2 log : '))
        tape = {0: 'b'}
        index = 0
        for i in range(angka1):
            tape[index] = '0'
            index += 1


        tm.logaritmaMode()
        tm.initialize(tape)

        while not tm.halted:
            tm.print()
            tm.step()

        print('Accepted : ', tm.accepted_input())

        sumOfZero = 0

        for x in tm.tape.values():
            if x == '0':
                sumOfZero += 1

        result = sumOfZero
        print(f'2 Log {angka1} = {result}')

    elif menu == '8':
        print('\n\nAkar Kuadrat')
        tm = TuringMachine()
        angka1 = int(input('\nAkar Kuadrat : '))
        tape = {0: 'b'}
        index = 0
        for i in range(angka1):
            tape[index] = '0'
            index += 1

            tape[index] = '1'
            index == 1

        tm.squareroot()
        tm.initialize(tape)

        while not tm.halted:
            tm.print()
            tm.step()

        print('Accepted : ', tm.accepted_input())

        sumOfZero = 0

        for x in tm.tape.values():
            if x == '0':
                sumOfZero += 1

        result = sumOfZero
        print(f'Hasil = {result}')