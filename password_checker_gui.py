import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/\\|]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    errors_count = sum(errors)

    if errors_count == 0:
        return "MOCNE"
    elif errors_count <= 2:
        return "ŚREDNIE"
    else:
        return "SŁABE"

def show_result():
    password = entry.get()
    if not password:
        messagebox.showwarning("Błąd", "Wprowadź hasło.")
        return

    strength = check_password_strength(password)

    if strength == "MOCNE":
        result_label.config(text="Hasło jest MOCNE 💪", fg="green")
    elif strength == "ŚREDNIE":
        result_label.config(text="Hasło jest ŚREDNIE 😐", fg="orange")
    else:
        result_label.config(text="Hasło jest SŁABE ❌", fg="red")

# GUI Setup
root = tk.Tk()
root.title("Sprawdzacz Hasła")
root.geometry("350x200")
root.configure(bg="#1e1e2e")

label = tk.Label(root, text="Wprowadź hasło:", fg="#ffffff", bg="#1e1e2e", font=("Helvetica", 12))
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Helvetica", 12))
entry.pack()

check_button = tk.Button(root, text="Sprawdź", command=show_result, bg="#c92a2a", fg="white", font=("Helvetica", 12))
check_button.pack(pady=10)

# Funkcje do animacji przycisku
def on_enter(e):
    check_button['background'] = '#99aaff'

def on_leave(e):
    check_button['background'] = '#c92a2a'

# Podpinamy zdarzenia do przycisku
check_button.bind("<Enter>", on_enter)
check_button.bind("<Leave>", on_leave)

result_label = tk.Label(root, text="", fg="white", bg="#1e1e2e", font=("Helvetica", 12, "bold"))
result_label.pack(pady=10)


root.mainloop()
