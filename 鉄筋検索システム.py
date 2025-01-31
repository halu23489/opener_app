import tkinter as tk
from tkinter import ttk

def show_animal():
    tab1_selection = tab1_combobox.get()
    tab2_selection = tab2_combobox.get()

    animal_name = animal_combinations.get((tab1_selection, tab2_selection))
    if animal_name:
        result_label.config(text=f"該当のかぶりは: {tab1_selection} の {tab2_selection} では、 {animal_name}")
    else:
        result_label.config(text="該当する組み合わせがありません")

root = tk.Tk()
root.title("鉄筋かぶり検索システム")  # タイトルを日本語で設定
root.geometry("400x200")  # ウィンドウのサイズを指定（幅x高さ）
hen = "設計編"
# プルダウンの作成
tab1_label = ttk.Label(root, text="基にする基準:")
tab1_label.pack()
tab1_combobox = ttk.Combobox(root, values=["コンクリート標準示方書"+ hen, "道路橋仕様書", "NEXCO設計要領書"], state="readonly")  # 読み取り専用に設定
tab1_combobox.current(0)  # 初期値を設定
tab1_combobox.pack()
hen = "設計編"

tab2_label = ttk.Label(root, text="鉄筋径:")
tab2_label.pack()
tab2_combobox = ttk.Combobox(root, values=["D13", "D16", "D19"], state="readonly")  # 読み取り専用に設定
tab2_combobox.current(0)  # 初期値を設定
tab2_combobox.pack()

# 動物名の組み合わせ (文字列キーに変更)
animal_combinations = {
    ("コンクリート標準示方書" + hen, "D13"): "鉄筋かぶり200",
    ("コンクリート標準示方書" + hen, "D16"): "鉄筋かぶり3300",
    ("コンクリート標準示方書" + hen, "D19"): "鉄筋かぶり200",
    ("道路橋仕様書", "D13"): "鉄筋かぶり200",
    ("道路橋仕様書", "D16"): "鉄筋かぶり3300",
    ("道路橋仕様書", "D19"): "鉄筋かぶり200",
    ("NEXCO設計要領書", "D13"): "鉄筋かぶり200",
    ("NEXCO設計要領書", "D16"): "鉄筋かぶり3300",
    ("NEXCO設計要領書", "D19"): "鉄筋かぶり200",
}

# ボタンとラベルの作成
show_button = tk.Button(root, text="検索結果を表示", command=show_animal)
show_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()