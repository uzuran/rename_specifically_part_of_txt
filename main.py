from tkinter import *
import tkinter as tk

from functions import browse_files, browse_files_add_mh, browse_files_add_pm


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Create root windows with geometry.
        parent.geometry("300x300+10+20")

        # Main title.
        parent.title('JW 2000')
        label_for_rename_table = Label(self, text="JW 2000", font="Arial")
        label_for_rename_table.pack()

        # Label.
        label_for_rename_table = Label(self, text="Add files and rename material to correct format.")
        label_for_rename_table.pack()
        # Button for file selected.
        button_for_selected_file = Button(self, text="Add files",
                                          command=browse_files)
        button_for_selected_file.pack()
        # Label.
        label_for_rename_mh = Label(self, text="Add files and add MH at the beginning of the table.")
        label_for_rename_mh.pack()
        # Button for file selected.
        button_for_selected_file = Button(self, text="Add files for MH",
                                          command=browse_files_add_mh)
        button_for_selected_file.pack()

        # Label.
        label_for_rename_pm = Label(self, text="Add files and add PM at the end of table name.")
        label_for_rename_pm.pack()
        # Button for file selected.
        button_for_selected_file = Button(self, text="Add files fro PM",
                                          command=browse_files_add_pm)
        button_for_selected_file.pack()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

