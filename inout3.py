import tkinter as tk
from tkinter import filedialog
import openpyxl

def transfer_data():
    out_path = out_entry.get()
    in_path = in_entry.get()
    save_path = save_entry.get() # 保存先パス

    try:
        out_wb = openpyxl.load_workbook(out_path)
        in_wb = openpyxl.load_workbook(in_path)

        out_sheet = out_wb["工事概要書【社内用ISO書式】 (3)"]
        in_sheet = in_wb["工事概要"]

        # 転記処理 (例)
        transfer_list = [
            ("M10","C5"),
            ("M28", "C13"),
            ("Z28", "E13"),
            ("M31", "C16"),
            ("A115", "D25"),
            ("K115", "D26"),
            ("M1", "D24"),
            ("M19", "C18"),
        ]

        for out_cell, in_cell in transfer_list:
            value = out_sheet[out_cell].value
            in_sheet[in_cell].value = value

        in_wb.save(save_path)  # 指定したパスに保存
        result_label.config(text=f"{save_path} に保存しました")

    except FileNotFoundError:
        result_label.config(text="ファイルが見つかりません")
    except KeyError as e:
        result_label.config(text=f"エラー: {e}")
    except Exception as e:
        result_label.config(text=f"エラー: {e}")

root = tk.Tk()
root.title("Excelデータ転送")

# ファイルパス入力
out_label = tk.Label(root, text="元データパス:")
out_label.grid(row=0, column=0)
out_entry = tk.Entry(root)
out_entry.grid(row=0, column=1)
out_button = tk.Button(root, text="参照", command=lambda: out_entry.insert(0, filedialog.askopenfilename()))
out_button.grid(row=0, column=2)

in_label = tk.Label(root, text="転載先データパス:")
in_label.grid(row=1, column=0)
in_entry = tk.Entry(root)
in_entry.grid(row=1, column=1)
in_button = tk.Button(root, text="参照", command=lambda: in_entry.insert(0, filedialog.askopenfilename()))
in_button.grid(row=1, column=2)

# 保存先入力
save_label = tk.Label(root, text="保存先パス:")
save_label.grid(row=2, column=0)
save_entry = tk.Entry(root)
save_entry.grid(row=2, column=1)
save_button = tk.Button(root, text="参照", command=lambda: save_entry.insert(0, filedialog.asksaveasfilename(defaultextension=".xlsx"))) # 拡張子をデフォルトに
save_button.grid(row=2, column=2)

# 転送ボタン
transfer_button = tk.Button(root, text="転送", command=transfer_data)
transfer_button.grid(row=3, column=0, columnspan=3)

# 結果表示ラベル
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=3)

root.mainloop()