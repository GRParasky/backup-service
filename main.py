import tkinter as tk
from tkinter import filedialog as fs

import functions as f


file_path = str()


root = tk.Tk()
app_width = 800
app_height = 400
root.geometry(f"{app_width}x{app_height}")
root.title("Backup FW7")

label = tk.Label(root, text="Bem-vindo ao serviço de Backup do Seviço da FW!")
service_path = tk.Button(root, text="Caminho do Integrador", command=f.service_folder)
exit_button = tk.Button(root, text="Sair", command=f.exit_program, padx=30)

label.pack()
service_path.pack()
exit_button.pack(side=tk.BOTTOM, )

print(file_path)

root.mainloop()
