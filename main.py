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
        time_points = [(8, 0, 0), (8, 30, 0),  # 上午上班
                       (9, 0, 0), (9, 30, 0),
                       (10, 0, 0), (10, 30, 0),
                       (11, 0, 0), (11, 30, 0),
                       (12, 0, 0), (12, 27, 0), (12, 28, 0),  # 上午下班
                       (13, 0, 0), (13, 30, 0),  # 下午上班
                       (14, 0, 0), (14, 30, 0),
                       (15, 0, 0), (15, 30, 0),
                       (16, 0, 0), (16, 30, 0),
                       (17, 0, 0), (17, 30, 0),
                       (18, 0, 0), (18, 29, 0), # 下午下班
                       (18, 30, 0), (18, 31, 0),  # 晚上上班
                       (19, 0, 0), (19, 30, 0),
                       (20, 0, 0), (20, 30, 0)]  # 晚上下班

        current_time = (current_hour, current_minute, current_second)

        if current_time in time_points:
            # winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
            # winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
            # winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
            # winsound.PlaySound('SystemExclamation', winsound.SND_ALIAS)
            winsound.PlaySound('C:/Windows/Media/Ring09.wav', winsound.SND_FILENAME)
            winsound.PlaySound('C:/Windows/Media/Ring09.wav', winsound.SND_FILENAME)
            tk.messagebox.showinfo('报时', '现在是' + str(current_hour) + '点' + str(current_minute) + '分！')

        self.after(1000, self.update_time)
        # winsound.PlaySound('C:/Windows/Media/Ring09.wav', winsound.SND_FILENAME)


if __name__ == '__main__':
    root = tk.Tk()
    clock = Clock(root, font=('Helvetica', 48), seconds=True)
    root.mainloop()

# Generate exe in command line
# pip install pyinstaller
# cd C:\gitcloud\alarm-clock
# pyinstaller main.py --noconsole
