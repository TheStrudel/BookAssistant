import tkinter
import tkinter.simpledialog
import tkinter.messagebox
import os.path
import abc
import Application.Code.MainWindow as Main


class Command(metaclass=abc.ABCMeta):
    main_window = None
    project = None
    project_path = None
    script_path = os.path.dirname(os.path.abspath(__file__))
    project_list_path = os.path.dirname(script_path) + "\\Resources\\ProjectData\\ProjectList.txt"

    @staticmethod
    def command_wrapper(display_project=False):
        def decorator(func):
            def wrapper(*args, **kwargs):
                Command.main_window = Main.MainWindow()
                Command.project = getattr(Command.main_window, 'project')
                Command.project_path = getattr(Command.main_window, 'project_directory_path')
                func(*args, **kwargs)
                setattr(Command.main_window, 'project', Command.project)
                setattr(Command.main_window, 'project_directory_path', Command.project_path)
                if display_project:
                    Command.main_window.display_project()
            return wrapper
        return decorator

    @staticmethod
    @abc.abstractmethod
    def execute_command():
        pass


class CreateProjectCommand(Command):
    @staticmethod
    @Command.command_wrapper(True)
    def execute_command():
        project_name = tkinter.simpledialog.askstring("Enter project name", "Project name:")

        with open(Command.project_list_path, "a+") as file:
            for line in file:
                if line.rstrip("\n") == project_name:
                    tkinter.messagebox.showwarning("Project with this name already exists",
                                                   "Please, pick different project name")
                    return

            project_directory_path = os.path.dirname(Command.script_path) + "\\Resources\\Projects\\" + project_name
            if os.path.exists(project_directory_path):
                tkinter.messagebox.showerror("Project directory already exists",
                                             "Please, delete existing project directory")
                return
            else:
                file.write(project_name + '\n')
                os.makedirs(project_directory_path)

                try:
                    with open(project_directory_path + "\\" + project_name + '.prj', "x"):
                        pass
                    Command.project = project_name
                    Command.project_path = project_directory_path
                except IOError:
                    tkinter.messagebox.showerror("Project file already exists",
                                                 "Please, delete existing project file")


class OpenProjectCommand(Command):
    @staticmethod
    @Command.command_wrapper(True)
    def execute_command():
        if os.stat(Command.project_list_path).st_size == 0:
            tkinter.messagebox.showwarning("No projects exist", "Please, create a project")
            return

        project_name = tkinter.simpledialog.askstring("Enter project name to open", "Project name:")
        with open(Command.project_list_path, "r") as file:
            if project_name + '\n' not in file:
                tkinter.messagebox.showwarning("Project doesn't exist", "Please, choose a different project")
                return

        Command.project = project_name
        Command.project_path = os.path.dirname(Command.script_path) + "\\Resources\\Projects\\" + project_name


class DeleteProjectCommand(Command):
    @staticmethod
    @Command.command_wrapper
    def execute_command():
        if tkinter.messagebox.askyesno('Delete project', 'Are you sure you want to delete project?'):
            pass


class CreateFileCommand(Command):
    @staticmethod
    @Command.command_wrapper()
    def execute_command():
        if Command.project is None:
            tkinter.messagebox.showwarning("No opened projects", "Please, open project first")
            return

        file_name = tkinter.simpledialog.askstring("Enter file name", "File name:")
        project_file_path = Command.project_path + '\\' + Command.project + ".prj"

        with open(project_file_path, "a+") as project_fie:
            if Command.project + '\n' in project_fie:
                tkinter.messagebox.showwarning("File already exists", "")
                return
            else:
                project_fie.write(file_name + '\n')
                try:
                    with open(Command.project_path + '\\' + file_name + '.txt', "x"):
                        pass
                except IOError:
                    tkinter.messagebox.showwarning("File already exists", "")


class SaveFileCommand(Command):
    @staticmethod
    @Command.command_wrapper
    def execute_command():
        if Command.project is None:
            tkinter.messagebox.showwarning("No opened projects", "Please, open project first")
            return
    # f = file.File("test.txt", self.textfield.get("1.0", tkinter.END))


class DeleteFileCommand(Command):
    @staticmethod
    @Command.command_wrapper
    def execute_command():
        if tkinter.messagebox.askyesno('Delete file', 'Are you sure you want to delete opened file?'):
            pass
