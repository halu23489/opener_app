import tkinter as tk
from tkinter import ttk

def show_animal():
    tab1_selection = tab1_combobox.get()
    tab2_selection = tab2_combobox.get()

    animal_name = animal_combinations.get((tab1_selection, tab2_selection))
    if animal_name:
        result_label.config(text=f"組み合わせ: {tab1_selection} + {tab2_selection} = {animal_name}")
    else:
        result_label.config(text="該当する組み合わせがありません")

root = tk.Tk()
root.title("動物名表示アプリ")

# プルダウンの作成
tab1_label = ttk.Label(root, text="グループ1:")
tab1_label.pack()
tab1_combobox = ttk.Combobox(root, values=["a", "b", "c"], state="readonly") # 読み取り専用に設定
tab1_combobox.current(0)  # 初期値を設定
tab1_combobox.pack()

tab2_label = ttk.Label(root, text="グループ2:")
tab2_label.pack()
tab2_combobox = ttk.Combobox(root, values=["1", "2", "3"], state="readonly") # 読み取り専用に設定
tab2_combobox.current(0)  # 初期値を設定
tab2_combobox.pack()

# 動物名の組み合わせ (文字列キーに変更)
animal_combinations = {
    ("a", "1"): "犬",
    ("a", "2"): "猫",
    ("a", "3"): "猿",
    ("b", "1"): "ライオン",
    ("b", "2"): "虎",
    ("b", "3"): "熊",
    ("c", "1"): "ゾウ",
    ("c", "2"): "キリン",
    ("c", "3"): "シマウマ",
}

# ボタンとラベルの作成
show_button = tk.Button(root, text="動物名を表示", command=show_animal)
show_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()