import tkinter as tk
import tkinter.messagebox
import time
import winsound


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

        # 获取当前时间
        current_hour = int(time.strftime('%H'))
        current_minute = int(time.strftime('%M'))
        current_second = int(time.strftime('%S'))

        # 如果当前时间与报时时间一致，则弹出对话框并播放声音
        if (current_hour == 8 and current_minute == 0 and current_second == 0) or \
                (current_hour == 8 and current_minute == 0 and current_second == 1) or \
                (current_hour == 8 and current_minute == 30 and current_second == 0) or \
                (current_hour == 9 and current_minute == 0 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0) or \
                (current_hour == 16 and current_minute == 10 and current_second == 0):
            tk.messagebox.showinfo('报时', '现在是' + str(current_hour) + '点' + str(current_minute) + '分！')
            winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)

        self.after(1000, self.update_time)


if __name__ == '__main__':
    root = tk.Tk()
    clock = Clock(root, font=('Helvetica', 48), seconds=True)
    root.mainloop()
