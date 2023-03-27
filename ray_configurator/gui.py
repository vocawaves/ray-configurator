import tkinter as tk
from tkinter import ttk, filedialog, Menu, messagebox
import mappings


class RayConfigurator(tk.Frame):
    # main window
    def __init__(self, master):
        self.master = master
        self.master.title("ray-configurator - unsaved")
        self.master.geometry("600x400")
        self.master.resizable(False, False)
        self.current_file = None
        self.unsaved_changes = False
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

        # NAVIGATION MENU
        self.menu = Menu(self.master)
        # file menu
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(
            label="New", command=self.new_file, accelerator="Ctrl+N")
        self.file_menu.add_command(
            label="Open", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(
            label="Save", command=self.save_values, accelerator="Ctrl+S")
        self.file_menu.add_command(
            label="Save As", command=self.save_as, accelerator="Ctrl+Shift+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        # help menu
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(label="About", command=self.about)
        self.menu.add_cascade(label="Help", menu=self.help_menu)

        self.master.config(menu=self.menu)

        # KEYBINDS
        self.master.bind("<Control-n>", lambda event: self.new_file())
        self.master.bind("<Control-s>", lambda event: self.save_values())
        self.master.bind("<Control-o>", lambda event: self.open_file())
        self.master.bind("<Control-Shift-s>", lambda event: self.save_as())

        # RENDER SETTINGS
        self.current_values = mappings.defaults

        max_label_width = max(len(mappings.name[key]) for key in mappings.name)

        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill="both", expand=True)

        self.tabs = {}
        self.inputs = {}
        self.labels = {}
        self.checkbox_objects = {}
        self.checkbox_vals = {}

        for category in mappings.category.keys():
            self.tabs[category] = ttk.Frame(self.notebook)
            self.notebook.add(self.tabs[category], text=category)

            for key in mappings.category[category]:
                frame = tk.Frame(self.tabs[category])
                frame.pack(side="top", fill="x", padx=10, pady=5)

                self.labels[key] = tk.Label(
                    frame, text=mappings.name[key], width=max_label_width + 2, anchor="w")
                self.labels[key].pack(side="left")

                value = mappings.setting[key][self.current_values[key]]

                if mappings.inputs[key] == "dropdown":
                    self.inputs[key] = ttk.Combobox(
                        frame, state="readonly", values=list(mappings.setting[key].values()))
                    self.inputs[key].set(value)
                    self.inputs[key].pack(side="right")
                    self.inputs[key].bind(
                        "<<ComboboxSelected>>", lambda event: self.on_value_change())
                elif mappings.inputs[key] == "checkbox":
                    checkbox_var = tk.BooleanVar()
                    checkbox_var.set(value == "Enabled")
                    checkbox = tk.Checkbutton(
                        frame, variable=checkbox_var, command=lambda key=key: self.on_checkbox_changed(key, checkbox_var))
                    checkbox.pack(side="right")
                    self.checkbox_objects[key] = checkbox
                    self.checkbox_vals[key] = checkbox_var

    # on value change
    def on_value_change(self):
        if self.current_file:
            self.master.title(f"ray-configurator - {self.current_file} *")
        else:
            self.master.title(f"ray-configurator - unsaved *")
        self.unsaved_changes = True

    # annoying checkbox fix
    def on_checkbox_changed(self, key, var):
        if var.get():
            self.inputs[key] = "Enabled"
        else:
            self.inputs[key] = "Disabled"

    # open file
    def open_file(self):
        if self.unsaved_changes:
            answer = messagebox.askyesnocancel(
                "Unsaved changes", "You have unsaved changes. Do you want to save them?")
            if answer == True:
                self.save_values()
            elif answer == False:
                pass
            else:
                return
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
                            if mappings.inputs[key] == "checkbox":
                                input_value = self.checkbox_vals[key].get()
                            else:
                                input_value = self.inputs[key].get()
                            if isinstance(input_value, bool):
                                numerical_value = int(input_value)
                            else:
                                numerical_value = str(list(mappings.setting[key].keys())[
                                                      list(mappings.setting[key].values()).index(input_value)])
                            self.current_values[key] = int(numerical_value)
                            line = f"#define {key} {numerical_value}\n"
                    f.write(line)
        else:
            filetypes = [("Configuration files", "*.conf"),
                         ("All files", "*.*")]
            filename = filedialog.asksaveasfilename(filetypes=filetypes)
            if filename:
                self.current_file = filename
                self.master.title(f"ray-configurator - {self.current_file}")
                with open(self.current_file, "w") as f:
                    for key in mappings.setting.keys():
                        if mappings.inputs[key] == "checkbox":
                            input_value = self.checkbox_vals[key].get()
                        else:
                            input_value = self.inputs[key].get()
                        if isinstance(input_value, bool):
                            numerical_value = int(input_value)
                        else:
                            numerical_value = str(list(mappings.setting[key].keys())[
                                                  list(mappings.setting[key].values()).index(input_value)])
                        self.current_values[key] = int(numerical_value)
                        line = f"#define {key} {numerical_value}\n"
                        f.write(line)
            else:
                return
        print("Values saved successfully.")
        self.master.title(f"ray-configurator - {self.current_file}")
        self.unsaved_changes = False

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
                    if mappings.inputs[key] == "dropdown":
                        self.inputs[key].set(value)
                    elif mappings.inputs[key] == "checkbox":
                        checkbox_var = tk.BooleanVar()
                        checkbox_var.set(value == "Enabled")
                        self.checkbox_objects[key].config(
                            variable=checkbox_var)
                    break
        print("Values loaded successfully.")

    # new file
    def new_file(self):
        if self.unsaved_changes:
            answer = messagebox.askyesnocancel(
                "Unsaved changes", "You have unsaved changes. Do you want to save them?")
            if answer == True:
                self.save_values()
            elif answer == False:
                pass
            else:
                return
        self.current_file = None
        self.current_values = mappings.defaults
        for key in mappings.setting.keys():
            value = mappings.setting[key][self.current_values[key]]
            if mappings.inputs[key] == "dropdown":
                self.inputs[key].set(value)
            elif mappings.inputs[key] == "checkbox":
                checkbox_var = tk.BooleanVar()
                checkbox_var.set(value == "Enabled")
                self.checkbox_objects[key].config(variable=checkbox_var)
                self.checkbox_vals[key] = checkbox_var
        self.master.title("ray-configurator - unsaved")
        self.unsaved_changes = False

    # about
    def about(self):
        messagebox.showinfo(
            "About", "ray-configurator v1.0.0\n\nDeveloped by @davidcralph")

    def on_close(self):
        if self.unsaved_changes:
            if messagebox.askyesno("Unsaved changes", "You have unsaved changes. Are you sure you want to exit?"):
                self.master.destroy()
            else:
                return
        else:
            self.master.destroy()

root = tk.Tk()
app = RayConfigurator(root)
root.mainloop()
