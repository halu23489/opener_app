import tkinter as tk
from tkinter import filedialog
import pandas as pd
import ezdxf

def load_csv_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        df = pd.read_csv(file_path)
        select_cad_file(df)

def select_cad_file(df):
    cad_path = filedialog.askopenfilename(filetypes=[("DXF files", "*.dxf")])
    if cad_path:
        doc = ezdxf.readfile(cad_path)
        add_circles_to_cad(doc, df)

def add_circles_to_cad(doc, df):
    msp = doc.modelspace()

    # 各座標点を円で囲む
    radius = 1000
    for index, row in df.iterrows():
        center = (row['x'], row['y'], row['z'])
        msp.add_circle(center=center, radius=radius)

    save_path = filedialog.asksaveasfilename(defaultextension=".dxf", filetypes=[("DXF files", "*.dxf")])
    if save_path:
        doc.saveas(save_path)
        print(f"CADファイルが保存されました: {save_path}")

root = tk.Tk()
root.title("CSVからCADファイル作成")
root.geometry("400x100")

load_button = tk.Button(root, text="CSVファイルを読み込む", command=load_csv_file)
load_button.pack(pady=20)

root.mainloop()