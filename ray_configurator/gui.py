import tkinter as tk
from tkinter import ttk, filedialog, Menu, messagebox
import importlib
import tooltip
import webbrowser

class RayConfigurator(tk.Frame):
    # main window
    def __init__(self, master):
        self.mappings = importlib.import_module('mappings.dev')
        self.language = importlib.import_module('languages.english').strings

        self.master = master
        self.master.title("ray-configurator - unsaved")
        self.master.geometry("600x400")
        self.master.resizable(False, False)
        self.current_file = None
        self.unsaved_changes = False
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
        self.recent_files = []

        # KEYBINDS
        self.master.bind("<Control-n>", lambda event: self.new_file())
        self.master.bind("<Control-s>", lambda event: self.save_values())
        self.master.bind("<Control-o>", lambda event: self.open_file())
        self.master.bind("<Control-Shift-s>", lambda event: self.save_as())
        self.master.bind("<F1>", lambda event: self.about())

        # INIT
        self.current_values = self.mappings.defaults
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill="both", expand=True)

        self.tabs = {}
        self.inputs = {}
        self.labels = {}
        self.checkbox_objects = {}
        self.checkbox_vals = {}

        self.init_menu()
        self.init_ui()

    def init_menu(self):
        # NAVIGATION MENU
        self.menu = Menu(self.master)
        # file menu
        self.file_menu = Menu(self.menu, tearoff=0)
        self.file_menu.add_command(
            label=self.language['menu_file_new_dev'], command=lambda: self.new_file('dev'), accelerator="Ctrl+N")
        self.file_menu.add_command(
            label=self.language['menu_file_new_stable'], command=lambda: self.new_file('stable'), accelerator="Ctrl+Shift+N")
        self.file_menu.add_command(
            label=self.language['menu_file_new_legacy'], command=lambda: self.new_file('legacy'))
        self.file_menu.add_command(
            label=self.language['menu_file_new_ancient'], command=lambda: self.new_file('ancient'))
        self.file_menu.add_command(
            label=self.language['menu_file_open'], command=self.open_file, accelerator="Ctrl+O")

        self.recent_menu = Menu(self.file_menu, tearoff=0)
        if len(self.recent_files) == 0:
            self.recent_menu.add_command(label=self.language['menu_file_open_recent_none'], state="disabled")
        for i in self.recent_files:
            self.file_menu.add_command(label=i, command=lambda: self.open_file(i))
        self.file_menu.add_cascade(label=self.language['menu_file_open_recent'], menu=self.recent_menu)
        self.file_menu.add_command(
            label=self.language['menu_file_save'], command=self.save_values, accelerator="Ctrl+S")
        self.file_menu.add_command(
            label=self.language['menu_file_save_as'], command=self.save_as, accelerator="Ctrl+Shift+S")
        self.file_menu.add_separator()
        self.file_menu.add_command(label=self.language['menu_file_exit'], command=self.master.quit)
        self.menu.add_cascade(label=self.language['menu_file'], menu=self.file_menu)

        # view menu
        self.view_menu = Menu(self.menu, tearoff=0)
        self.language_menu = Menu(self.view_menu, tearoff=0)
        self.english = tk.BooleanVar()
        self.english.set(True)
        self.japanese = tk.BooleanVar()
        self.language_menu.add_checkbutton(
            label="English", command=lambda: self.set_language('english'), onvalue=1, offvalue=0, variable=self.english)
        self.language_menu.add_checkbutton(
            label="日本語", command=lambda: self.set_language('japanese'), onvalue=1, offvalue=0, variable=self.japanese)
        self.view_menu.add_cascade(label=self.language['menu_view_language'], menu=self.language_menu)
        self.view_menu.add_command(label="Clear Recent Items", command=self.clear_recent)
        self.menu.add_cascade(label=self.language['menu_view'], menu=self.view_menu)

        # help menu
        self.help_menu = Menu(self.menu, tearoff=0)
        self.help_menu.add_command(
            label=self.language['menu_help_docs'], command=self.documentation)
        self.help_menu.add_separator()
        self.help_menu.add_command(
            label=self.language['menu_help_about'], command=self.about, accelerator="F1")
        self.menu.add_cascade(label=self.language['menu_help'], menu=self.help_menu)

        self.master.config(menu=self.menu)


    def init_ui(self):
        max_label_width = max(
            len(self.mappings.name[key]) for key in self.mappings.name)

        # preset buttons
        self.preset_frame = tk.Frame(self.master)
        self.preset_frame.pack(side="top", fill="x", padx=10, pady=5)

        self.preset_label = tk.Label(
            self.preset_frame, text=self.language['presets'], width=max_label_width + 2, anchor="w")
        self.preset_label.pack(side="left")

        self.preset_dropdown = ttk.Combobox(
            self.preset_frame, state="readonly", values=list(self.mappings.presets.keys()))
        self.preset_dropdown.set("Default")
        self.preset_dropdown.pack(side="right")
        self.preset_dropdown.bind(
            "<<ComboboxSelected>>", lambda event: self.on_preset_change())

        for category in self.mappings.category.keys():
            self.tabs[category] = ttk.Frame(self.notebook)
            self.notebook.add(self.tabs[category], text=category)

            for key in self.mappings.category[category]:
                frame = tk.Frame(self.tabs[category])
                frame.pack(side="top", fill="x", padx=10, pady=5)

                self.labels[key] = tk.Label(
                    frame, text=self.mappings.name[key], width=max_label_width + 2, anchor="w")
                self.labels[key].pack(side="left")
                tooltip.add_tooltip(
                    self.labels[key], self.mappings.description[key])

                value = self.mappings.setting[key][self.current_values[key]]

                if self.mappings.inputs[key] == "dropdown":
                    self.inputs[key] = ttk.Combobox(
                        frame, state="readonly", values=list(self.mappings.setting[key].values()))
                    self.inputs[key].set(value)
                    self.inputs[key].pack(side="right")
                    self.inputs[key].bind(
                        "<<ComboboxSelected>>", lambda event: self.on_value_change())
                elif self.mappings.inputs[key] == "checkbox":
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

        self.preset_dropdown.set("Custom")
        self.unsaved_changes = True


    # annoying checkbox fix
    def on_checkbox_changed(self, key, var):
        self.inputs[key] = "Enabled" if var.get() else "Disabled"
        self.on_value_change()


    # on preset change
    def on_preset_change(self):
        self.current_values = self.mappings.presets[self.preset_dropdown.get()]
        for key in self.mappings.name.keys():
            value = self.mappings.setting[key][self.current_values[key]]
            if self.mappings.inputs[key] == "dropdown":
                self.inputs[key].set(value)
            elif self.mappings.inputs[key] == "checkbox":
                checkbox_var = tk.BooleanVar()
                checkbox_var.set(value == "Enabled")
                self.checkbox_vals[key] = checkbox_var
                self.checkbox_objects[key].config(
                    variable=checkbox_var)

    # open file
    def open_file(self):
        if self.unsaved_changes:
            answer = messagebox.askyesnocancel(
                self.language['unsaved_title'], self.language['unsaved_message'])
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
            # recent files
            if len(self.recent_files) == 0:
                self.recent_menu.delete(0)
            if filename not in self.recent_files:
                self.recent_files.append(filename)
                self.recent_menu.add_command(
                    label=filename, command=lambda filename=filename: self.open_recent(filename))
            if len(self.recent_files) > 5:
                self.recent_files.pop(0)
                self.recent_menu.delete(0, "end")

            self.master.title(f"ray-configurator - {self.current_file}")
            self.load_values()

    def clear_recent(self):
        self.recent_files = []
        self.recent_menu.delete(0, "end")
        self.recent_menu.add_command(
            label=self.language['no_recent'], command=self.clear_recent)


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
                    for key in self.mappings.setting.keys():
                        if line.startswith(f"#define {key}"):
                            if self.mappings.inputs[key] == "checkbox":
                                input_value = self.checkbox_vals[key].get()
                            else:
                                input_value = self.inputs[key].get()

                            if isinstance(input_value, bool):
                                numerical_value = int(input_value)
                            else:
                                numerical_value = str(list(self.mappings.setting[key].keys())[
                                                      list(self.mappings.setting[key].values()).index(input_value)])

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
                    for key in self.mappings.setting.keys():
                        if self.mappings.inputs[key] == "checkbox":
                            input_value = self.checkbox_vals[key].get()
                        else:
                            input_value = self.inputs[key].get()

                        if isinstance(input_value, bool):
                            numerical_value = int(input_value)
                        else:
                            numerical_value = str(list(self.mappings.setting[key].keys())[
                                                  list(self.mappings.setting[key].values()).index(input_value)])

                        self.current_values[key] = int(numerical_value)
                        line = f"#define {key} {numerical_value}\n"
                        f.write(line)
            else:
                return
        print("Values saved successfully.")
        self.master.title(f"ray-configurator - {self.current_file}")
        self.unsaved_changes = False

    def reset_tabs(self):
        self.current_values = self.mappings.defaults

        self.tabs = {}
        self.inputs = {}
        self.labels = {}
        self.checkbox_objects = {}
        self.checkbox_vals = {}
        for i in self.notebook.tabs():
            self.notebook.forget(i)
        self.preset_frame.destroy()
        
        self.init_ui()
        
        self.menu.delete(0, "end")
        self.init_menu()


    # load from file
    def load_values(self):
        with open(self.current_file, "r") as f:
            lines = f.readlines()
            not_dev = False
            for line in lines:
                if '#define MAIN_LIGHT_ENABLE' in line:
                    self.mappings = importlib.import_module("mappings.legacy")
                    self.reset_tabs()
                    not_dev = True
                    break
                elif '#define IBL_QUALITY' in line:
                    self.mappings = importlib.import_module("mappings.ancient")
                    self.reset_tabs()
                    not_dev = True
                    break
                elif '#define BOKEH_QUALITY' in line:
                    self.mappings = importlib.import_module("mappings.stable")
                    self.reset_tabs()
                    not_dev = True
                    break

            if not_dev:
                self.mappings = importlib.import_module("mappings.dev")
                self.reset_tabs()

            for line in lines:
                for key in self.mappings.setting.keys():
                    if line.startswith(f"#define {key}"):
                        numerical_value = int(line.strip().split()[-1])
                        value = self.mappings.setting[key][numerical_value]
                        self.current_values[key] = numerical_value

                        if self.mappings.inputs[key] == "dropdown":
                            self.inputs[key].set(value)
                        elif self.mappings.inputs[key] == "checkbox":
                            checkbox_var = tk.BooleanVar()
                            checkbox_var.set(value == "Enabled")
                            self.checkbox_vals[key] = checkbox_var
                            self.checkbox_objects[key].config(
                                variable=checkbox_var)
                        break

            print("Values loaded successfully.")
            self.unsaved_changes = False


    # MENU CONTROLS
    # new file
    def new_file(self, type):
        if self.unsaved_changes:
            answer = messagebox.askyesnocancel(
                self.language['unsaved_title'], self.language['unsaved_message'])
            if answer == True:
                self.save_values()
            elif answer == False:
                pass
            else:
                return

        self.mappings = importlib.import_module("mappings." + type)
        self.reset_tabs()
        self.current_file = None
        self.current_values = self.mappings.defaults

        for key in self.mappings.setting.keys():
            value = self.mappings.setting[key][self.current_values[key]]

            if self.mappings.inputs[key] == "dropdown":
                self.inputs[key].set(value)
            elif self.mappings.inputs[key] == "checkbox":
                checkbox_var = tk.BooleanVar()
                checkbox_var.set(value == "Enabled")
                self.checkbox_objects[key].config(variable=checkbox_var)
                self.checkbox_vals[key] = checkbox_var

        self.master.title("ray-configurator - unsaved")
        self.unsaved_changes = False


    # set language (english/japanese)
    def set_language(self, language):
        self.mappings.set_language(language)
        self.language = importlib.import_module('languages.' + language).strings
        self.reset_tabs()
        if language == "english":
            self.english.set(True)
            self.japanese.set(False)
        elif language == "japanese":
            self.english.set(False)
            self.japanese.set(True)


    # about
    def about(self):
        messagebox.showinfo(
            "About", "ray-configurator v1.0.0\n\nDeveloped by @davidcralph")


    # docs
    def documentation(self):
        webbrowser.open("https://github.com/ray-cast/ray-mmd/wiki", new=2)

    def on_close(self):
        if self.unsaved_changes:
            if messagebox.askyesno(self.language['unsaved_title'], self.language['unsaved_exit']):
                self.master.destroy()
            else:
                return
        else:
            self.master.destroy()


root = tk.Tk()
app = RayConfigurator(root)
root.mainloop()
