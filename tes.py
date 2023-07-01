import time
from collections import defaultdict
from dataclasses import dataclass, field
from typing import DefaultDict, Dict, List, Set, Tuple
# from pydantic import BaseModel
from typing import List, Optional
# end

# 1
@dataclass
class TuringMachine:

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

    # def additionMode(self):
    #     self.states = {'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13'}
    #     self.symbols = {'-0', '-1', '0', '1', 'b'}
    #     self.blank_symbol = 'b'
    #     self.input_symbols = {'0', '1', '-0', '-1'}
    #     self.initial_state = 'q1'
    #     self.accepting_states = {'q13'}
    #     self.transitions = {
    #                         ('q1', '0'): ('q1', '0', 1),
    #                         ('q1', '1'): ('q2', '0', 1),
    #                         ('q1', 'b'): ('q1', 'b', 1),
    #                         ('q1', '-0'): ('q6', 'b', 1),

    #                         ('q2', '0'): ('q2', '0', 1),
    #                         ('q2', '-0'): ('q2', '-0', 1),
    #                         ('q2', 'b'): ('q3', 'b', -1),

    #                         ('q3', '-0'): ('q4', 'b', -1),
    #                         ('q3', '0'): ('q13', 'b', -1),

    #                         ('q4', '-0'): ('q4', '-0', -1),
    #                         ('q4', '0'): ('q4', '0', -1),
    #                         ('q4', 'b'): ('q5', 'b', 1),

    #                         ('q5', '0'): ('q2', 'b', 1),
    #                         ('q5', '-0'): ('q11', '-0', -1),

    #                         ('q11', 'b'): ('q12', '-0', 1),

    #                         ('q12', '-0'): ('q12', '-0', 1),
    #                         ('q12', 'b'): ('q13', '-0', 1),

    #                         ('q6', '-0'): ('q6', '-0', 1),
    #                         ('q6', '1'): ('q7', '1', 1),

    #                         ('q7', '0'): ('q7', '0', 1),
    #                         ('q7', 'b'): ('q8', 'b', -1),
    #                         ('q7', '-0'): ('q8', '-0', -1),

    #                         ('q8', '1'): ('q13', '-0', -1),
    #                         ('q8', '0'): ('q9', 'b', -1),
    #                         ('q8', '-0'): ('q9', 'b', -1),

    #                         ('q9', '0'): ('q9', '0', -1),
    #                         ('q9', '-0'): ('q9', '-0', -1),
    #                         ('q9', '1'): ('q10', '1', -1),

    #                         ('q10', '-0'): ('q10', '-0', -1),
    #                         ('q10', 'b'): ('q1', 'b', 1),
    #                         }

    # def substraction(self):
    #     self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
    #                     'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21',
    #                     'q22'}
    #     self.symbols = {'0', '1', '-', 'B'}
    #     self.blank_symbol = 'B'
    #     self.input_symbols = {'0', '1', '-'}
    #     self.initial_state = 'q0'
    #     self.accepting_states = {'q6'}
    #     self.transitions = {('q0', '0'): ('q0', '0', 1),
    #                         ('q0', '1'): ('q1', '1', 1),
    #                         ('q0', '-'): ('q12', '-', 1),

    #                         ('q1', '0'): ('q1', '0', 1),
    #                         ('q1', 'B'): ('q2', 'B', -1),
    #                         ('q1', '-'): ('q8', '0', -1),

    #                         ('q2', '0'): ('q3', 'B', -1),
    #                         ('q2', '1'): ('q6', 'B', -1),

    #                         ('q3', '0'): ('q3', '0', -1),
    #                         ('q3', '1'): ('q3', '1', -1),
    #                         ('q3', 'B'): ('q4', 'B', 1),

    #                         ('q4', '0'): ('q5', 'B', 1),
    #                         ('q4', '1'): ('q7', '0', -1),

    #                         ('q5', '0'): ('q5', '0', 1),
    #                         ('q5', '1'): ('q1', '1', 1),

    #                         ('q7', 'B'): ('q6', '-', -1),

    #                         ('q8', '1'): ('q9', '0', 1),

    #                         ('q9', '0'): ('q9', '0', 1),
    #                         ('q9', 'B'): ('q10', 'B', -1),

    #                         ('q10', '0'): ('q11', 'B', -1),

    #                         ('q11', '0'): ('q6', 'B', -1),

    #                         ('q12', '0'): ('q12', '0', 1),
    #                         ('q12', '1'): ('q13', '1', 1),

    #                         ('q13', '0'): ('q14', '0', -1),
    #                         ('q13', '-'): ('q15', '-', 1),

    #                         ('q14', '0'): ('q14', '0', 1),
    #                         ('q14', '1'): ('q14', '0', 1),
    #                         ('q14', 'B'): ('q11', 'B', -1),

    #                         ('q15', '0'): ('q15', '0', 1),
    #                         ('q15', 'B'): ('q16', 'B', -1),

    #                         ('q16', '0'): ('q17', 'B', -1),
    #                         ('q16', '-'): ('q20', 'B', -1),

    #                         ('q17', '0'): ('q17', '0', -1),
    #                         ('q17', '-'): ('q17', '-', -1),
    #                         ('q17', '1'): ('q18', '1', -1),

    #                         ('q18', 'B'): ('q18', 'B', -1),
    #                         ('q18', '-'): ('q21', 'B', 1),
    #                         ('q18', '0'): ('q19', 'B', 1),

    #                         ('q19', 'B'): ('q19', 'B', 1),
    #                         ('q19', '1'): ('q13', '1', 1),

    #                         ('q20', '1'): ('q6', 'B', -1),

    #                         ('q21', 'B'): ('q21', 'B', 1),
    #                         ('q21', '1'): ('q22', 'B', 1),

    #                         ('q22', '-'): ('q6', '0', 1),

    #                         }

    # def multiplicationMode(self):
    #     self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
    #                     'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19'}
    #     self.symbols = {'#', '+', '-', '0', '1', 'b', 'x'}
    #     self.blank_symbol = 'b'
    #     self.input_symbols = {'0', '1', '+', '-', 'x', '#'}
    #     self.initial_state = 'q0'
    #     self.accepting_states = {'q19'}
    #     self.transitions = {('q0', '-'): ('q0', '-', -1),
    #                         ('q0', '+'): ('q0', '+', -1),
    #                         ('q0', 'b'): ('q1', '#', 1),

    #                         ('q1', '+'): ('q1', '+', 1),
    #                         ('q1', '-'): ('q1', '-', 1),
    #                         ('q1', '0'): ('q1', '0', 1),
    #                         ('q1', '1'): ('q1', '1', 1),
    #                         ('q1', 'b'): ('q2', '#', -1),

    #                         ('q2', '0'): ('q2', '0', -1),
    #                         ('q2', '1'): ('q2', '1', -1),
    #                         ('q2', '+'): ('q2', '+', -1),
    #                         ('q2', '-'): ('q2', '-', -1),
    #                         ('q2', '#'): ('q3', '#', 1),

    #                         ('q3', '-'): ('q5', '-', 1),
    #                         ('q3', '+'): ('q4', '+', 1),

    #                         ('q4', '0'): ('q4', '0', 1),
    #                         ('q4', '1'): ('q4', '1', 1),
    #                         ('q4', '+'): ('q6', '+', 1),
    #                         ('q4', '-'): ('q7', '-', 1),

    #                         ('q5', '0'): ('q5', '0', 1),
    #                         ('q5', '1'): ('q5', '1', 1),
    #                         ('q5', '-'): ('q6', '-', 1),
    #                         ('q5', '+'): ('q7', '+', 1),

    #                         ('q6', '0'): ('q6', '0', 1),
    #                         ('q6', '#'): ('q6', '#', 1),
    #                         ('q6', 'b'): ('q8', '+', -1),

    #                         ('q7', '#'): ('q7', '#', 1),
    #                         ('q7', '0'): ('q7', '0', 1),
    #                         ('q7', 'b'): ('q8', '-', -1),

    #                         ('q8', '#'): ('q9', '#', -1),

    #                         ('q9', '0'): ('q9', '0', -1),
    #                         ('q9', '1'): ('q9', '1', -1),
    #                         ('q9', '+'): ('q9', '+', -1),
    #                         ('q9', '-'): ('q9', '-', -1),
    #                         ('q9', '#'): ('q10', '#', 1),

    #                         ('q10', '+'): ('q10', '+', 1),
    #                         ('q10', '-'): ('q10', '-', 1),
    #                         ('q10', '0'): ('q11', 'b', 1),
    #                         ('q10', '1'): ('q18', 'b', 1),

    #                         ('q11', '0'): ('q11', '0', 1),
    #                         ('q11', '1'): ('q12', '1', 1),

    #                         ('q12', '+'): ('q12', '+', 1),
    #                         ('q12', '-'): ('q12', '-', 1),
    #                         ('q12', '0'): ('q13', 'x', 1),
    #                         ('q12', '#'): ('q15', '#', -1),

    #                         ('q13', '+'): ('q13', '+', 1),
    #                         ('q13', '-'): ('q13', '-', 1),
    #                         ('q13', '0'): ('q13', '0', 1),
    #                         ('q13', '#'): ('q13', '#', 1),
    #                         ('q13', 'b'): ('q14', '0', -1),

    #                         ('q14', '+'): ('q14', '+', -1),
    #                         ('q14', '-'): ('q14', '-', -1),
    #                         ('q14', '0'): ('q14', '0', -1),
    #                         ('q14', '#'): ('q14', '#', -1),
    #                         ('q14', 'x'): ('q12', 'x', 1),

    #                         ('q15', '+'): ('q15', '+', -1),
    #                         ('q15', '-'): ('q15', '-', -1),
    #                         ('q15', '0'): ('q15', '0', -1),
    #                         ('q15', '1'): ('q15', '1', -1),
    #                         ('q15', '#'): ('q15', '#', -1),
    #                         ('q15', 'x'): ('q15', '0', -1),
    #                         ('q15', 'b'): ('q16', 'b', -1),

    #                         ('q16', '-'): ('q16', '-', -1),
    #                         ('q16', '+'): ('q16', '+', -1),
    #                         ('q16', '#'): ('q16', '#', -1),
    #                         ('q16', 'b'): ('q17', 'b', 1),

    #                         ('q17', '-'): ('q17', 'b', 1),
    #                         ('q17', '+'): ('q17', 'b', 1),
    #                         ('q17', '#'): ('q17', 'b', 1),
    #                         ('q17', '1'): ('q17', '1', -1),
    #                         ('q17', 'b'): ('q10', 'b', 1),

    #                         ('q18', '+'): ('q18', 'b', 1),
    #                         ('q18', '-'): ('q18', 'b', 1),
    #                         ('q18', '0'): ('q18', 'b', 1),
    #                         ('q18', '#'): ('q19', 'b', 1),
    #                         }

    # def division(self):
    #     self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
    #                     'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17'}
    #     self.symbols = {'0', '1', '-', '+', 'B', 'X', 'Y', 'Z'}
    #     self.blank_symbol = 'B'
    #     self.input_symbols = {'0', '1', '-', '+'}
    #     self.initial_state = 'q0'
    #     self.accepting_states = {'q17'}
    #     self.transitions = {
    #                         ('q0', 'B'): ('q0', 'B', 1),
    #                         ('q0', '+'): ('q1', 'B', 1),
    #                         ('q0', '-'): ('q4', 'B', 1),

    #                         ('q1', '0'): ('q1', '0', 1),
    #                         ('q1', '1'): ('q1', '1', 1),
    #                         ('q1', '+'): ('q2', 'Z', 1),
    #                         ('q1', '-'): ('q5', 'Z', 1),

    #                         ('q2', '0'): ('q2', '0', 1),
    #                         ('q2', '1'): ('q2', '1', 1),
    #                         ('q2', 'B'): ('q3', '+', -1),

    #                         ('q3', '0'): ('q3', '0', -1),
    #                         ('q3', '1'): ('q3', '1', -1),
    #                         ('q3', 'Z'): ('q3', 'Z', -1),
    #                         ('q3', 'B'): ('q6', 'B', 1),

    #                         ('q4', '0'): ('q4', '0', 1),
    #                         ('q4', '1'): ('q4', '1', 1),
    #                         ('q4', '+'): ('q5', 'Z', 1),
    #                         ('q4', '-'): ('q2', 'Z', 1),

    #                         ('q5', '0'): ('q5', '0', 1),
    #                         ('q5', '1'): ('q5', '1', 1),
    #                         ('q5', 'B'): ('q3', '-', -1),

    #                         ('q6', '0'): ('q7', 'B', 1),
    #                         ('q6', '1'): ('q16', 'B', 1),

    #                         ('q7', '0'): ('q7', '0', 1),
    #                         ('q7', '1'): ('q8', '1', 1),

    #                         ('q8', 'Z'): ('q8', 'Z', 1),
    #                         ('q8', 'X'): ('q8', 'X', 1),
    #                         ('q8', '0'): ('q8', '0', 1),
    #                         ('q8', '1'): ('q9', '1', -1),

    #                         ('q9', 'X'): ('q9', 'X', -1),
    #                         ('q9', '0'): ('q10', 'X', -1),
    #                         ('q9', 'Z'): ('q10', 'Z', -1),

    #                         ('q10', 'Z'): ('q10', 'Z', -1),
    #                         ('q10', '0'): ('q11', '0', -1),
    #                         ('q10', '1'): ('q13', '1', 1),

    #                         ('q11', '0'): ('q11', '0', -1),
    #                         ('q11', 'Y'): ('q11', 'Y', -1),
    #                         ('q11', 'Z'): ('q11', 'Z', -1),
    #                         ('q11', '1'): ('q12', '1', -1),

    #                         ('q12', '0'): ('q12', '0', -1),
    #                         ('q12', 'B'): ('q6', 'B', 1),

    #                         ('q13', 'Z'): ('q13', 'Z', 1),
    #                         ('q13', 'X'): ('q13', '0', 1),
    #                         ('q13', '1'): ('q14', '1', 1),

    #                         ('q14', 'Y'): ('q14', 'Y', 1),
    #                         ('q14', '-'): ('q14', '-', 1),
    #                         ('q14', '+'): ('q14', '+', 1),
    #                         ('q14', 'B'): ('q15', 'Y', -1),

    #                         ('q15', 'Y'): ('q15', 'Y', -1),
    #                         ('q15', '-'): ('q15', '-', -1),
    #                         ('q15', '+'): ('q15', '+', -1),
    #                         ('q15', '1'): ('q11', '1', -1),

    #                         ('q16', '-'): ('q16', '-', 1),
    #                         ('q16', '+'): ('q16', '+', 1),
    #                         ('q16', 'Y'): ('q16', '0', 1),
    #                         ('q16', '0'): ('q16', 'B', 1),
    #                         ('q16', 'X'): ('q16', 'B', 1),
    #                         ('q16', '1'): ('q16', 'B', 1),
    #                         ('q16', 'Z'): ('q16', 'B', 1),
    #                         ('q16', 'B'): ('q17', 'B', -1),
    #                         }

    # def faktorialMode(self):
    #     self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
    #                     'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21',
    #                     'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35'}
    #     self.symbols = {'1', '0', 'B', 'X'}
    #     self.blank_symbol = 'B'
    #     self.input_symbols = {'0', '1', 'X'}
    #     self.initial_state = 'q0'
    #     self.accepting_states = {'q35'}
    #     self.transitions = {
    #                         ('q0', 'B'): ('q0', 'B', 1),
    #                         ('q0', '1'): ('q1', '1', 1),

    #                         ('q1', '0'): ('q2', 'X', 1),
    #                         ('q1', '1'): ('q5', '1', 1),

    #                         ('q2', '0'): ('q2', '0', 1),
    #                         ('q2', '1'): ('q2', '1', 1),
    #                         ('q2', 'B'): ('q3', '0', -1),

    #                         ('q3', '0'): ('q3', '0', -1),
    #                         ('q3', '1'): ('q4', '1', -1),

    #                         ('q4', '0'): ('q4', '0', -1),
    #                         ('q4', 'X'): ('q1', '0', 1),

    #                         ('q5', '0'): ('q5', '0', 1),
    #                         ('q5', 'B'): ('q6', 'B', -1),

    #                         ('q6', '0'): ('q7', '1', -1),
    #                         ('q6', '1'): ('q8', 'B', -1),

    #                         ('q7', '0'): ('q7', '0', -1),
    #                         ('q7', '1'): ('q1', '1', 1),

    #                         ('q8', '1'): ('q8', 'B', -1),
    #                         ('q8', '0'): ('q9', 'B', -1),

    #                         ('q9', '1'): ('q10', '1', -1),

    #                         ('q10', '0'): ('q11', 'X', -1),

    #                         ('q11', '0'): ('q11', '0', -1),
    #                         ('q11', '1'): ('q12', '1', -1),

    #                         ('q12', 'X'): ('q12', 'X', -1),
    #                         ('q12', '0'): ('q13', 'X', 1),
    #                         ('q12', '1'): ('q18', '1', 1),
    #                         ('q12', 'B'): ('q33', 'B', 1),

    #                         ('q13', 'X'): ('q13', 'X', 1),
    #                         ('q13', '1'): ('q14', '1', 1),

    #                         ('q14', 'X'): ('q14', 'X', 1),
    #                         ('q14', '0'): ('q14', '0', 1),
    #                         ('q14', '1'): ('q15', '1', 1),

    #                         ('q15', '0'): ('q15', '0', 1),
    #                         ('q15', 'B'): ('q16', '0', -1),

    #                         ('q16', '0'): ('q16', '0', -1),
    #                         ('q16', '1'): ('q17', '1', -1),

    #                         ('q17', 'X'): ('q17', 'X', -1),
    #                         ('q17', '0'): ('q17', '0', -1),
    #                         ('q17', '1'): ('q12', '1', -1),

    #                         ('q18', 'X'): ('q18', '0', 1),
    #                         ('q18', '1'): ('q19', '1', 1),

    #                         ('q19', '0'): ('q19', '0', 1),
    #                         ('q19', 'X'): ('q20', 'X', -1),

    #                         ('q20', '1'): ('q21', '1', 1),
    #                         ('q20', '0'): ('q11', 'X', -1),

    #                         ('q21', 'X'): ('q21', '1', 1),
    #                         ('q21', '1'): ('q22', '1', -1),

    #                         ('q22', '1'): ('q22', '1', -1),
    #                         ('q22', '0'): ('q23', '1', -1),

    #                         ('q23', '0'): ('q23', '1', -1),
    #                         ('q23', '1'): ('q24', '1', 1),

    #                         ('q24', '0'): ('q24', '0', 1),
    #                         ('q24', '1'): ('q24', '1', 1),
    #                         ('q24', 'B'): ('q25', 'B', -1),

    #                         ('q25', '0'): ('q25', '0', -1),
    #                         ('q25', '1'): ('q26', '1', -1),

    #                         ('q26', '1'): ('q30', '1', 1),
    #                         ('q26', 'B'): ('q27', 'B', 1),
    #                         ('q26', '0'): ('q29', '0', -1),

    #                         ('q27', '1'): ('q28', '1', 1),

    #                         ('q28', '0'): ('q28', '0', 1),
    #                         ('q28', '1'): ('q28', '1', 1),
    #                         ('q28', 'B'): ('q10', '1', -1),

    #                         ('q29', '0'): ('q29', '0', -1),
    #                         ('q29', '1'): ('q28', '1', 1),

    #                         ('q30', '1'): ('q31', '0', 1),

    #                         ('q31', '0'): ('q31', '0', 1),
    #                         ('q31', 'B'): ('q32', 'B', -1),

    #                         ('q32', '0'): ('q25', 'B', -1),

    #                         ('q33', '1'): ('q34', '1', 1),

    #                         ('q34', '0'): ('q34', '0', 1),
    #                         ('q34', 'X'): ('q35', '0', 1),
    #                         }

    # def powerMode(self):
    #     self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
    #                     'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21',
    #                     'q22', 'q23', 'q24', 'q25', 'q26', 'q27'}
    #     self.symbols = {'0', '1', 'b', '#'}
    #     self.blank_symbol = 'b'
    #     self.input_symbols = {'0', '1'}
    #     self.initial_state = 'q0'
    #     self.accepting_states = {'q27'}
    #     self.transitions = {
    #                         ('q0', '0'): ('q1', 'b', 1),
    #                         ('q0', 'b'): ('q0', 'b', 1),

    #                         ('q1', '0'): ('q1', '0', 1),
    #                         ('q1', '1'): ('q2', '1', 1),

    #                         ('q2', 'b'): ('q2', 'b', 1),
    #                         ('q2', '0'): ('q3', 'b', 1),
    #                         ('q2', '1'): ('q7', '1', 1),

    #                         ('q3', '0'): ('q3', '0', 1),
    #                         ('q3', '1'): ('q4', '1', 1),

    #                         ('q4', '0'): ('q4', '0', 1),
    #                         ('q4', '#'): ('q4', '#', 1),
    #                         ('q4', 'b'): ('q5', '0', -1),
    #                         ('q4', '1'): ('q11', '1', -1),

    #                         ('q5', '0'): ('q5', '0', -1),
    #                         ('q5', '1'): ('q6', '1', -1),

    #                         ('q6', '0'): ('q6', '0', -1),
    #                         ('q6', 'b'): ('q2', 'b', 1),

    #                         ('q7', '0'): ('q7', '0', 1),
    #                         ('q7', '#'): ('q7', '#', 1),
    #                         ('q7', 'b'): ('q8', '1', -1),
    #                         ('q7', '1'): ('q18', '#', -1),

    #                         ('q8', '0'): ('q8', '0', -1),
    #                         ('q8', '1'): ('q9', '1', -1),

    #                         ('q9', 'b'): ('q9', '0', -1),
    #                         ('q9', '1'): ('q10', '1', -1),

    #                         ('q10', '0'): ('q10', '0', -1),
    #                         ('q10', 'b'): ('q0', 'b', 1),

    #                         ('q11', 'b'): ('q11', 'b', -1),
    #                         ('q11', '0'): ('q12', 'b', 1),
    #                         ('q11', '1'): ('q15', '1', 1),
    #                         ('q11', '#'): ('q15', '#', 1),

    #                         ('q12', 'b'): ('q12', 'b', 1),
    #                         ('q12', '1'): ('q13', '1', 1),

    #                         ('q13', '0'): ('q13', '0', 1),
    #                         ('q13', 'b'): ('q14', '0', -1),

    #                         ('q14', '0'): ('q14', '0', -1),
    #                         ('q14', '1'): ('q11', '1', -1),

    #                         ('q15', 'b'): ('q15', '0', 1),
    #                         ('q15', '1'): ('q16', '1', -1),

    #                         ('q16', '0'): ('q16', '0', -1),
    #                         ('q16', '#'): ('q16', '#', -1),
    #                         ('q16', '1'): ('q17', '1', -1),

    #                         ('q17', '0'): ('q17', '0', -1),
    #                         ('q17', 'b'): ('q2', 'b', 1),

    #                         ('q18', '0'): ('q18', '0', -1),
    #                         ('q18', '1'): ('q19', '1', 1),
    #                         ('q18', '#'): ('q19', '#', 1),

    #                         ('q19', '0'): ('q19', '#', 1),
    #                         ('q19', '#'): ('q20', '#', 1),

    #                         ('q20', '0'): ('q20', '0', 1),
    #                         ('q20', 'b'): ('q21', '1', -1),

    #                         ('q21', '1'): ('q21', '1', -1),
    #                         ('q21', '0'): ('q21', '0', -1),
    #                         ('q21', '#'): ('q21', '#', -1),
    #                         ('q21', 'b'): ('q22', '0', -1),

    #                         ('q22', 'b'): ('q22', '0', -1),
    #                         ('q22', '1'): ('q23', '1', -1),

    #                         ('q23', '0'): ('q23', '0', -1),
    #                         ('q23', 'b'): ('q0', 'b', 1),

    #                         ('q0', '1'): ('q24', 'b', 1),

    #                         ('q24', '0'): ('q24', 'b', 1),
    #                         ('q24', '1'): ('q25', 'b', 1),

    #                         ('q25', '#'): ('q25', 'b', 1),
    #                         ('q25', '1'): ('q26', 'b', 1),
    #                         ('q25', '0'): ('q26', '0', 1),
    #                         ('q25', 'b'): ('q27', '0', 1),

    #                         ('q26', '0'): ('q26', '0', 1),
    #                         ('q26', '1'): ('q27', 'b', 1),
    #                        }

    # def logaritmaMode(self):
    #     self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
    #                     'q11', 'q12'}
    #     self.symbols = {'0', '1', 'X', 'Z', 'b'}
    #     self.blank_symbol = 'b'
    #     self.input_symbols = {'0', '1', 'X', 'b'}
    #     self.initial_state = 'q0'
    #     self.accepting_states = {'q12'}
    #     self.transitions = {('q0', 'b'): ('q12', 'b', 1),
    #                         ('q0', '0'): ('q1', '0', 1),

    #                         ('q1', 'b'): ('q2', 'b', -1),
    #                         ('q1', '0'): ('q3', '0', 1),

    #                         ('q2', '0'): ('q12', 'b', 1),

    #                         ('q3', 'b'): ('q2', 'b', -1),
    #                         ('q3', '0'): ('q4', 'X', 1),

    #                         ('q4', 'b'): ('q5', 'b', -1),
    #                         ('q4', '0'): ('q8', 'X', -1),
    #                         ('q4', 'X'): ('q4', 'X', 1),

    #                         ('q5', 'X'): ('q5', 'b', -1),
    #                         ('q5', '0'): ('q5', '0', -1),
    #                         ('q5', 'Z'): ('q5', 'Z', -1),
    #                         ('q5', 'b'): ('q6', 'b', 1),

    #                         ('q6', 'Z'): ('q6', '0', 1),
    #                         ('q6', '0'): ('q7', '0', 1),

    #                         ('q7', 'Z'): ('q7', '0', 1),
    #                         ('q7', '0'): ('q11', '0', 1),
    #                         ('q7', 'b'): ('q2', 'b', -1),

    #                         ('q8', 'X'): ('q8', 'X', -1),
    #                         ('q8', '0'): ('q8', '0', -1),
    #                         ('q8', 'Z'): ('q8', 'Z', -1),
    #                         ('q8', 'b'): ('q9', 'b', 1),

    #                         ('q9', '0'): ('q9', 'Z', 1),
    #                         ('q9', 'X'): ('q10', '0', 1),
    #                         ('q9', 'Z'): ('q10', '0', 1),

    #                         ('q10', '0'): ('q10', '0', 1),
    #                         ('q10', 'Z'): ('q10', 'Z', 1),
    #                         ('q10', 'X'): ('q4', 'X', 1),

    #                         ('q11', 'Z'): ('q11', '0', 1),
    #                         ('q11', '0'): ('q11', '0', 1),
    #                         ('q11', 'b'): ('q12', 'b', -1),
    #                         }

    # def squareroot(self):
    #     self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12',
    #                     'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23'}
    #     self.symbols = {'0', '1', 'X', 'b'}
    #     self.blank_symbol = 'b'
    #     self.input_symbols = {'0', '1', 'X', 'b'}
    #     self.initial_state = 'q0'
    #     self.accepting_states = {'q9'}
    #     self.transitions = {
    #                         ('q0', '0'): ('q1', 'b', 1),

    #                         ('q1', '0'): ('q1', '0', 1),
    #                         ('q1', '1'): ('q2', '1', 1),

    #                         ('q2', 'b'): ('q3', '0', 1),

    #                         ('q3', 'b'): ('q4', 'b', -1),
                            
    #                         ('q4', '0'): ('q4', '0', -1),
    #                         ('q4', '1'): ('q5', '1', -1),

    #                         ('q5', '0'): ('q5', '0', -1),
    #                         ('q5', 'b'): ('q6', 'b', 1),

    #                         ('q6', '1'): ('q7', '1', 1),
    #                         ('q6', '0'): ('q10', 'b', 1),

    #                         ('q7', '0'): ('q7', '0', 1),
    #                         ('q7', 'X'): ('q7', 'X', 1),
    #                         ('q7', 'b'): ('q8', 'b', -1),

    #                         ('q8', '0'): ('q8', '0', -1),
    #                         ('q8', 'X'): ('q8', '0', -1),
    #                         ('q8', '1'): ('q9', 'b', 1),

    #                         ('q10', '0'): ('q10', '0', 1),
    #                         ('q10', '1'): ('q11', '1', 1),
                        
    #                         ('q11', 'X'): ('q7', 'X', 1),
    #                         ('q11', '0'): ('q12', 'X', -1),

    #                         ('q12', '1'): ('q13', '1', -1),

    #                         ('q13', '0'): ('q13', '0', -1),
    #                         ('q13', 'b'): ('q14', 'b', 1),

    #                         ('q14', '1'): ('q7', '1', 1),
    #                         ('q14', '0'): ('q15', 'b', 1),

    #                         ('q15', '1'): ('q11', '1', 1),
    #                         ('q15', '0'): ('q16', 'b', 1),

    #                         ('q16', '0'): ('q16', '0', 1),
    #                         ('q16', '1'): ('q17', '1', 1),

    #                         ('q17', 'X'): ('q17', 'X', 1),
    #                         ('q17', 'b'): ('q18', '0', -1),
    #                         ('q17', '0'): ('q21', 'X', -1),

    #                         ('q18', 'X'): ('q18', '0', -1),
    #                         ('q18', '1'): ('q19', '1', -1),

    #                         ('q19', '0'): ('q19', '0', -1),
    #                         ('q19', 'b'): ('q20', 'b', 1),

    #                         ('q20', '1'): ('q7', '1', 1),
    #                         ('q20', '0'): ('q16', 'b', 1),

    #                         ('q21', 'X'): ('q21', 'X', -1),
    #                         ('q21', '1'): ('q22', '1', -1),

    #                         ('q22', '0'): ('q22', '0', -1),
    #                         ('q22', 'b'): ('q23', 'b', 1),

    #                         ('q23', '1'): ('q7', '1', 1),
    #                         ('q23', '0'): ('q15', 'b', 1),
    #                         }
            # end

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