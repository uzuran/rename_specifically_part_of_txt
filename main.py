from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox as msg
import os


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Create root windows with geometry.
        parent.geometry("300x300+10+20")

        # Main title.
        parent.title('JW 2000')

        # Function for browse files.
        def browse_files():
            file_paths = filedialog.askopenfilenames()

            # Select path and rename it with .txt format.
            for file_path in file_paths:
                new_file_name = os.path.splitext(file_path)[0] + ".txt"
                os.rename(file_path, new_file_name)
                # Call the next function and pass new_file_name as an argument.
                make_correct_format_for_table(new_file_name)

        def make_correct_format_for_table(new_file_name):

                with open(new_file_name, "r+") as f:
                    lines = f.readlines()
                    fourth_line = lines[3]

                    list_of_material = ["1.0", "2.0", "3.0", "4.0", "5.0", "6.0", "7.0", "8.0", "10.0", "15.0", "20.0"]
                    if fourth_line[10:13] in list_of_material:
                        char_list = list(fourth_line)
                        del char_list[10:13]
                        updated_line = ''.join(char_list)
                        lines[3] = updated_line
                        f.seek(0)
                        f.writelines(lines)
                        f.close()
                        success = Label(text="Success, in correct format", fg="green")
                        success.pack()
                        self.after(5000, success.destroy)
                    else:
                        msg.showwarning(title="Warning", message="Already renamed!")

        def browse_files_add_mh():
            file_paths = filedialog.askopenfilenames()

            # Select path and rename it with .txt format.
            for file_path in file_paths:
                new_file_name = os.path.splitext(file_path)[0] + ".txt"
                os.rename(file_path, new_file_name)
                # Call the next function and pass new_file_name as an argument.
                make_correct_format_for_table_mh(new_file_name)

        def make_correct_format_for_table_mh(new_file_name):

                with open(new_file_name, "r+") as f:
                    lines = f.readlines()
                    fourth_line = lines[25]
                    char_list = list(fourth_line)
                    list_of_mh = ["M"]

                    if char_list[5] in list_of_mh:
                        msg.showwarning(message="MH already EXIST!")

                    else:

                        char_list = list(fourth_line)
                        new_char_list = char_list[:5] + ['M', 'H', '-'] + char_list[5:]
                        updated_line = ''.join(new_char_list)
                        lines[25] = updated_line
                        f.seek(0)
                        f.writelines(lines)
                        f.close()
                        success = Label(text="Success add MH", fg="green")
                        success.pack()
                        self.after(5000, success.destroy)

        def browse_files_add_pm():
            file_paths = filedialog.askopenfilenames()

            # Select path and rename it with .txt format.
            for file_path in file_paths:
                new_file_name = os.path.splitext(file_path)[0] + ".txt"
                os.rename(file_path, new_file_name)
                # Call the next function and pass new_file_name as an argument.
                make_correct_format_for_table_pm(new_file_name)

        def make_correct_format_for_table_pm(new_file_name):
                with open(new_file_name, "r+") as f:
                    lines = f.readlines()
                    fourth_line = lines[25]
                    char_list = list(fourth_line)
                    list_of_pm = ["-"]

                    if char_list[17] in list_of_pm:
                        msg.showwarning(message="PM already EXIST!")

                    else:

                        char_list = list(fourth_line)
                        new_char_list = char_list[:17] + ['-', 'P', 'M'] + char_list[17:]
                        updated_line = ''.join(new_char_list)
                        lines[25] = updated_line
                        f.seek(0)
                        f.writelines(lines)
                        f.close()
                        success = Label(text="Success add PM", fg="green")
                        success.pack()
                        self.after(5000, success.destroy)

        def browse_files_for_nc():
            file_paths = filedialog.askopenfilenames()

            # Select path and rename it with .txt format.
            for file_path in file_paths:
                new_file_name = os.path.splitext(file_path)[0] + ".NC"
                os.rename(file_path, new_file_name)
                success_rename_nc = Label(text="Success format NC", fg="green")
                success_rename_nc.pack()
                self.after(5000, success_rename_nc.destroy)

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

        # Label.
        label_for_rename_pm = Label(self, text="Rename files with NC ending.")
        label_for_rename_pm.pack()
        # Button for file selected.
        button_for_selected_file = Button(self, text="Add files for NC",
                                          command=browse_files_for_nc)
        button_for_selected_file.pack()


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()

