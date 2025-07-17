import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Weak Length", "Password length should be at least 4.")
            return

        # Define character sets
        characters = string.ascii_letters + string.digits + string.punctuation

        # Generate password
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display the password
        password_output.delete(0, tk.END)
        password_output.insert(0, password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for password length.")

# --- GUI Setup ---
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.configure(bg="#2c3e50")

# --- Widgets ---
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), fg="white", bg="#2c3e50")
title_label.pack(pady=10)

length_label = tk.Label(root, text="Enter Password Length:", font=("Arial", 12), bg="#2c3e50", fg="white")
length_label.pack()

length_entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
length_entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12), bg="#16a085", fg="white", relief=tk.RAISED)
generate_btn.pack(pady=10)

password_output = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
password_output.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 11), bg="#c0392b", fg="white")
exit_btn.pack(pady=5)

root.mainloop()
