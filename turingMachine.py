import time
from collections import defaultdict
from dataclasses import dataclass, field
from typing import DefaultDict, Dict, List, Set, Tuple
# from pydantic import BaseModel
from typing import List, Optional
from Penjumlahan import penjumlahan_m
from Pengurangan import pengurangan_m
from Perkalian import perkalian_m
from Pembagian import division
from Faktorial import faktorialMode
from AkarKuadrat import squareroot
from LogaritmaBiner import logaritmaMode
from Pangkat import powerMode
# end

# 1
@dataclass
class TuringMachine:

    penjumlahan = penjumlahan_m
    substraction = pengurangan_m
    multiplicationMode = perkalian_m
    division = division
    faktorialMode = faktorialMode
    squareroot = squareroot
    logaritmaMode = logaritmaMode
    powerMode = powerMode

    states: Set[str] = field(init=False)
    symbols: Set[str] = field(init=False)
    blank_symbol: str = field(init=False)
    input_symbols: Set[str] = field(init=False)
    initial_state: str = field(init=False)
    accepting_states: Set[str] = field(init=False)
    transitions: Dict[Tuple[str, str],
                      Tuple[str, str, int]] = field(init=False)
    # state, symbol -> new state, new symbol, direction

    head: int = field(init=False)
    tape: DefaultDict[int, str] = field(init=False)
    current_state: str = field(init=False)
    halted: bool = field(init=False, default=True)

    tape_string: List[Tuple[str, str]] = field(init=False)

    # end

    # 2)
    def initialize(self, input_symbols: 'dict[int, str]'):
        self.head = 0
        self.halted = False
        self.current_state = self.initial_state
        self.tape = defaultdict(lambda: self.blank_symbol, input_symbols)
        self.tape_string = []

    # 3) sama n0.3 yg diatas
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

    # end

    # 4)
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

    # end

# Create an instance of TuringMachine
tm = TuringMachine()

tm.penjumlahan()
tm.substraction()
tm.multiplicationMode()
tm.division()
tm.faktorialMode()
tm.squareroot()
tm.logaritmaMode()
tm.powerMode()