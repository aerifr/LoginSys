import tkinter as tk
from tkinter import filedialog, CENTER
from PIL import Image, ImageTk
import sqlite3


class PayrollApp:
    def __init__(self, root):
        self.con = sqlite3.connect("final_proj")
        self.root = root
        self.root.title("SE-RI'S CHOICE PAYROLL")
        self.root.geometry('1500x900')
        self.root.configure(bg="white")

        self.create_widgets()

    def create_widgets(self):
        # Set background color
        cf1 = tk.Frame(self.root, width=800, height=1400, bg='lightgray')
        cf1.place(x=330, y=50)

        # Heading
        heading = tk.Label(self.root, text="SE-RI'S CHOICE PAYROLL", bg="lightgray", fg="black",
                           font=("Georgia", 20, "bold"))
        heading.place(relx=0.5, rely=0.03, anchor=CENTER)

        # Employee basic info
        heading1 = tk.Label(self.root, text="EMPLOYEE BASIC INFO", fg="black", font=("new times roman", 12, "bold"),
                            bg="lightgray")
        heading1.place(relx=0.25, rely=0.08)

        # Employee's image
        image_path = "defaultimg.png"
        image = Image.open(image_path)
        picpic = ImageTk.PhotoImage(image.resize((200, 150)))
        pics = tk.Label(self.root)
        pics.picpic = picpic
        pics.config(image=picpic)
        pics.place(x=370, y=100)

        # Employee Number
        self.emp_no_label = tk.Label(self.root, text="Employee Number: ", bg="lightgray")
        self.emp_no_label.place(relx=0.26, rely=0.32)
        self.emp_no_entry = tk.Entry(self.root, width=25, bg='white')
        self.emp_no_entry.place(relx=0.37, rely=0.32)

        # Search Employee
        self.search_emp_label = tk.Label(self.root, text=" Search Employee: ", bg="lightgray")
        self.search_emp_label.place(relx=0.26, rely=0.36)
        self.search_button = tk.Button(self.root, bg='#E87899', fg='black', text="SEARCH",
                                       command=lambda: self.payroll_search_command(self.emp_no_entry.get()))
        self.search_button.place(relx=0.37, rely=0.36)

        # Department
        self.dept_label = tk.Label(self.root, text="Department: ", bg="lightgray")
        self.dept_label.place(relx=0.26, rely=0.40)
        self.dept_entry = tk.Entry(self.root, width=25, bg='white')
        self.dept_entry.place(relx=0.37, rely=0.40)

        # Basic Income
        heading1 = tk.Label(self.root, text="BASIC INCOME", fg="black", font=("new times roman", 9, "bold"),
                            bg="lightgray")
        heading1.place(relx=0.25, rely=0.43)

        # Rate / hour
        self.rate_label = tk.Label(self.root, text="Rate / Hour: ", bg="lightgray")
        self.rate_label.place(relx=0.26, rely=0.46)
        self.rate_entry = tk.Entry(self.root, width=25, bg='white')
        self.rate_entry.place(relx=0.37, rely=0.46)

        # No. of Hours / Cut Off
        self.cut_off_label = tk.Label(self.root, text="No. of Hours / Cut Off: ", bg="lightgray")
        self.cut_off_label.place(relx=0.26, rely=0.50)
        self.cut_off_entry = tk.Entry(self.root, width=25, bg='white')
        self.cut_off_entry.place(relx=0.37, rely=0.50)

        # Income / Cut Off
        self.income_label = tk.Label(self.root, text="Income / Cut Off: ", bg="lightgray")
        self.income_label.place(relx=0.26, rely=0.54)
        self.income_entry = tk.Entry(self.root, width=25, bg='white')
        self.income_entry.place(relx=0.37, rely=0.54)

        # Honorarium Income
        heading2 = tk.Label(self.root, text="HONORARIUM INCOME", fg="black", font=("new times roman", 9, "bold"),
                            bg="lightgray")
        heading2.place(relx=0.25, rely=0.57)

        # Rate / hour
        self.rate1_label = tk.Label(self.root, text="Rate / Hour: ", bg="lightgray")
        self.rate1_label.place(relx=0.26, rely=0.60)
        self.rate1_entry = tk.Entry(self.root, width=25, bg='white')
        self.rate1_entry.place(relx=0.37, rely=0.60)

        # No. of Hours / Cut Off
        self.cut_off1_label = tk.Label(self.root, text="No. of Hours / Cut Off: ", bg="lightgray")
        self.cut_off1_label.place(relx=0.26, rely=0.64)
        self.cut_off1_entry = tk.Entry(self.root, width=25, bg='white')
        self.cut_off1_entry.place(relx=0.37, rely=0.64)

        # Income / Cut Off
        self.income1_label = tk.Label(self.root, text="Income / Cut Off: ", bg="lightgray")
        self.income1_label.place(relx=0.26, rely=0.68)
        self.income1_entry = tk.Entry(self.root, width=25, bg='white')
        self.income1_entry.place(relx=0.37, rely=0.68)

        # Other Income
        heading3 = tk.Label(self.root, text="OTHER INCOME", fg="black", font=("new times roman", 9, "bold"),
                            bg="lightgray")
        heading3.place(relx=0.25, rely=0.71)

        # Rate / hour
        self.rate2_label = tk.Label(self.root, text="Rate / Hour: ", bg="lightgray")
        self.rate2_label.place(relx=0.26, rely=0.74)
        self.rate2_entry = tk.Entry(self.root, width=25, bg='white')
        self.rate2_entry.place(relx=0.37, rely=0.74)

        # No. of Hours / Cut Off
        self.cut_off2_label = tk.Label(self.root, text="No. of Hours / Cut Off: ", bg="lightgray")
        self.cut_off2_label.place(relx=0.26, rely=0.78)
        self.cut_off2_entry = tk.Entry(self.root, width=25, bg='white')
        self.cut_off2_entry.place(relx=0.37, rely=0.78)

        # Income / Cut Off
        self.income2_label = tk.Label(self.root, text="Income / Cut Off: ", bg="lightgray")
        self.income2_label.place(relx=0.26, rely=0.82)
        self.income2_entry = tk.Entry(self.root, width=25, bg='white')
        self.income2_entry.place(relx=0.37, rely=0.82)

        # Summary Income
        heading4 = tk.Label(self.root, text="SUMMARY INCOME", fg="black", font=("new times roman", 9, "bold"),
                            bg="lightgray")
        heading4.place(relx=0.25, rely=0.85)

        # Gross Income
        self.gross_label = tk.Label(self.root, text="Gross Income: ", bg="lightgray")
        self.gross_label.place(relx=0.26, rely=0.88)
        self.gross_entry = tk.Entry(self.root, width=25, bg='white')
        self.gross_entry.place(relx=0.37, rely=0.88)

        # Net Income
        self.net_label = tk.Label(self.root, text="NET INCOME: ", bg="lightgray")
        self.net_label.place(relx=0.26, rely=0.92)
        self.net_entry = tk.Entry(self.root, width=25, bg='white')
        self.net_entry.place(relx=0.37, rely=0.92)

        # First name section
        self.first_name_label = tk.Label(self.root, text="First Name", bg="lightgray")
        self.first_name_label.place(relx=0.51, rely=0.10)
        self.first_name_entry = tk.Entry(self.root, width=25, bg='white')
        self.first_name_entry.place(relx=0.62, rely=0.10)

        # Middle Name
        self.middle_name_label = tk.Label(self.root, text="Middle Name", bg="lightgray")
        self.middle_name_label.place(relx=0.51, rely=0.13)
        self.middle_name_entry = tk.Entry(self.root, width=25, bg='white')
        self.middle_name_entry.place(relx=0.62, rely=0.13)

        # Surname
        self.last_name_label = tk.Label(self.root, text="Surname", bg="lightgray")
        self.last_name_label.place(relx=0.51, rely=0.16)
        self.last_name_entry = tk.Entry(self.root, width=25, bg='white')
        self.last_name_entry.place(relx=0.62, rely=0.16)

        # Civil Status
        self.civil_status_label = tk.Label(self.root, text="Civil Status", bg="lightgray")
        self.civil_status_label.place(relx=0.51, rely=0.20)
        self.civil_status_entry = tk.Entry(self.root, width=25, bg='white')
        self.civil_status_entry.place(relx=0.62, rely=0.20)

        # Quality Dep. Status
        self.qualified_label = tk.Label(self.root, text="Qualified Dep. Status", bg="lightgray")
        self.qualified_label.place(relx=0.51, rely=0.24)
        self.qualified_entry = tk.Entry(self.root, width=25, bg='white')
        self.qualified_entry.place(relx=0.62, rely=0.24)

        # Paydate
        self.paydate_label = tk.Label(self.root, text="Paydate", bg="lightgray")
        self.paydate_label.place(relx=0.51, rely=0.28)
        self.paydate_entry = tk.Entry(self.root, width=25, bg='white')
        self.paydate_entry.place(relx=0.62, rely=0.28)

        # Employee Status
        self.emp_stat_label = tk.Label(self.root, text="Employee Status:", bg="lightgray")
        self.emp_stat_label.place(relx=0.51, rely=0.33)
        self.emp_stat_entry = tk.Entry(self.root, width=25, bg='white')
        self.emp_stat_entry.place(relx=0.62, rely=0.33)

        # Designation
        self.designation_label = tk.Label(self.root, text="Designation", bg="lightgray")
        self.designation_label.place(relx=0.51, rely=0.36)
        self.designation_entry = tk.Entry(self.root, width=25, bg='white')
        self.designation_entry.place(relx=0.62, rely=0.36)

        # REGULAR DEDUCTIONS
        heading5 = tk.Label(self.root, text="REGULAR DEDUCTIONS", fg="black", font=("new times roman", 9, "bold"),
                            bg="lightgray")
        heading5.place(relx=0.50, rely=0.40)

        # SSS Contribution
        self.SSS_label = tk.Label(self.root, text="SSS Contribution:", bg="lightgray")
        self.SSS_label.place(relx=0.51, rely=0.44)
        self.SSS_entry = tk.Entry(self.root, width=25, bg='white')
        self.SSS_entry.place(relx=0.62, rely=0.44)

        # Philhealth Contribution
        self.phil_label = tk.Label(self.root, text="Philhealth Contribution:", bg="lightgray")
        self.phil_label.place(relx=0.51, rely=0.47)
        self.phil_entry = tk.Entry(self.root, width=25, bg='white')
        self.phil_entry.place(relx=0.62, rely=0.47)

        # Pagibig Contribution
        self.pagibig_label = tk.Label(self.root, text="Pagibig Contribution:", bg="lightgray")
        self.pagibig_label.place(relx=0.51, rely=0.50)
        self.pagibig_entry = tk.Entry(self.root, width=25, bg='white')
        self.pagibig_entry.place(relx=0.62, rely=0.50)

        # Income Tax Contribution
        self.tax_label = tk.Label(self.root, text="Income Tax Contribution:", bg="lightgray")
        self.tax_label.place(relx=0.51, rely=0.53)
        self.tax_entry = tk.Entry(self.root, width=25, bg='white')
        self.tax_entry.place(relx=0.62, rely=0.53)

        # OTHER DEDUCTIONS
        heading6 = tk.Label(self.root, text="OTHER DEDUCTIONS", fg="black", font=("new times roman", 9, "bold"),
                            bg="lightgray")
        heading6.place(relx=0.50, rely=0.58)

        # SSS Loan
        self.sss_loan_label = tk.Label(self.root, text="SSS Loan:", bg="lightgray")
        self.sss_loan_label.place(relx=0.51, rely=0.62)
        self.sss_loan_entry = tk.Entry(self.root, width=25, bg='white')
        self.sss_loan_entry.place(relx=0.62, rely=0.62)

        # Pagibig Loan
        self.pagibig_loan_label = tk.Label(self.root, text="Pagibig Loan:", bg="lightgray")
        self.pagibig_loan_label.place(relx=0.51, rely=0.65)
        self.pagibig_loan_entry = tk.Entry(self.root, width=25, bg='white')
        self.pagibig_loan_entry.place(relx=0.62, rely=0.65)

        # Faculty Savings Deposit
        self.faculty_deposit_label = tk.Label(self.root, text="Faculty Savings Deposit:", bg="lightgray")
        self.faculty_deposit_label.place(relx=0.51, rely=0.68)
        self.faculty_deposit_entry = tk.Entry(self.root, width=25, bg='white')
        self.faculty_deposit_entry.place(relx=0.62, rely=0.68)

        # Faculty Savings Loan
        self.faculty_loan_label = tk.Label(self.root, text="Faculty Savings Loan:", bg="lightgray")
        self.faculty_loan_label.place(relx=0.51, rely=0.71)
        self.faculty_loan_entry = tk.Entry(self.root, width=25, bg='white')
        self.faculty_loan_entry.place(relx=0.62, rely=0.71)

        # Salary Loan
        self.salary_loan_label = tk.Label(self.root, text="Salary Loan:", bg="lightgray")
        self.salary_loan_label.place(relx=0.51, rely=0.74)
        self.salary_loan_entry = tk.Entry(self.root, width=25, bg='white')
        self.salary_loan_entry.place(relx=0.62, rely=0.74)

        # Other Loans
        self.other_loan_label = tk.Label(self.root, text="Other Loans:", bg="lightgray")
        self.other_loan_label.place(relx=0.51, rely=0.78)
        self.other_loan_entry = tk.Entry(self.root, width=25, bg='white')
        self.other_loan_entry.place(relx=0.62, rely=0.78)

        # DEDUCTIONS SUMMARY
        heading7 = tk.Label(self.root, text="DEDUCTIONS SUMMARY", fg="black", font=("new times roman", 9, "bold"),
                            bg="lightgray")
        heading7.place(relx=0.50, rely=0.83)

        # Total Deductions
        self.total_label = tk.Label(self.root, text="Total Deductions:", bg="lightgray")
        self.total_label.place(relx=0.51, rely=0.87)
        self.total_loan_entry = tk.Entry(self.root, width=25, bg='white')
        self.total_loan_entry.place(relx=0.62, rely=0.87)

        # BUTTONS
        self.gross_button = tk.Button(self.root, bg='#24438D', fg='white', text="GROSS INCOME",
                                      command=self.calculate_gross_income)
        self.gross_button.place(relx=0.50, rely=0.91)
        self.net_button = tk.Button(self.root, bg='#39248D', fg='white', text="NET INCOME",
                                    command=self.calculate_net_income)
        self.net_button.place(relx=0.57, rely=0.91)
        self.save_button = tk.Button(self.root, bg='#6E248D', fg='white', text="SAVE", command=self.payroll_save)
        self.save_button.place(relx=0.63, rely=0.91)
        self.update_button = tk.Button(self.root, bg='#8D2478', fg='white', text="UPDATE", command=self.update_data)
        self.update_button.place(relx=0.66, rely=0.91)
        self.new_button = tk.Button(self.root, bg='#8D3924', fg='white', text="NEW", command=self.new_entries)
        self.new_button.place(relx=0.70, rely=0.91)

    def payroll_save(self):
        payroll_save_query = """
        INSERT INTO payroll_tbl (
            empNum, deparment, rate, cutoff, income, rate1, cutoff1, income1, rate2, 
            cutoff2, income2, gross_income, net_income, first_name, middle_name, last_name, civil_stat, qualified, 
            paydate, employee_stat, designation, sss_contribution, philhealth, pagibigcon, tax, sssloan, 
            pagibigloan, faculty_dep, faculty_loan, salary, otherloan, total_deduction
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        data = (
            self.emp_no_entry.get(), self.dept_entry.get(), self.rate_entry.get(), self.cut_off_entry.get(),
            self.income_entry.get(),
            self.rate1_entry.get(), self.cut_off1_entry.get(), self.income1_entry.get(), self.rate2_entry.get(),
            self.cut_off2_entry.get(),
            self.income2_entry.get(), self.gross_entry.get(), self.net_entry.get(), self.first_name_entry.get(),
            self.middle_name_entry.get(),
            self.last_name_entry.get(), self.civil_status_entry.get(), self.qualified_entry.get(),
            self.paydate_entry.get(),
            self.emp_stat_entry.get(), self.designation_entry.get(), self.SSS_entry.get(), self.phil_entry.get(),
            self.pagibig_entry.get(),
            self.tax_entry.get(), self.sss_loan_entry.get(), self.pagibig_loan_entry.get(),
            self.faculty_deposit_entry.get(),
            self.faculty_loan_entry.get(), self.salary_loan_entry.get(), self.other_loan_entry.get(),
            self.total_loan_entry.get()
        )
        self.con.execute(payroll_save_query, data)
        self.con.commit()
        print("data saved")

    def calculate_gross_income(self):
        try:
            rate_per_hour = float(self.rate_entry.get())
            cut_off = float(self.cut_off_entry.get())
            rate_per_hour1 = float(self.rate1_entry.get())
            cut_off1 = float(self.cut_off1_entry.get())
            rate_per_hour2 = float(self.rate2_entry.get())
            cut_off2 = float(self.cut_off2_entry.get())
            income = float(self.income_entry.get())
            income1 = float(self.income1_entry.get())
            income2 = float(self.income2_entry.get())
            basic = rate_per_hour * cut_off / income
            honor = rate_per_hour1 * cut_off1 / income1
            other = rate_per_hour2 * cut_off2 / income2
            gross_income = basic + honor + other
            self.gross_entry.delete(0, tk.END)
            self.gross_entry.insert(0, gross_income)
        except ValueError:
            print("Please enter valid numbers for the rate and cutoff fields.")

    def calculate_net_income(self):
        try:
            gross_income = float(self.gross_entry.get())
            total_deduction = float(self.total_loan_entry.get())
            net_income = gross_income - total_deduction
            self.net_entry.delete(0, tk.END)
            self.net_entry.insert(0, net_income)
        except ValueError:
            print("Please enter valid numbers for the gross income and total deduction fields.")

    def update_data(self):
        employee_number = self.emp_no_entry.get()
        if employee_number:
            self.con = sqlite3.connect("second_db")
            cur = self.con.cursor()
            cur.execute("SELECT * FROM payroll_tbl WHERE empNum=?", (employee_number,))
            if cur.fetchone():
                payroll_update_query = """
                UPDATE payroll_tbl
                SET dept=?, rate=?, cutoff=?, income=?, rate1=?, cutoff1=?, income1=?, rate2=?, cutoff2=?, income2=?, gross=?, net=?, fname=?, mname=?, lname=?, civstat=?, qualified=?, paydate=?, empstat=?, desig=?, ssscon=?, phil=?, pagibigcon=?, tax=?, sssloan=?, pagibigloan=?, facdep=?, facloan=?, salary=?, otherloan=?, totalded=?
                WHERE empNum=?
                """
                data = (
                    self.dept_entry.get(), self.rate_entry.get(), self.cut_off_entry.get(), self.income_entry.get(),
                    self.rate1_entry.get(), self.cut_off1_entry.get(),
                    self.income1_entry.get(), self.rate2_entry.get(), self.cut_off2_entry.get(),
                    self.income2_entry.get(), self.gross_entry.get(), self.net_entry.get(),
                    self.first_name_entry.get(), self.middle_name_entry.get(), self.last_name_entry.get(),
                    self.civil_status_entry.get(), self.qualified_entry.get(),
                    self.paydate_entry.get(), self.emp_stat_entry.get(), self.designation_entry.get(),
                    self.SSS_entry.get(), self.phil_entry.get(), self.pagibig_entry.get(),
                    self.tax_entry.get(), self.sss_loan_entry.get(), self.pagibig_loan_entry.get(),
                    self.faculty_deposit_entry.get(), self.faculty_loan_entry.get(),
                    self.salary_loan_entry.get(), self.other_loan_entry.get(), self.total_loan_entry.get(),
                    employee_number
                )
                self.con.execute(payroll_update_query, data)
                self.con.commit()
                print("Employee information has been updated successfully!")
            else:
                print("Employee ID not located!")
            self.con.close()
        else:
            print("Please enter an employee number.")

    def new_entries(self):
        # Clear all entry fields
        self.emp_no_entry.delete(0, tk.END)
        self.dept_entry.delete(0, tk.END)
        self.rate_entry.delete(0, tk.END)
        self.cut_off_entry.delete(0, tk.END)
        self.income_entry.delete(0, tk.END)
        self.rate1_entry.delete(0, tk.END)
        self.cut_off1_entry.delete(0, tk.END)
        self.income1_entry.delete(0, tk.END)
        self.rate2_entry.delete(0, tk.END)
        self.cut_off2_entry.delete(0, tk.END)
        self.income2_entry.delete(0, tk.END)
        self.gross_entry.delete(0, tk.END)
        self.net_entry.delete(0, tk.END)
        self.first_name_entry.delete(0, tk.END)
        self.middle_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.civil_status_entry.delete(0, tk.END)
        self.qualified_entry.delete(0, tk.END)
        self.paydate_entry.delete(0, tk.END)
        self.emp_stat_entry.delete(0, tk.END)
        self.designation_entry.delete(0, tk.END)
        self.SSS_entry.delete(0, tk.END)
        self.phil_entry.delete(0, tk.END)
        self.pagibig_entry.delete(0, tk.END)
        self.tax_entry.delete(0, tk.END)
        self.sss_loan_entry.delete(0, tk.END)
        self.pagibig_loan_entry.delete(0, tk.END)
        self.faculty_deposit_entry.delete(0, tk.END)
        self.faculty_loan_entry.delete(0, tk.END)
        self.salary_loan_entry.delete(0, tk.END)
        self.other_loan_entry.delete(0, tk.END)
        self.total_loan_entry.delete(0, tk.END)

    def payroll_search_command(self, payroll_tbl):
        con = sqlite3.connect("final_proj")
        cur = con.cursor()
        search_query = """
        SELECT deparment, rate, cutoff, income, rate1, cutoff1, income1, rate2, 
            cutoff2, income2, gross_income, net_income, first_name, middle_name, last_name, civil_stat, qualified, 
            paydate, employee_stat, designation, sss_contribution, philhealth, pagibigcon, tax, sssloan, 
            pagibigloan, faculty_dep, faculty_loan, salary, otherloan, total_deduction
        FROM payroll_tbl
        WHERE empNum = ?
        """
        cur.execute(search_query, (payroll_tbl,))
        result = cur.fetchone()
        if result:
            self.first_name_entry.delete(0, 'end')
            self.first_name_entry.insert(0, result[0])
            self.middle_name_entry.delete(0, 'end')
            self.middle_name_entry.insert(0, result[1])
            self.last_name_entry.delete(0, 'end')
            self.last_name_entry.insert(0, result[2])
            self.dept_entry.delete(0, 'end')
            self.dept_entry.insert(0, result[3])
            self.designation_entry.delete(0, 'end')
            self.designation_entry.insert(0, result[4])
            self.rate_entry.delete(0, 'end')
            self.rate_entry.insert(0, result[5])
            self.cut_off_entry.delete(0, 'end')
            self.cut_off_entry.insert(0, result[6])
            self.income_entry.delete(0, 'end')
            self.income_entry.insert(0, result[7])
            self.rate1_entry.delete(0, 'end')
            self.rate1_entry.insert(0, result[8])
            self.cut_off1_entry.delete(0, 'end')
            self.cut_off1_entry.insert(0, result[9])
            self.income1_entry.delete(0, 'end')
            self.income1_entry.insert(0, result[10])
            self.rate2_entry.delete(0, 'end')
            self.rate2_entry.insert(0, result[11])
            self.cut_off2_entry.delete(0, 'end')
            self.cut_off2_entry.insert(0, result[12])
            self.income2_entry.delete(0, 'end')
            self.income2_entry.insert(0, result[13])
            self.gross_entry.delete(0, 'end')
            self.gross_entry.insert(0, result[14])
            self.net_entry.delete(0, 'end')
            self.net_entry.insert(0, result[15])
            self.civil_status_entry.delete(0, 'end')
            self.civil_status_entry.insert(0, result[16])
            self.qualified_entry.delete(0, 'end')
            self.qualified_entry.insert(0, result[17])
            self.paydate_entry.delete(0, 'end')
            self.paydate_entry.insert(0, result[18])
            self.emp_stat_entry.delete(0, 'end')
            self.emp_stat_entry.insert(0, result[19])
            self.SSS_entry.delete(0, 'end')
            self.SSS_entry.insert(0, result[20])
            self.phil_entry.delete(0, 'end')
            self.phil_entry.insert(0, result[21])
            self.pagibig_entry.delete(0, 'end')
            self.pagibig_entry.insert(0, result[22])
            self.tax_entry.delete(0, 'end')
            self.tax_entry.insert(0, result[23])
            self.sss_loan_entry.delete(0, 'end')
            self.sss_loan_entry.insert(0, result[24])
            self.pagibig_loan_entry.delete(0, 'end')
            self.pagibig_loan_entry.insert(0, result[25])
            self.faculty_deposit_entry.delete(0, 'end')
            self.faculty_deposit_entry.insert(0, result[26])
            self.faculty_loan_entry.delete(0, 'end')
            self.faculty_loan_entry.insert(0, result[27])
            self.salary_loan_entry.delete(0, 'end')
            self.salary_loan_entry.insert(0, result[28])
            self.other_loan_entry.delete(0, 'end')
            self.other_loan_entry.insert(0, result[29])
            self.total_loan_entry.delete(0, 'end')
            self.total_loan_entry.insert(0, result[30])
        else:
            print("Employee not found")
        con.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = PayrollApp(root)
    root.mainloop()
