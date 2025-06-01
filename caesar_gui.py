import tkinter as tk
from tkinter import messagebox

# Encrypt function
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isprintable():
            result += chr((ord(char) + shift) % 127)
        else:
            result += char
    return result

# Decrypt function
def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isprintable():
            result += chr((ord(char) - shift) % 127)
        else:
            result += char
    return result

# Button actions
def perform_action():
    text = entry_text.get("1.0", tk.END).strip()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Shift value must be an integer.")
        return

    if mode.get() == "Encrypt":
        result = encrypt(text, shift)
    else:
        result = decrypt(text, shift)
    
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, result)

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher GUI")

tk.Label(root, text="Enter Text:").pack()
entry_text = tk.Text(root, height=5, width=40)
entry_text.pack()

tk.Label(root, text="Shift Value:").pack()
entry_shift = tk.Entry(root)
entry_shift.pack()

mode = tk.StringVar(value="Encrypt")
tk.Radiobutton(root, text="Encrypt", variable=mode, value="Encrypt").pack()
tk.Radiobutton(root, text="Decrypt", variable=mode, value="Decrypt").pack()

tk.Button(root, text="Execute", command=perform_action).pack(pady=10)

tk.Label(root, text="Result:").pack()
result_text = tk.Text(root, height=5, width=40)
result_text.pack()

root.mainloop()
