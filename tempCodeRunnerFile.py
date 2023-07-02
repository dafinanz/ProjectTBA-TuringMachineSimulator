        self.canvas_frame = Canvas(self.window, width=400, height=400)
        self.canvas_frame.pack(side='left', fill='both', expand=True)

        self.canvas = Canvas(self.canvas_frame)
        self.canvas.pack(side='left', fill='both', expand=True)

        self.scrollbar = Scrollbar(self.canvas_frame, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame_output = ttk.LabelFrame(self.window, text="Output", width=600)
        self.frame_output.pack()

        self.canvas_output = Canvas(self.frame_output, width=600, height=300)
        self.canvas_output.pack()