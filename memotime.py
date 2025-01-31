import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import csv

log_entries = []

def log_entry():
    text = entry.get()
    if text:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_text = f"{current_time} - {text}\n"
        log_box.insert(tk.END, log_text)
        entry.delete(0, tk.END)
        log_entries.append((current_time, text))

def save_log():
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["Time", "Text"])
            csv_writer.writerows(log_entries)

# Tkinterのウィンドウを作成
root = tk.Tk()
root.title("ログ記録アプリ")

# 入力フィールド
tk.Label(root, text="文字を入力してください:").pack()
entry = tk.Entry(root)
entry.pack()

# ログボタン
log_button = tk.Button(root, text="ログに記録", command=log_entry)
log_button.pack()

# 保存ボタン
save_button = tk.Button(root, text="まとめて保存", command=save_log)
save_button.pack()

# ログ表示ボックス
log_box = tk.Text(root, height=10, width=50)
log_box.pack()

# Tkinterのメインループを開始
root.mainloop()