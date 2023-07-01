# from tes import TuringMachine

from collections import defaultdict

def initialize(self, input_symbols: 'dict[int, str]'):
    self.head = 0
    self.halted = False
    self.current_state = self.initial_state
    self.tape = defaultdict(lambda: self.blank_symbol, input_symbols)
    self.tape_string = []

def additionMode(self):
        self.states = {'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13'}
        self.symbols = {'-0', '-1', '0', '1', 'b'}
        self.blank_symbol = 'b'
        self.input_symbols = {'0', '1', '-0', '-1'}
        self.initial_state = 'q1'
        self.accepting_states = {'q13'}
        self.transitions = {
                            ('q1', '0'): ('q1', '0', 1),
                            ('q1', '1'): ('q2', '0', 1),
                            ('q1', 'b'): ('q1', 'b', 1),
                            ('q1', '-0'): ('q6', 'b', 1),

                            ('q2', '0'): ('q2', '0', 1),
                            ('q2', '-0'): ('q2', '-0', 1),
                            ('q2', 'b'): ('q3', 'b', -1),

                            ('q3', '-0'): ('q4', 'b', -1),
                            ('q3', '0'): ('q13', 'b', -1),

                            ('q4', '-0'): ('q4', '-0', -1),
                            ('q4', '0'): ('q4', '0', -1),
                            ('q4', 'b'): ('q5', 'b', 1),

                            ('q5', '0'): ('q2', 'b', 1),
                            ('q5', '-0'): ('q11', '-0', -1),

                            ('q11', 'b'): ('q12', '-0', 1),

                            ('q12', '-0'): ('q12', '-0', 1),
                            ('q12', 'b'): ('q13', '-0', 1),

                            ('q6', '-0'): ('q6', '-0', 1),
                            ('q6', '1'): ('q7', '1', 1),

                            ('q7', '0'): ('q7', '0', 1),
                            ('q7', 'b'): ('q8', 'b', -1),
                            ('q7', '-0'): ('q8', '-0', -1),

                            ('q8', '1'): ('q13', '-0', -1),
                            ('q8', '0'): ('q9', 'b', -1),
                            ('q8', '-0'): ('q9', 'b', -1),

                            ('q9', '0'): ('q9', '0', -1),
                            ('q9', '-0'): ('q9', '-0', -1),
                            ('q9', '1'): ('q10', '1', -1),

                            ('q10', '-0'): ('q10', '-0', -1),
                            ('q10', 'b'): ('q1', 'b', 1),
                            }