import tkinter as tk
from tkinter import ttk, filedialog, Menu
import mappings

class RayConfigurator(tk.Frame):
    # main window
    def __init__(self, master):
        self.master = master
        self.master.title("ray-configurator - unsaved")
        self.master.geometry("400x300")
        self.current_file = None

        # NAVIGATION MENU
        self.menu = Menu(self.master)
        # file menu
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_values)
        self.file_menu.add_command(label="Save As", command=self.save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        # help menu
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="About")
        self.menu.add_cascade(label="Help", menu=self.help_menu)

        self.master.config(menu=self.menu)

        # ACTUAL LOGIC
        # defaults - move later
        self.current_values = {
            'SUN_SHADOW_SAMPLE_QUALITY': 1,
            'MULTI_SHADOW_MAP_QUALITY': 1
        }
        
        max_label_width = max(len(mappings.name[key]) for key in mappings.name)

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill="both", expand=True)

        self.tabs = {}
        self.inputs = {}
        self.labels = {}

        for category in mappings.category.keys():
            self.tabs[category] = ttk.Frame(self.notebook)
            self.notebook.add(self.tabs[category], text=category)

            for key in mappings.category[category]:
                frame = tk.Frame(self.tabs[category])
                frame.pack(side="top", fill="x", padx=10, pady=5)
                
                self.labels[key] = tk.Label(frame, text=mappings.name[key], width=max_label_width + 2, anchor="w")
                self.labels[key].pack(side="left")
                
                value = mappings.setting[key][self.current_values[key]]

                if mappings.inputs[key] == "dropdown":
                    self.inputs[key] = ttk.Combobox(frame, state="readonly", values=list(mappings.setting[key].values()))
                    self.inputs[key].set(value)
                    self.inputs[key].pack(side="right")
                    self.inputs[key].bind("<<ComboboxSelected>>", self.on_value_change)
                elif mappings.inputs[key] == "checkbox":
                    self.inputs[key] = tk.BooleanVar()
                    self.inputs[key].set(value)
                    tk.Checkbutton(frame, variable=self.inputs[key]).pack(side="right")
                    self.inputs[key].trace_add("write", self.on_value_change)
        
        self.save_button = tk.Button(self.master, text="Save", command=self.save_values)
        self.save_button.pack(side="left", padx=(0, 10))

    # on value change
    def on_value_change(self, key):
        self.master.title(f"ray-configurator - {self.current_file} *")

    # open file
    def open_file(self):
        filetypes = [("Configuration files", "*.conf"), ("All files", "*.*")]
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            self.current_file = filename
            self.master.title(f"ray-configurator - {self.current_file}")
            self.load_values()

    # save as file
    def save_as(self):
        self.current_file = None
        self.save_values()
    
    # save to file
    def save_values(self):
        if self.current_file:
            with open(self.current_file, "r") as f:
                lines = f.readlines()
            with open(self.current_file, "w") as f:
                for line in lines:
                    for key in mappings.setting.keys():
                        if line.startswith(f"#define {key}"):
                            numerical_value = str(list(mappings.setting[key].keys())[list(mappings.setting[key].values()).index(self.inputs[key].get())])
                            self.current_values[key] = int(numerical_value)
                            line = f"#define {key} {numerical_value}\n"
                    f.write(line)
        else:
            filetypes = [("Configuration files", "*.conf"), ("All files", "*.*")]
            filename = filedialog.asksaveasfilename(filetypes=filetypes)
            if filename:
                self.current_file = filename
                self.master.title(f"ray-configurator - {self.current_file}")
                with open(self.current_file, "w") as f:
                    for key in mappings.setting.keys():
                        numerical_value = str(list(mappings.setting[key].keys())[list(mappings.setting[key].values()).index(self.inputs[key].get())])
                        self.current_values[key] = int(numerical_value)
                        line = f"#define {key} {numerical_value}\n"
                        f.write(line)
            else:
                return
        print("Values saved successfully.")
        self.master.title(f"ray-configurator - {self.current_file}")

    # load from file
    def load_values(self):
        with open(self.current_file, "r") as f:
            lines = f.readlines()
        for line in lines:
            for key in mappings.setting.keys():
                if line.startswith(f"#define {key}"):
                    numerical_value = int(line.strip().split()[-1])
                    value = mappings.setting[key][numerical_value]
                    self.current_values[key] = numerical_value
                    self.inputs[key].set(value)
                    break
        print("Values loaded successfully.")

root = tk.Tk()
app = RayConfigurator(root)
root.mainloop()
