import sqlite3
from tkinter import *
from PIL import Image, ImageTk

class UserAccountInfoApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1200x799")
        self.master.title("User Account Information")

        # Connect to SQLite database
        self.con = sqlite3.connect("final_proj")

        self.create_widgets()

    def create_widgets(self):

        # Creating the main frame
        frame = Frame(self.master, width=900, height=500, bg="#0A4F40")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label = Label(self.master, text="User Account Information", font=('serif', 25, 'bold'), bg="#C2B599")
        label.place(x=165, y=130)

        # Creating and placing the image label
        image_path = "defaultimg.png"
        image = Image.open(image_path)
        picpic = ImageTk.PhotoImage(image.resize((110, 130)))
        pics = Label(self.master)
        pics.picpic = picpic
        pics.config(image=picpic)
        pics.place(x=170, y=230)

        # Creating and placing labels and entry widgets for user data
        self.first_name_entry = self.create_label_and_entry("First Name", .26, .39)
        self.middle_name_entry = self.create_label_and_entry("Middle Name", .38, .39)
        self.last_name_entry = self.create_label_and_entry("Last Name", .51, .39)
        self.suffix_entry = self.create_label_and_entry("Suffix", .64, .39)
        self.department_entry = self.create_label_and_entry("Department", .76, .39)
        self.designation_entry = self.create_label_and_entry("Designation", .15, .50, width=40)
        self.username_entry = self.create_label_and_entry("Username", .38, .50, width=40)
        self.password_entry = self.create_label_and_entry("Password", .63, .50, width=40, show="*")
        self.confirm_password_entry = self.create_label_and_entry("Confirm Password", .15, .61, width=40, show="*")
        self.usertype_entry = self.create_label_and_entry("User Type", .38, .61, width=29)
        self.userstatus_entry = self.create_label_and_entry("User Status", .55, .61, width=26)
        self.employeenum_entry = self.create_label_and_entry("Employee Number", .70, .61, width=28)

        # Creating and placing buttons for saving, clearing, and canceling actions
        update_button = Button(self.master, text="Update", bg="#3E64DA", font=("Arial", 16), fg="#FFFFFF", width=10, command=self.save_command)
        update_button.place(relx=.36, rely=.78, anchor=CENTER)

        delete_button = Button(self.master, text="Delete", bg="#FFDB58", font=("Arial", 16), fg="#000000", width=10, command=self.clear_entry)
        delete_button.place(relx=.47, rely=.78, anchor=CENTER)

        cancel_button = Button(self.master, text="Cancel", bg="#FFFFFF", font=("Arial", 16), fg="#000000", width=10)
        cancel_button.place(relx=.58, rely=.78, anchor=CENTER)

    def create_label_and_entry(self, text, relx, rely, width=20, show=None):
        label = Label(self.master, text=text, font=(13), bg="#0A4F40", fg='#E1D7C1')
        label.place(relx=relx, rely=rely)
        entry = Entry(self.master, bg="#FFFFFF", width=width, show=show)
        entry.place(relx=relx, rely=rely+0.04)
        return entry

    def save_command(self):
        save_data_query = """
        INSERT INTO user_acc (
            first_name, mid_name, last_name, suffix, department, designation, 
            username, password, confirm_pass, usertype, user_stat, employee_number
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        data = (
            self.first_name_entry.get(), self.middle_name_entry.get(), self.last_name_entry.get(), self.suffix_entry.get(),
            self.department_entry.get(), self.designation_entry.get(), self.username_entry.get(), self.password_entry.get(),
            self.confirm_password_entry.get(), self.usertype_entry.get(), self.userstatus_entry.get(), self.employeenum_entry.get()
        )
        self.con.execute(save_data_query, data)
        self.con.commit()
        print("data saved")

    def clear_entry(self):
        self.first_name_entry.delete(0, "end")
        self.middle_name_entry.delete(0, "end")
        self.last_name_entry.delete(0, "end")
        self.suffix_entry.delete(0, "end")
        self.department_entry.delete(0, "end")
        self.designation_entry.delete(0, "end")
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        self.confirm_password_entry.delete(0, "end")
        self.usertype_entry.delete(0, "end")
        self.userstatus_entry.delete(0, "end")
        self.employeenum_entry.delete(0, "end")

if __name__ == "__main__":
    root = Tk()
    app = UserAccountInfoApp(root)
    root.mainloop()
