"""
This script automates the picking and compiling of a QT Designer .UI file.
It is designed to be used as an add in tool for Visual Studio 2022.

It will pop a file selector, then pick the .UI file to compile and it will then
send the proper commands to pyuic5.

pyuic5 must be in the path somewhere - it is usually in the Python scripts
directory.

Totally free script, but remember,
   "Written by an infinite number of Monkeys in an infinite amount of time,
    ...so beware."
"""

import subprocess
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import sys

root = tk.Tk()
root.withdraw()


# File Selector Dialog Box
def select_file(title_msg):
    filetypes = (('UI files', '*.ui'), ('All files', '*.*'))
    file_path_selected = filedialog.askopenfilename(
        title=title_msg, filetypes=filetypes)
    return file_path_selected


# ===== Main ========================================================================================
# Get the input file name
file_path = select_file('Open a UI file')

# Check for cancel
if len(file_path) == 0:
    messagebox.showinfo("Error", "No UI file selected.")
    sys.exit(0)

# Parse the input file name
file_name = os.path.basename(file_path)
file_name, file_extension = os.path.splitext(file_name)

# Check for proper extension
if file_extension != '.ui':
    messagebox.showinfo("Error", "You picked the wrong input file type!")
    sys.exit(0)

# Run pyuic5.exe (It must be in the path somewhere)
cmd = []
cmd.append('pyuic5')
cmd.append('-x')

file_in = file_name + '.ui'
cmd.append(file_in)

cmd.append('-o')

file_out = file_name + '.py'
cmd.append(file_out)

result = subprocess.run(cmd)

# Check the result for gross errors
if result.returncode == 0:
    print("Created: " + file_out + "\n")
else:
    print("\nReturn code was not zero - so some error happened!\n")


# --- Fini ---
