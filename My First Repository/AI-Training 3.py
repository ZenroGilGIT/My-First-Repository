import tkinter as tk
from tkinter import messagebox

def calculate_beam():
    try:
        # Inputs
        w = float(entry_w.get())          # kN/m
        L = float(entry_L.get())          # m
        b = float(entry_b.get())          # mm
        d = float(entry_d.get())          # mm
        fck = float(entry_fck.get())      # MPa
        fy = float(entry_fy.get())        # MPa

        # Convert units
        Mu = (w * L**2) / 8               # kN·m
        Mu_Nmm = Mu * 10**6               # convert to Nmm

        # Steel calculation
        j = 0.9
        As = Mu_Nmm / (0.87 * fy * j * d)

        # Minimum steel (IS style approx)
        As_min = 0.85 * b * d / fy

        # Results
        result_text = f"""
Maximum Moment (Mu): {Mu:.2f} kN·m
Required Steel Area (As): {As:.2f} mm²
Minimum Steel Area: {As_min:.2f} mm²
"""

        if As < As_min:
            result_text += "\n⚠ Use Minimum Steel Area"

        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# GUI Window
root = tk.Tk()
root.title("RC Beam Designer")
root.geometry("450x500")

tk.Label(root, text="Reinforced Concrete Beam Designer",
         font=("Arial", 14, "bold")).pack(pady=10)

# Inputs
fields = [
    ("Uniform Load w (kN/m):", "entry_w"),
    ("Span L (m):", "entry_L"),
    ("Beam Width b (mm):", "entry_b"),
    ("Effective Depth d (mm):", "entry_d"),
    ("Concrete Strength fck (MPa):", "entry_fck"),
    ("Steel Yield Strength fy (MPa):", "entry_fy")
]

entries = {}

for label_text, var_name in fields:
    tk.Label(root, text=label_text).pack()
    entry = tk.Entry(root)
    entry.pack()
    entries[var_name] = entry

entry_w = entries["entry_w"]
entry_L = entries["entry_L"]
entry_b = entries["entry_b"]
entry_d = entries["entry_d"]
entry_fck = entries["entry_fck"]
entry_fy = entries["entry_fy"]

tk.Button(root, text="Design Beam",
          command=calculate_beam,
          bg="green", fg="white").pack(pady=15)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()