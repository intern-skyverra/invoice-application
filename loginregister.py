import requests
import tkinter as tk
from tkinter import messagebox


class AuthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice Application")
        self.root.geometry("450x600")
        self.root.configure(bg="#f5f5f5")

        self.show_login()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ---------------- LOGIN PAGE ----------------
    def show_login(self):
        self.clear_window()

        tk.Label(
            self.root,
            text="Welcome Back",
            font=("Georgia", 22, "bold"),
            bg="#f5f5f5"
        ).pack(pady=20)

        tk.Label(self.root, text="Email", bg="#f5f5f5").pack()
        self.login_email = tk.Entry(self.root, width=35)
        self.login_email.pack(pady=5)

        tk.Label(self.root, text="Password", bg="#f5f5f5").pack()
        self.login_password = tk.Entry(self.root, show="*", width=35)
        self.login_password.pack(pady=5)

        tk.Button(
            self.root,
            text="Sign In",
            bg="#5551f1",
            fg="white",
            width=25,
            command=self.login
        ).pack(pady=20)

        tk.Label(self.root, text="Don't have an account?", bg="#f5f5f5").pack()

        tk.Button(
            self.root,
            text="Create One",
            fg="#5551f1",
            command=self.show_register
        ).pack()

    # ---------------- REGISTER PAGE ----------------
    def show_register(self):
        self.clear_window()

        tk.Label(
            self.root,
            text="Create Account",
            font=("Georgia", 22, "bold"),
            bg="#f5f5f5"
        ).pack(pady=20)

        tk.Label(self.root, text="Full Name", bg="#f5f5f5").pack()
        self.reg_name = tk.Entry(self.root, width=35)
        self.reg_name.pack(pady=5)

        tk.Label(self.root, text="Email", bg="#f5f5f5").pack()
        self.reg_email = tk.Entry(self.root, width=35)
        self.reg_email.pack(pady=5)

        tk.Label(self.root, text="Password", bg="#f5f5f5").pack()
        self.reg_password = tk.Entry(self.root, show="*", width=35)
        self.reg_password.pack(pady=5)

        tk.Label(self.root, text="Confirm Password", bg="#f5f5f5").pack()
        self.reg_confirm = tk.Entry(self.root, show="*", width=35)
        self.reg_confirm.pack(pady=5)

        self.terms_var = tk.IntVar()

        tk.Checkbutton(
            self.root,
            text="I agree to Terms & Conditions",
            variable=self.terms_var,
            bg="#f5f5f5"
        ).pack(pady=10)

        tk.Button(
            self.root,
            text="Create Account",
            bg="#5551f1",
            fg="white",
            width=25,
            command=self.register
        ).pack(pady=20)

        tk.Label(self.root, text="Already have an account?", bg="#f5f5f5").pack()

        tk.Button(
            self.root,
            text="Sign In",
            fg="#5551f1",
            command=self.show_login
        ).pack()

    # ---------------- ACTIONS ----------------
    def login(self):
        email = self.login_email.get()
        password = self.login_password.get()

        try:
            response = requests.post(
                "http://localhost:5000/api/auth/login",
                json={
                    "email": email,
                    "password": password
                }
            )

            data = response.json()

            if response.status_code == 200:

                token = data["token"]

                with open("token.txt", "w") as file:
                    file.write(token)

                messagebox.showinfo(
                    "Success",
                    "Login Successful"
                )

            else:
                messagebox.showerror(
                    "Error",
                    data.get("message")
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )
            
    def register(self):
        name = self.reg_name.get()
        email = self.reg_email.get()
        password = self.reg_password.get()
        confirm = self.reg_confirm.get()

        if not all([name, email, password, confirm]):
            messagebox.showerror("Error", "Please fill all fields")
            return

        if password != confirm:
            messagebox.showerror("Error", "Passwords do not match")
            return

        if not self.terms_var.get():
            messagebox.showerror("Error", "Accept Terms & Conditions")
            return

        try:
            response = requests.post(
                "http://localhost:5000/api/auth/signup",
                json={
                    "fullName": name,
                    "email": email,
                    "password": password
                }
            )

            data = response.json()

            if response.status_code == 201:
                messagebox.showinfo(
                    "Success",
                    "Registration Successful"
                )

                self.show_login()

            else:
                messagebox.showerror(
                    "Error",
                    data.get("message")
                )

        except Exception as e:
            messagebox.showerror(
                "Error",
                str(e)
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = AuthApp(root)
    root.mainloop()