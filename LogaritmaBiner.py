def logaritma_m(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10',
                        'q11', 'q12'}
        self.symbols = {'0', '1', 'X', 'Z', 'B'}
        self.blank_symbol = 'B'
        self.input_symbols = {'0', '1', 'X', 'B'}
        self.initial_state = 'q0'
        self.accepting_states = {'q12'}
        self.transitions = {('q0', 'B'): ('q12', 'B', 1),
                            ('q0', '0'): ('q1', '0', 1),

                            ('q1', 'B'): ('q2', 'B', -1),
                            ('q1', '0'): ('q3', '0', 1),

                            ('q2', '0'): ('q12', 'B', 1),

                            ('q3', 'B'): ('q2', 'B', -1),
                            ('q3', '0'): ('q4', 'X', 1),

                            ('q4', 'B'): ('q5', 'B', -1),
                            ('q4', '0'): ('q8', 'X', -1),
                            ('q4', 'X'): ('q4', 'X', 1),

                            ('q5', 'X'): ('q5', 'B', -1),
                            ('q5', '0'): ('q5', '0', -1),
                            ('q5', 'Z'): ('q5', 'Z', -1),
                            ('q5', 'B'): ('q6', 'B', 1),

                            ('q6', 'Z'): ('q6', '0', 1),
                            ('q6', '0'): ('q7', '0', 1),

                            ('q7', 'Z'): ('q7', '0', 1),
                            ('q7', '0'): ('q11', '0', 1),
                            ('q7', 'B'): ('q2', 'B', -1),

                            ('q8', 'X'): ('q8', 'X', -1),
                            ('q8', '0'): ('q8', '0', -1),
                            ('q8', 'Z'): ('q8', 'Z', -1),
                            ('q8', 'B'): ('q9', 'B', 1),

                            ('q9', '0'): ('q9', 'Z', 1),
                            ('q9', 'X'): ('q10', '0', 1),
                            ('q9', 'Z'): ('q10', '0', 1),

                            ('q10', '0'): ('q10', '0', 1),
                            ('q10', 'Z'): ('q10', 'Z', 1),
                            ('q10', 'X'): ('q4', 'X', 1),

                            ('q11', 'Z'): ('q11', '0', 1),
                            ('q11', '0'): ('q11', '0', 1),
                            ('q11', 'B'): ('q12', 'B', -1),
                            }