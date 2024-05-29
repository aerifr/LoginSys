import tkinter as tk
from tkinter import messagebox
import sqlite3
import PERSONALinfo
import payroll
import USERinfo

# Database setup
def setup_database():
    conn = sqlite3.connect('final_proj.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS final (username TEXT PRIMARY KEY, password INTEGER)''')
    conn.commit()
    conn.close()

setup_database()

class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Login System")
        self.master.geometry("1200x700")
        self.master.configure(bg='#242363')

        self.label1 = tk.Label(self.master, text='Login System', bg='#242363', fg='#faaf40',
                               font=('Times New Roman', 30))
        self.label1.place(x=500, y=30)

        self.label2 = tk.Label(self.master, text='Username :', font=('Arial', 20, 'bold'), bg='#242363', fg='#faaf40')
        self.label2.place(x=310, y=190)

        self.label3 = tk.Label(self.master, text='Password :', font=('Arial', 20, 'bold'), bg='#242363', fg='#faaf40')
        self.label3.place(x=310, y=340)

        self.entry1 = tk.Entry(self.master, font=('Arial', 15))
        self.entry1.place(x=600, y=200)

        self.entry2 = tk.Entry(self.master, font=('Arial', 15), show='*')
        self.entry2.place(x=600, y=350)

        self.button = tk.Button(self.master, text='Login', bg='#faaf40', font=('Arial', 15), bd=5, fg='white',
                                command=self.login)
        self.button.place(x=680, y=450)

        self.signup_button = tk.Button(self.master, text='Click to Sign Up', bg='#242363', font=('Arial', 15), bd=3,
                                       fg='white', command=self.open_signup)
        self.signup_button.place(x=640, y=500)

    def login(self):
        username = self.entry1.get()
        password = self.entry2.get()

        conn = sqlite3.connect('final_proj.db')
        c = conn.cursor()
        c.execute("SELECT * FROM final WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        conn.close()

        print(f"Login attempt: username={username}, password={password}, result={result}")

        if result:
            messagebox.showinfo("Login Success", "Welcome!")
            self.master.withdraw()
            self.open_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")

    def open_menu(self):
        self.menu_window = tk.Toplevel(self.master)
        self.menu_window.configure(bg='#f9af52')

        button1 = tk.Button(self.menu_window, text='Employee Registration', bg='#544c84', fg='white',
                            font=('Arial', 15), bd=5,
                            command=self.open_employee_regis)
        button1.pack(pady=20)

        button2 = tk.Button(self.menu_window, text='Payroll', bg='#544c84', fg='white', font=('Arial', 15), bd=5,
                            command=self.open_payroll)
        button2.pack(pady=20)

        button3 = tk.Button(self.menu_window, text='User Info', bg='#544c84', fg='white', font=('Arial', 15), bd=5,
                            command=self.open_user_info)
        button3.pack(pady=20)

    def open_employee_regis(self):
        self.master.withdraw()
        employee_window = tk.Toplevel(self.master)
        PERSONALinfo.EmployeeInfo(employee_window)

    def open_payroll(self):
        self.master.withdraw()
        payroll_window = tk.Toplevel(self.master)
        payroll.PayrollApp(payroll_window)

    def open_user_info(self):
        self.master.withdraw()
        user_info_window = tk.Toplevel(self.master)
        USERinfo.UserAccountInfoApp(user_info_window)

    def open_signup(self):
        self.signup_window = tk.Toplevel(self.master)
        SignUpApp(self.signup_window)


class SignUpApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sign Up")
        self.master.geometry("500x400")
        self.master.configure(bg='#242363')

        self.sgnlabel = tk.Label(self.master, text='Sign Up', bg='#242363', fg='#faaf40', font=('Times New Roman', 30))
        self.sgnlabel.pack(pady=20)

        self.userlabel = tk.Label(self.master, text='Username :', font=('Arial', 15, 'bold'), bg='#242363', fg='#faaf40')
        self.userlabel.pack(pady=5)

        self.username = tk.Entry(self.master, font=('Arial', 15))
        self.username.pack(pady=5)

        self.pwlabel = tk.Label(self.master, text='Password :', font=('Arial', 15, 'bold'), bg='#242363', fg='#faaf40')
        self.pwlabel.pack(pady=5)

        self.password = tk.Entry(self.master, font=('Arial', 15), show='*')
        self.password.pack(pady=5)

        self.button = tk.Button(self.master, text='Sign Up', bg='#faaf40', font=('Arial', 15), bd=5, fg='white',
                                command=self.signup)
        self.button.pack(pady=20)

    def signup(self):
        username = self.username.get()
        password = self.password.get()

        if not username or not password:
            messagebox.showerror("Error", "Please fill out all the fields.")
            return

        conn = sqlite3.connect('final_proj.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS final (username TEXT PRIMARY KEY, password TEXT)''')

        c.execute("SELECT * FROM final WHERE username=?", (username,))
        existing_user = c.fetchone()

        print(f"Sign up attempt: username={username}, password={password}, existing_user={existing_user}")

        if existing_user:
            messagebox.showerror("Error", "The username is already taken. Please choose another one.")
            conn.close()
            return

        c.execute("INSERT INTO final (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)

        messagebox.showinfo("Success", "Sign up successful!")
        self.master.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
