import tkinter as tk
from tkinter import ttk

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            if mode == "Encrypt":
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char
    return result

def process_text(*args):
    try:
        shift = int(shift_entry.get())
        mode = mode_var.get()
        input_text = input_box.get("1.0", tk.END).strip()
        result = caesar_cipher(input_text, shift, mode)
        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)
        output_box.config(state=tk.DISABLED)
    except ValueError:
        output_box.config(state=tk.NORMAL)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, "Please enter a valid number for shift.")
        output_box.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Caesar Cipher - Elegant Dark Theme")
root.geometry("600x500")
root.configure(bg="#121212")

# Custom Styling
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel",
                background="#121212",
                foreground="#ffffff",
                font=("Segoe UI", 12))

style.configure("TEntry",
                fieldbackground="#1e1e1e",
                foreground="#ffffff",
                background="#1e1e1e",
                borderwidth=1,
                relief="flat")

style.configure("TButton",
                background="#333333",
                foreground="#ffffff",
                font=("Segoe UI", 11),
                borderwidth=0)

style.map("TButton",
          background=[("active", "#444444")])

# Radiobutton Style
style.configure("Dark.TRadiobutton",
                background="#121212",
                foreground="#ffffff",
                font=("Segoe UI", 11),
                indicatorcolor="#00ffff",
                indicatormargin=6,
                focuscolor="#121212",
                relief="flat")

style.map("Dark.TRadiobutton",
          background=[("active", "#121212")],
          foreground=[("active", "#ffffff")])

# Shift Entry
label_shift = ttk.Label(root, text="Enter Shift:")
label_shift.pack(pady=(15, 5))

shift_entry = ttk.Entry(root, width=10)
shift_entry.pack(pady=5)
shift_entry.bind("<KeyRelease>", process_text)

# Mode selection
mode_var = tk.StringVar(value="Encrypt")
frame_mode = tk.Frame(root, bg="#121212")
frame_mode.pack(pady=10)

ttk.Radiobutton(frame_mode, text="Encrypt", variable=mode_var, value="Encrypt", style="Dark.TRadiobutton", command=process_text).pack(side="left", padx=10)
ttk.Radiobutton(frame_mode, text="Decrypt", variable=mode_var, value="Decrypt", style="Dark.TRadiobutton", command=process_text).pack(side="left", padx=10)

# Input Text
label_input = ttk.Label(root, text="Enter Text:")
label_input.pack(pady=(20, 5))

input_box = tk.Text(root, height=6, width=60, bg="#1e1e1e", fg="#ffffff", insertbackground="white", font=("Segoe UI", 11), wrap="word", relief="flat")
input_box.pack(pady=5)
input_box.bind("<KeyRelease>", process_text)

# Output Text
label_output = ttk.Label(root, text="Result:")
label_output.pack(pady=(20, 5))

output_box = tk.Text(root, height=6, width=60, bg="#1e1e1e", fg="#00ffcc", font=("Segoe UI", 11), state=tk.DISABLED, wrap="word", relief="flat")
output_box.pack(pady=5)

root.mainloop()