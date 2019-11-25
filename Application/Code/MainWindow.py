import tkinter
import tkinter.scrolledtext
import tkinter.ttk
import tkinter.messagebox
import tkinter.simpledialog
import os


class MainWindow(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.project = None

        self.create_menu()
        self.create_manager_frame()
        self.create_textfield()
        self.create_notes_field()

    def create_menu(self):
        self.menu = tkinter.Menu(self.master)

        project_menu = tkinter.Menu(self.menu, tearoff=False)
        project_menu.add_command(label="New Project", command=self.create_project)
        project_menu.add_command(label="Open Project", command=self.open_project)
        project_menu.add_separator()
        project_menu.add_command(label="Save")
        project_menu.add_command(label="Delete")
        project_menu.add_separator()
        project_menu.add_command(label="Create File", command=self.create_file)
        project_menu.add_command(label="Add File")

        self.menu.add_cascade(label="Project", menu=project_menu)

        version_menu = tkinter.Menu(self.menu, tearoff=False)
        version_menu.add_command(label="Change Version")
        version_menu.add_command(label="Compare Versions")

        self.menu.add_cascade(label="Versions", menu=version_menu)

        self.master.config(menu=self.menu)

    def create_textfield(self):
        self.master.update()
        self.textfield = tkinter.scrolledtext.ScrolledText(self.master,
                                                           width=int(self.master.winfo_width() / 15),
                                                           undo=True)
        self.textfield.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)

    def create_notes_field(self):
        self.textfield.update()
        self.notes_field = tkinter.scrolledtext.ScrolledText(self.master,
                                                             width=int(self.textfield.winfo_width() / 65),
                                                             undo=True)
        self.notes_field.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)

    def create_manager_frame(self):
        self.master.update()
        self.manager_frame = tkinter.Frame(self.master)
        self.manager_frame.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)

        self.button_frame = tkinter.Frame(self.manager_frame)
        self.button_frame.pack(side=tkinter.TOP, fill=tkinter.X)

        self.hide_manager_button = tkinter.Button(self.button_frame, text='Hide', bg='#ccffcc')
        self.hide_manager_button.pack(side=tkinter.RIGHT)

        self.create_project_tree()
        self.create_version_tree()

    def create_project_tree(self):
        self.project_tree = tkinter.ttk.Treeview(self.manager_frame)
        self.project_tree.insert('', 'end', 'widgets', text='Project1')
        self.project_tree.pack(side=tkinter.TOP, expand=True, fill=tkinter.BOTH)

    def create_version_tree(self):
        self.version_tree = tkinter.ttk.Treeview(self.manager_frame)

        self.version_tree.pack(side=tkinter.TOP, expand=True, fill=tkinter.BOTH)

    def create_project(self):
        project_name = tkinter.simpledialog.askstring("Enter project name", "Project name:")
        script_path = os.path.dirname(os.path.abspath(__file__))
        project_file_path = os.path.dirname(script_path) + u"\\Resources\\ProjectData\\ProjectList.txt"
        print(project_file_path)
        with open(project_file_path, "a+") as file:
            for line in file:
                if line.rstrip("\n") == project_name:
                    tkinter.messagebox.showwarning("Project with this name already exists",
                                                   "Please, pick different project name")
                    return

            project_directory_path = os.path.dirname(script_path) + "\\Resources\\Projects\\" + project_name
            if os.path.exists(project_directory_path):
                tkinter.messagebox.showerror("Project directory already exists",
                                             "Please, delete existing project directory")
                return
            else:
                file.write(project_name + '\n')
                os.makedirs(project_directory_path)

                try:
                    self.project = project_name
                    with open(project_directory_path + "\\" + project_name + '.prj', "x") as self.file:
                        pass
                except IOError:
                    tkinter.messagebox.showerror("Project file already exists",
                                                 "Please, delete existing project file")

    def open_project(self):
        script_path = os.path.dirname(os.path.abspath(__file__))
        project_file_path = os.path.dirname(script_path) + u"\\Resources\\ProjectData\\ProjectList.txt"

        if os.stat(project_file_path).st_size == 0:
            tkinter.messagebox.showwarning("No projects exist", "Please, create a project")
            return

        project_name = tkinter.simpledialog.askstring("Enter project name to open", "Project name:")
        with open(project_file_path, "r") as file:
            if project_name + '\n' not in file:
                tkinter.messagebox.showwarning("Project doesn't exist", "Please, choose a different project")
                return
        self.project = project_name

    def create_file(self):
        if self.project is None:
            tkinter.messagebox.showwarning("No opened projects", "Please, open project first")

    # def
    # f = file.File("test.txt", self.textfield.get("1.0", tkinter.END))
