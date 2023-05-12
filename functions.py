import os
from tkinter import filedialog
import tkinter as tk
from tkinter import messagebox as msg


def rename_to_nc(file_paths):
    # Select path and rename it with .txt format.
    for file_path in file_paths:
        new_file_name = os.path.splitext(file_path)[0] + ".NC"
        os.rename(file_path, new_file_name)


def browse_files():
    file_paths = filedialog.askopenfilenames(initialdir="X:/", title="Select a File", filetypes=[("Nc files", "*.NC")])

    # Select path and rename it with .txt format.
    for file_path in file_paths:
        if file_path.endswith(".NC"):
            new_file_name = os.path.splitext(file_path)[0] + ".txt"
            os.rename(file_path, new_file_name)
            # Call the next function and pass new_file_name as an argument.
            make_correct_format_for_table(new_file_name)
            rename_to_nc([new_file_name])


def make_correct_format_for_table(new_file_name):
    with open(new_file_name, "r+") as f:
        lines = f.readlines()
        fourth_line = lines[3]

        list_of_material = ["-1.0", "-2.0", "-3.0", "-4.0", "-5.0", "-6.0", "-8.0", "-10.0", "-12.0", "-15.0",
                            "-20.0", "-22.0"]
        if fourth_line[10:13] in list_of_material:
            char_list = list(fourth_line)
            del char_list[10:13]
            updated_line = ''.join(char_list)
            lines[3] = updated_line
            f.seek(0)
            f.writelines(lines)
            f.close()
            success = tk.Label(text="Success, in correct format", fg="green")
            success.pack()
            success.after(5000, success.destroy)

        elif fourth_line[10:14] in list_of_material:
            char_list = list(fourth_line)
            del char_list[10:14]
            updated_line = ''.join(char_list)
            lines[3] = updated_line
            f.seek(0)
            f.writelines(lines)
            f.close()
            success = tk.Label(text="Success, in correct format", fg="green")
            success.pack()
            success.after(5000, success.destroy)
        else:
            msg.showwarning(title="Warning", message="Already renamed!")


def browse_files_add_mh():
    file_paths = filedialog.askopenfilenames(initialdir="X:/", title="Select a File", filetypes=[("Nc files", "*.NC")])

    # Select path and rename it with .txt format.
    for file_path in file_paths:
        new_file_name = os.path.splitext(file_path)[0] + ".txt"
        os.rename(file_path, new_file_name)
        # Call the next function and pass new_file_name as an argument.
        make_correct_format_for_table_mh(new_file_name)
        rename_to_nc([new_file_name])


def make_correct_format_for_table_mh(new_file_name):
    with open(new_file_name, "r+") as f:
        lines = f.readlines()
        line_24 = lines[24]
        line_23 = lines[23]
        line_25 = lines[25]
        list_from_line_24 = list(line_24)
        list_from_line_25 = list(line_25)
        list_of_mh = ["M"]

        if len(line_23) == 1:
            if list_from_line_24[5] in list_of_mh:
                msg.showwarning(title="MH format already exists.", message="MH already EXISTS!")
            elif list_from_line_24[18] == "-":
                msg.showwarning(title="PM format already exists.", message="You have PM format here already.")
            else:
                new_char_list = list_from_line_24[:5] + ['M', 'H', '-'] + list_from_line_24[5:]
                updated_line = ''.join(new_char_list)
                lines[24] = updated_line
                f.seek(0)
                f.writelines(lines)
                f.close()
                success = tk.Label(text="Success add MH", fg="green")
                success.pack()
                success.after(5000, success.destroy)
        elif len(line_24) == 1:
            if list_from_line_25[5] in list_of_mh:
                msg.showwarning(title="MH format already exists.", message="MH already EXISTS!")
            elif list_from_line_25[18] == "-":
                msg.showwarning(title="PM format already exists.", message="You have PM format here already.")
            else:
                new_char_list = list_from_line_25[:5] + ['M', 'H', '-'] + list_from_line_25[5:]
                updated_line = ''.join(new_char_list)
                lines[25] = updated_line
                f.seek(0)
                f.writelines(lines)
                f.close()
                success = tk.Label(text="Success add MH", fg="green")
                success.pack()
                success.after(5000, success.destroy)


def browse_files_add_pm():
    file_paths = filedialog.askopenfilenames(initialdir="X:/", title="Select a File", filetypes=[("Nc files", "*.NC")])

    # Select path and rename it with .txt format.
    for file_path in file_paths:
        new_file_name = os.path.splitext(file_path)[0] + ".txt"
        os.rename(file_path, new_file_name)
        # Call the next function and pass new_file_name as an argument.
        make_correct_format_for_table_pm(new_file_name)
        rename_to_nc([new_file_name])


def make_correct_format_for_table_pm(new_file_name):
    with open(new_file_name, "r+") as f:
        lines = f.readlines()
        line_24 = lines[24]
        line_23 = lines[23]
        line_25 = lines[25]
        list_from_line_24 = list(line_24)
        list_from_line_25 = list(line_25)

        if len(line_23) == 1:
            if list_from_line_24[5] == "M":
                msg.showwarning(title="MH format already exists.", message="MH already EXISTS!")
            elif list_from_line_24[18] == "-":
                msg.showwarning(title="PM format already exists.", message="You have PM format here already.")
            else:
                new_char_list = list_from_line_24[:18] + ['-', 'P', 'M'] + list_from_line_24[18:]
                updated_line = ''.join(new_char_list)
                lines[24] = updated_line
                f.seek(0)
                f.writelines(lines)
                f.close()
                success = tk.Label(text="Success add PM", fg="green")
                success.pack()
                success.after(5000, success.destroy)
        elif len(line_24) == 1:
            if list_from_line_25[5] == "M":
                msg.showwarning(title="MH format already exists.", message="MH already EXISTS!")
            elif list_from_line_25[17] == "-":
                msg.showwarning(title="PM format already exists.", message="You have PM format here already.")
            else:
                new_char_list = list_from_line_25[:18] + ['-', 'P', 'M'] + list_from_line_25[18:]
                updated_line = ''.join(new_char_list)
                lines[25] = updated_line
                f.seek(0)
                f.writelines(lines)
                f.close()
                success = tk.Label(text="Success add PM", fg="green")
                success.pack()
                success.after(5000, success.destroy)

