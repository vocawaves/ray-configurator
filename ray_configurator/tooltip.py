import tkinter as tk
import tkinter.ttk as ttk

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None

    def show_tip(self):
        "Display the tooltip"
        if self.tip_window or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = ttk.Label(tw, justify='left', background="#ffffe0",
                          relief='solid', borderwidth=1, font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

        label.config(text=self.text)

    def hide_tip(self):
        "Hide the tooltip"
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()

def add_tooltip(widget, text):
    tooltip = Tooltip(widget, text)
    widget.bind('<Enter>', lambda event: tooltip.show_tip())
    widget.bind('<Leave>', lambda event: tooltip.hide_tip())
