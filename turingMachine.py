import time
from collections import defaultdict
from dataclasses import dataclass, field
from typing import DefaultDict, Dict, List, Set, Tuple
from typing import List, Optional
from Penjumlahan import penjumlahan_m
from Pengurangan import pengurangan_m
from Perkalian import perkalian_m
from Pembagian import pembagian_m
from Faktorial import faktorial_m
from Pangkat import pangkat_m
from AkarKuadrat import akarkuadrat_m
from LogaritmaBiner import logaritma_m

@dataclass
class TuringMachine:

    penjumlahan = penjumlahan_m
    pengurangan = pengurangan_m
    perkalian = perkalian_m
    pembagian = pembagian_m
    faktorial = faktorial_m
    pangkat = pangkat_m
    akarkuadrat = akarkuadrat_m
    logaritma = logaritma_m

    states: Set[str] = field(init=False)
    symbols: Set[str] = field(init=False)
    blank_symbol: str = field(init=False)
    input_symbols: Set[str] = field(init=False)
    initial_state: str = field(init=False)
    accepting_states: Set[str] = field(init=False)
    transitions: Dict[Tuple[str, str],
                      Tuple[str, str, int]] = field(init=False)

    head: int = field(init=False)
    tape: DefaultDict[int, str] = field(init=False)
    current_state: str = field(init=False)
    halted: bool = field(init=False, default=True)

    tape_string: List[Tuple[str, str]] = field(init=False)

    def initialize(self, input_symbols: 'dict[int, str]'):
        self.head = 0
        self.halted = False
        self.current_state = self.initial_state
        self.tape = defaultdict(lambda: self.blank_symbol, input_symbols)
        self.tape_string = []

    def step(self):
        if self.halted:
            raise RuntimeError('Cannot step halted machine')

        try:
            state, symbol, direction = self.transitions[(self.current_state,
                                                         self.tape[self.head])]
        except KeyError:
            self.halted = True
            return

        self.tape[self.head] = symbol
        self.current_state = state
        self.head += direction

    def accepted_input(self):
        if not self.halted:
            raise RuntimeError('Machine still running')
        return self.current_state in self.accepting_states

    def print(self, window=10):
        print('... ', end='')
        print(' '.join(self.tape[i] for i in range(
            self.head - window, self.head + window + 1)), end='')
        tape = ' '.join(self.tape[i] for i in range(
            self.head - window, self.head + window + 1))
        tape_state = (tape, self.current_state)
        self.tape_string.append(tape_state)

        print(f' ... state={self.current_state}')
        print(f'{" " * (2 * window + 4)}^')


# Membuat instance turingMachine
tm = TuringMachine()

tm.penjumlahan()
tm.pengurangan()
tm.perkalian()
tm.pembagian()
tm.faktorial()
tm.pangkat()
tm.akarkuadrat()
tm.logaritma()