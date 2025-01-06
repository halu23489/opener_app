import os
import tkinter as tk
from tkinter import filedialog, messagebox

def set_folder_path():
    employee_number = entry.get()
    if employee_number:
        folder_path = f"C:\\Users\\{employee_number}\\"
        if os.path.isdir(folder_path):
            entry_path.delete(0, tk.END)
            entry_path.insert(0, folder_path)
        else:
            messagebox.showerror("エラー", "有効なフォルダパスが見つかりません。")
    else:
        messagebox.showerror("エラー", "従業員番号を入力してください。")
        
def open_file_from_path():
    folder_path = entry_path.get()
    if os.path.isdir(folder_path):
        file_path = filedialog.askopenfilename(initialdir=folder_path)
        if file_path:
            os.startfile(file_path)
    else:
        messagebox.showerror("エラー", "有効なフォルダパスを入力してください。")
        
def create_app():
    root = tk.Tk()
    root.title("従業員番号からフォルダパスを設定")

    global entry, entry_path
    tk.Label(root, text="従業員番号:").pack(pady=5)
    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)

    set_path_button = tk.Button(root, text="フォルダパスを設定", command=set_folder_path)
    set_path_button.pack(pady=5)

    tk.Label(root, text="フォルダパス:").pack(pady=5)
    entry_path = tk.Entry(root, width=50)
    entry_path.pack(pady=5)

    open_button = tk.Button(root, text="ファイルを開く", command=open_file_from_path)
    open_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_app()