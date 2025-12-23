import tkinter as tk
from tkinter import ttk, messagebox
import math

# --- LOGIC WRAPPERS ---
# These functions wrap your existing logic so they work with GUI inputs instead of CLI input()

def calculate_basic(n1, n2, op):
    try:
        num1, num2 = float(n1), float(n2)
        if op == "+": return num1 + num2
        if op == "-": return num1 - num2
        if op == "*": return num1 * num2
        if op == "/": return num1 / num2 if num2 != 0 else "Error: Div by 0"
    except ValueError:
        return "Invalid Input"

def calculate_2d(shape, val1, val2=0):
    try:
        v1, v2 = float(val1), float(val2)
        if shape == "Rectangle/Square": return v1 * v2
        if shape == "Circle": return v1 * v1 * math.pi
        if shape == "Triangle": return (v1 * v2) / 2
    except ValueError:
        return "Invalid Input"

def calculate_3d(shape, l, w=0, h=0):
    try:
        l, w, h = float(l), float(w), float(h)
        if shape == "Cube": return l * l * 6  # Surface Area as per your 3d shape.py
        if shape == "Sphere": return l * l * 4 * math.pi
        if shape == "Rectangular Prism": return l * w * h
    except ValueError:
        return "Invalid Input"

# --- GUI APPLICATION ---

class PyCalcGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PyCalc - Graphical Edition")
        self.root.geometry("450x550")

        # Create Tabs
        self.tabs = ttk.Notebook(root)
        self.tab_basic = ttk.Frame(self.tabs)
        self.tab_2d = ttk.Frame(self.tabs)
        self.tab_3d = ttk.Frame(self.tabs)

        self.tabs.add(self.tab_basic, text="Basic Calc")
        self.tabs.add(self.tab_2d, text="2D Shapes")
        self.tabs.add(self.tab_3d, text="3D Shapes")
        self.tabs.pack(expand=1, fill="both")

        self.setup_basic_ui()
        self.setup_2d_ui()
        self.setup_3d_ui()

    def setup_basic_ui(self):
        frame = ttk.LabelFrame(self.tab_basic, text="Arithmetic")
        frame.pack(padx=20, pady=20, fill="both")

        ttk.Label(frame, text="Number 1:").grid(row=0, column=0, pady=5)
        self.b_n1 = ttk.Entry(frame)
        self.b_n1.grid(row=0, column=1)

        ttk.Label(frame, text="Number 2:").grid(row=1, column=0, pady=5)
        self.b_n2 = ttk.Entry(frame)
        self.b_n2.grid(row=1, column=1)

        ttk.Label(frame, text="Operation:").grid(row=2, column=0, pady=5)
        self.b_op = ttk.Combobox(frame, values=["+", "-", "*", "/"])
        self.b_op.grid(row=2, column=1)
        self.b_op.current(0)

        ttk.Button(frame, text="Calculate", command=self.run_basic).grid(row=3, columnspan=2, pady=10)
        self.b_res = ttk.Label(frame, text="Result: --", font=("Arial", 12, "bold"))
        self.b_res.grid(row=4, columnspan=2)

    def run_basic(self):
        res = calculate_basic(self.b_n1.get(), self.b_n2.get(), self.b_op.get())
        self.b_res.config(text=f"Result: {res}")

    def setup_2d_ui(self):
        frame = ttk.LabelFrame(self.tab_2d, text="Area Calculation")
        frame.pack(padx=20, pady=20, fill="both")

        ttk.Label(frame, text="Shape:").grid(row=0, column=0, pady=5)
        self.shape_2d = ttk.Combobox(frame, values=["Rectangle/Square", "Circle", "Triangle"])
        self.shape_2d.grid(row=0, column=1)
        self.shape_2d.current(0)

        ttk.Label(frame, text="Dim 1 (Length/Radius/Base):").grid(row=1, column=0, pady=5)
        self.d2_v1 = ttk.Entry(frame)
        self.d2_v1.grid(row=1, column=1)

        ttk.Label(frame, text="Dim 2 (Width/Height):").grid(row=2, column=0, pady=5)
        self.d2_v2 = ttk.Entry(frame)
        self.d2_v2.grid(row=2, column=1)

        ttk.Button(frame, text="Calculate Area", command=self.run_2d).grid(row=3, columnspan=2, pady=10)
        self.d2_res = ttk.Label(frame, text="Area: --", font=("Arial", 12, "bold"))
        self.d2_res.grid(row=4, columnspan=2)

    def run_2d(self):
        res = calculate_2d(self.shape_2d.get(), self.d2_v1.get(), self.d2_v2.get() or 0)
        self.d2_res.config(text=f"Area: {res}")

    def setup_3d_ui(self):
        frame = ttk.LabelFrame(self.tab_3d, text="Volume & Surface Area")
        frame.pack(padx=20, pady=20, fill="both")

        ttk.Label(frame, text="Shape:").grid(row=0, column=0, pady=5)
        self.shape_3d = ttk.Combobox(frame, values=["Cube", "Sphere", "Rectangular Prism"])
        self.shape_3d.grid(row=0, column=1)
        self.shape_3d.current(0)

        ttk.Label(frame, text="Length/Radius:").grid(row=1, column=0, pady=5)
        self.d3_l = ttk.Entry(frame)
        self.d3_l.grid(row=1, column=1)

        ttk.Label(frame, text="Width (Prism only):").grid(row=2, column=0, pady=5)
        self.d3_w = ttk.Entry(frame)
        self.d3_w.grid(row=2, column=1)

        ttk.Label(frame, text="Height (Prism only):").grid(row=3, column=0, pady=5)
        self.d3_h = ttk.Entry(frame)
        self.d3_h.grid(row=3, column=1)

        ttk.Button(frame, text="Calculate 3D", command=self.run_3d).grid(row=4, columnspan=2, pady=10)
        self.d3_res = ttk.Label(frame, text="Result: --", font=("Arial", 12, "bold"))
        self.d3_res.grid(row=5, columnspan=2)

    def run_3d(self):
        res = calculate_3d(self.shape_3d.get(), self.d3_l.get(), self.d3_w.get() or 0, self.d3_h.get() or 0)
        self.d3_res.config(text=f"Volume: {res}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PyCalcGUI(root)
    root.mainloop()