import os
import tkinter as tk
from tkinter import filedialog, messagebox

def open_file_from_path():
    folder_path = entry.get()
    if os.path.isdir(folder_path):
        file_path = filedialog.askopenfilename(initialdir=folder_path)
        if file_path:
            os.startfile(file_path)
    else:
        messagebox.showerror("エラー", "有効なフォルダパスを入力してください。")
        
def create_app():
    root = tk.Tk()
    root.title("フォルダパスからファイルを開く")

    global entry
    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)

    open_button = tk.Button(root, text="ファイルを開く", command=open_file_from_path)
    open_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_app()   