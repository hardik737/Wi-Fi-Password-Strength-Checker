import tkinter as tk
from tkinter import ttk
import re
def check_strength(pw):
    score = 0
    tips = []
    if len(pw)>=8:
        score += 1
    else:
        tips.append("use at least 8 characters.")
    if re.search(r"[A-Z]",pw):
        score += 1
    else:
        tips.append("Add at least one uppercase letter.")
    if re.search(r"[a-z]",pw):
        score += 1
    else:
        tips.append("Add at least one lowercase letter.")
    if re.search(r"\d",pw):
        score += 1
    else:
        tips.append("Add at least one digits.")
    if re.search(r"[!@#$%^&*]",pw):
        score += 1
    else:
        tips.append("Add a special symbol(!@#$%^&*).")
    common_pw = ["password", "admin", "12345678", "qwerty", "iloveyou"]
    for c in common_pw:
        if c in pw.lower():
            score = 0
            tips.append("don't use common paasword.")
            break
    if re.search(r"(.)\1\1",pw):
        tips.append("Avoid repeated characters in sequence for more security.")
    return score, tips
def update_strength(*args):
    pw = password_var.get()
    score, tips = check_strength(pw)
    if score <=2:
        strength_lbl.config(text="Weak Password", foreground="red")
        strength_bar["value"] = 20
    elif score ==3 or score ==4:
        strength_lbl.config(text="Moderate Password", foreground="orange")
        strength_bar["value"] = 60
    else:
        strength_lbl.config(text="Strong Password", foreground="green")
        strength_bar["value"] = 100
    tips_text.delete('1.0', tk.END)
    if tips:
        tips_text.insert(tk.END,"\n".join(tips))
    else:
        tips_text.insert(tk.END, "Good Job!Your password is strong.")
root = tk.Tk()
root.title("wi-fi password strength checker")
tk.Label(root,text="Enter your wi-fi password:").pack(pady=5)
password_var = tk.StringVar()
password_var.trace_add("write", update_strength)
password_entry = tk.Entry(root, textvariable=password_var,width=30,show="*")
password_entry.pack(pady=5)
strength_bar = ttk.Progressbar(root, length=200, maximum=100)
strength_bar.pack(pady=5)
strength_lbl = tk.Label(root, text="", font=("Arial", 12, "bold"))
strength_lbl.pack()
tk.Label(root,text="Tips for a strong password:").pack()
tips_text = tk.Text(root, height=5, width=50)
tips_text.pack(pady=5)
root.mainloop()

