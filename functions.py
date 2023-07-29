from tkinter import filedialog as fs

def service_folder():
    file_path = fs.askdirectory()
    print(file_path)

def exit_program():
    exit()