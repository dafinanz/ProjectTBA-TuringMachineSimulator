def akarkuadrat_m(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12',
                        'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23'}
        self.symbols = {'0', '1', 'X', 'B'}
        self.blank_symbol = 'B'
        self.input_symbols = {'0', '1', 'X', 'B'}
        self.initial_state = 'q0'
        self.accepting_states = {'q9'}
        self.transitions = {
                            ('q0', '0'): ('q1', 'B', 1),

                            ('q1', '0'): ('q1', '0', 1),
                            ('q1', '1'): ('q2', '1', 1),

                            ('q2', 'B'): ('q3', '0', 1),

                            ('q3', 'B'): ('q4', 'B', -1),
                            
                            ('q4', '0'): ('q4', '0', -1),
                            ('q4', '1'): ('q5', '1', -1),

                            ('q5', '0'): ('q5', '0', -1),
                            ('q5', 'B'): ('q6', 'B', 1),

                            ('q6', '1'): ('q7', '1', 1),
                            ('q6', '0'): ('q10', 'B', 1),

                            ('q7', '0'): ('q7', '0', 1),
                            ('q7', 'X'): ('q7', 'X', 1),
                            ('q7', 'B'): ('q8', 'B', -1),

                            ('q8', '0'): ('q8', '0', -1),
                            ('q8', 'X'): ('q8', '0', -1),
                            ('q8', '1'): ('q9', 'B', 1),

                            ('q10', '0'): ('q10', '0', 1),
                            ('q10', '1'): ('q11', '1', 1),
                        
                            ('q11', 'X'): ('q7', 'X', 1),
                            ('q11', '0'): ('q12', 'X', -1),

                            ('q12', '1'): ('q13', '1', -1),

                            ('q13', '0'): ('q13', '0', -1),
                            ('q13', 'B'): ('q14', 'B', 1),

                            ('q14', '1'): ('q7', '1', 1),
                            ('q14', '0'): ('q15', 'B', 1),

                            ('q15', '1'): ('q11', '1', 1),
                            ('q15', '0'): ('q16', 'B', 1),

                            ('q16', '0'): ('q16', '0', 1),
                            ('q16', '1'): ('q17', '1', 1),

                            ('q17', 'X'): ('q17', 'X', 1),
                            ('q17', 'B'): ('q18', '0', -1),
                            ('q17', '0'): ('q21', 'X', -1),

                            ('q18', 'X'): ('q18', '0', -1),
                            ('q18', '1'): ('q19', '1', -1),

                            ('q19', '0'): ('q19', '0', -1),
                            ('q19', 'B'): ('q20', 'B', 1),

                            ('q20', '1'): ('q7', '1', 1),
                            ('q20', '0'): ('q16', 'B', 1),

                            ('q21', 'X'): ('q21', 'X', -1),
                            ('q21', '1'): ('q22', '1', -1),

                            ('q22', '0'): ('q22', '0', -1),
                            ('q22', 'B'): ('q23', 'B', 1),

                            ('q23', '1'): ('q7', '1', 1),
                            ('q23', '0'): ('q15', 'B', 1),
                            }