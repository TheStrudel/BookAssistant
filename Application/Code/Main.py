import tkinter
import Application.Code.MainWindow as Main


application_window = tkinter.Tk()
application_window.title("BookAssistant")
application_window.state("zoomed")
main_window = Main.MainWindow(master=application_window)
application_window.mainloop()
