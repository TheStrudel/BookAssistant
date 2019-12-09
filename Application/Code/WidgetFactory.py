# import abc
# import Application.Code.MainWindow as Main
# import Application.Code.Commands as Commands
#
#
# class WidgetFactory(metaclass=abc.ABCMeta):
#     @staticmethod
#     @abc.abstractmethod
#     def create_widget(self):
#         pass
#
#     def
#
#
# class MenuWidget(WidgetFactory):
#     def create_widget(self):
#         self.menu = tkinter.Menu(self.root)
#
#         project_menu = tkinter.Menu(self.menu, tearoff=False)
#         project_menu.add_command(label="New Project", command=Commands.CreateProjectCommand.execute_command)
#         project_menu.add_command(label="Open Project", command=Commands.OpenProjectCommand.execute_command)
#         project_menu.add_separator()
#         project_menu.add_command(label="Save")
#         project_menu.add_command(label="Delete")
#         project_menu.add_separator()
#         project_menu.add_command(label="Create File", command=Commands.CreateFileCommand.execute_command)
#         # project_menu.add_command(label="Add File")
#
#         self.menu.add_cascade(label="Project", menu=project_menu)
#
#         version_menu = tkinter.Menu(self.menu, tearoff=False)
#         version_menu.add_command(label="Change Version")
#         version_menu.add_command(label="Compare Versions")
#
#         self.menu.add_cascade(label="Versions", menu=version_menu)
#
#         self.root.config(menu=self.menu)
#
#
# class TextfieldWidget(WidgetFactory):
#     def create_widget(self):
#         self.root.update()
#         self.textfield = tkinter.scrolledtext.ScrolledText(self.root,
#                                                            width=int(self.root.winfo_width() / 15),
#                                                            undo=True)
#         self.textfield.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)
#
#
# class NotesfieldWidget(WidgetFactory):
#     def create_widget(self):
#         self.textfield.update()
#         self.notes_field = tkinter.scrolledtext.ScrolledText(self.root,
#                                                              width=int(self.textfield.winfo_width() / 65),
#                                                              undo=True)
#         self.notes_field.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)
#
#
# class FrameWidget(WidgetFactory):
#     def create_widget(self):
#         self.root.update()
#         self.manager_frame = tkinter.Frame(self.root)
#         self.manager_frame.pack(side=tkinter.LEFT, expand=True, fill=tkinter.BOTH)
#
#         self.button_frame = tkinter.Frame(self.manager_frame)
#         self.button_frame.pack(side=tkinter.TOP, fill=tkinter.X)
#
#         self.hide_manager_button = tkinter.Button(self.button_frame, text='Hide', bg='#ccffcc')
#         self.hide_manager_button.pack(side=tkinter.RIGHT)
#
#         self.create_project_tree()
#         self.create_version_tree()
#
#
# class ProjectTreeWidget(WidgetFactory):
#     def create_widget(self):
#         self.project_tree = tkinter.ttk.Treeview(self.manager_frame)
#         self.project_tree.insert('', 'end', 'widgets', text='Project1')
#         self.project_tree.pack(side=tkinter.TOP, expand=True, fill=tkinter.BOTH)
#
#
# class VersionTreeWidget(WidgetFactory):
#     def create_widget(self):
#         self.version_tree = tkinter.ttk.Treeview(self.manager_frame)
#         self.version_tree.pack(side=tkinter.TOP, expand=True, fill=tkinter.BOTH)
