import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("350x300")
        self.root.config(bg="#f0f8ff")

        # Title Label
        tk.Label(root, text="🧮 Simple Calculator", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#333").pack(pady=10)

        # Input Fields
        input_frame = tk.Frame(root, bg="#f0f8ff")
        input_frame.pack(pady=5)

        tk.Label(input_frame, text="Enter first number:", bg="#f0f8ff", font=("Arial", 10)).grid(row=0, column=0, pady=5, sticky='w')
        self.num1_entry = tk.Entry(input_frame, width=20, font=("Arial", 12))
        self.num1_entry.grid(row=0, column=1, pady=5)

        tk.Label(input_frame, text="Enter second number:", bg="#f0f8ff", font=("Arial", 10)).grid(row=1, column=0, pady=5, sticky='w')
        self.num2_entry = tk.Entry(input_frame, width=20, font=("Arial", 12))
        self.num2_entry.grid(row=1, column=1, pady=5)

        # Buttons
        button_frame = tk.Frame(root, bg="#f0f8ff")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="➕ Add", width=8, command=self.add, bg="#90ee90").grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="➖ Sub", width=8, command=self.subtract, bg="#ffd700").grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="✖ Mul", width=8, command=self.multiply, bg="#add8e6").grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="➗ Div", width=8, command=self.divide, bg="#ffb6c1").grid(row=0, column=3, padx=5)

        # Result Display
        self.result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f8ff", fg="#333")
        self.result_label.pack(pady=15)

        # Exit Button
        tk.Button(root, text="❌ Exit", command=root.destroy, bg="#d9534f", fg="white", width=15).pack(pady=5)

    def get_numbers(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return None, None

    def add(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            self.result_label.config(text=f"Result: {num1 + num2}")

    def subtract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            self.result_label.config(text=f"Result: {num1 - num2}")

    def multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            self.result_label.config(text=f"Result: {num1 * num2}")

    def divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            if num2 == 0:
                messagebox.showerror("Math Error", "Cannot divide by zero.")
            else:
                self.result_label.config(text=f"Result: {num1 / num2:.2f}")

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
