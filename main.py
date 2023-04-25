import tkinter as tk
import time


class Clock(tk.Label):
    def __init__(self, parent=None, seconds=True, **kw):
        tk.Label.__init__(self, parent, kw)
        self.display_seconds = seconds
        self.update_time()
        self.pack()

    def update_time(self):
        if self.display_seconds:
            format = '%H:%M:%S'
        else:
            format = '%H:%M'
        current_time = time.strftime(format)
        self.config(text=current_time)
        self.after(1000, self.update_time)


if __name__ == '__main__':
    root = tk.Tk()
    clock = Clock(root, font=('Helvetica', 48), seconds=True)
    root.mainloop()
