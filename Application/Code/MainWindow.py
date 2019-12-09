import tkinter
import tkinter.scrolledtext
import tkinter.ttk
import Application.Code.Commands as Commands


class MainWindow(object):
    __instance = None
    project = None
    project_directory_path = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(MainWindow, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if self.__initialized:
            return
        self.__initialized = True

        self.root = tkinter.Tk()
        self.root.title("BookAssistant")
        self.root.state("zoomed")

        self.main_window = tkinter.Frame(master=self.root)
        self.main_window.pack()
        self.create_menu()
        self.create_manager_frame()
        self.create_textfield()
        self.create_notes_field()

        self.project = None

        self.root.mainloop()

    def create_menu(self):
        self.menu = tkinter.Menu(self.root)

        project_menu = tkinter.Menu(self.menu, tearoff=False)
        project_menu.add_command(label="New Project", command=Commands.CreateProjectCommand.execute_command)
        project_menu.add_command(label="Open Project", command=Commands.OpenProjectCommand.execute_command)
        project_menu.add_separator()
        project_menu.add_command(label="Delete Project", command=Commands.DeleteProjectCommand.execute_command)
        project_menu.add_separator()
        project_menu.add_command(label="Create File", command=Commands.CreateFileCommand.execute_command)
        project_menu.add_command(label="Save File")
        project_menu.add_command(label="Delete File")
        # project_menu.add_command(label="Add File")

        self.menu.add_cascade(label="Project", menu=project_menu)

        version_menu = tkinter.Menu(self.menu, tearoff=False)
        version_menu.add_command(label="Change Version")
        version_menu.add_command(label="Compare Versions")

        self.menu.add_cascade(label="Versions", menu=version_menu)

        self.root.config(menu=self.menu)

    def create_textfield(self):
        self.root.update()
        self.textfield = tkinter.scrolledtext.ScrolledText(self.root,
                                                           width=int(self.root.winfo_width() / 15),
                                                           undo=True)
        self.textfield.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)

    def create_notes_field(self):
        self.textfield.update()
        self.notes_field = tkinter.scrolledtext.ScrolledText(self.root,
                                                             width=int(self.textfield.winfo_width() / 65),
                                                             undo=True)
        self.notes_field.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)

    def create_manager_frame(self):
        self.root.update()
        self.manager_frame = tkinter.Frame(self.root)
        self.manager_frame.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)

        self.button_frame = tkinter.Frame(self.manager_frame)
        self.button_frame.pack(side=tkinter.TOP, fill=tkinter.X)

        self.hide_manager_button = tkinter.Button(self.button_frame, text='Hide', bg='#ccffcc', command=self.hide)
        self.hide_manager_button.pack(side=tkinter.RIGHT)

        self.create_project_tree()
        self.create_version_tree()

    def create_project_tree(self):
        self.project_tree = tkinter.ttk.Treeview(self.manager_frame)
        self.project_tree.pack(side=tkinter.TOP, expand=True, fill=tkinter.BOTH)

    def hide(self):
        if self.project_tree.winfo_ismapped() and self.version_tree.winfo_ismapped():
            self.project_tree.pack_forget()
            self.version_tree.pack_forget()
        else:
            self.project_tree.pack(side=tkinter.TOP, expand=True, fill=tkinter.BOTH)
            self.version_tree.pack(side=tkinter.BOTTOM, expand=True, fill=tkinter.BOTH)

    def display_project(self):
        self.project_tree.insert('', 'end', 'project', text=self.project)

        with open(self.project_directory_path + '\\' + self.project + '.prj') as file:
            for line in file:
                self.project_tree.insert('project', 'end', text=line)

    def create_version_tree(self):
        self.version_tree = tkinter.ttk.Treeview(self.manager_frame)
        self.version_tree.pack(side=tkinter.BOTTOM, expand=True, fill=tkinter.BOTH)
