import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3

# Connect to SQLite database
con = sqlite3.connect("final_proj")

# Create main window
window = tk.Tk()


# Start of Employee Information
class EmployeeInfo:
    def __init__(self, window):
        self.window = window
        self.window.title("personal info")
        self.window.geometry('700x900')

        # Main frame
        boxbox = tk.Frame(window, bg='#E4E1E1', width=1500, height=1500)
        boxbox.place(x=0.01, y=50)

        # Code for Image
        image_path = "defaultimg.png"
        image = Image.open(image_path)
        picpic = ImageTk.PhotoImage(image.resize((100, 90)))
        pics = tk.Label(self.window)
        pics.picpic = picpic
        pics.config(image=picpic)
        pics.place(x=40, y=100)

        # Text for Employee's Information
        serip = tk.Label(window, text="SE-RI'S EMPLOYEE PERSONAL INFORMATION", font=('impact', 23, 'bold'))
        serip.place(x=60, y=5)

        # Labels and Entries
        self.FirstN_label = tk.Label(window, text="First Name", font=('Times New Roman', 8), bg="#E4E1E1")
        self.FirstN_label.place(x=165, y=110)
        self.FirstN_entry = tk.Entry(window, width=17)
        self.FirstN_entry.place(x=165, y=130)

        self.MiddleN_label = tk.Label(window, text="Middle Name", font=('Times New Roman', 8), bg="#E4E1E1")
        self.MiddleN_label.place(x=275, y=110)
        self.MiddleN_entry = tk.Entry(window, width=17)
        self.MiddleN_entry.place(x=275, y=130)

        self.LastN_label = tk.Label(window, text="Last Name", font=('Times New Roman', 8), bg="#E4E1E1")
        self.LastN_label.place(x=385, y=110)
        self.LastN_entry = tk.Entry(window, width=17)
        self.LastN_entry.place(x=385, y=130)

        self.Suffix_label = tk.Label(window, text="Suffix", font=('Times New Roman', 8), bg="#E4E1E1")
        self.Suffix_label.place(x=500, y=110)
        self.Suffix_entry = tk.Entry(window, width=10)
        self.Suffix_entry.place(x=500, y=130)

        self.Choose_button = tk.Button(window, text="Choose File", font=('Times New Roman', 8), bg="#E4E1E1", width=10)
        self.Choose_button.place(x=60, y=200)

        self.DateOfBirth_label = tk.Label(window, text="Date of Birth", font=('Times New Roman', 8), bg="#E4E1E1")
        self.DateOfBirth_label.place(x=165, y=165)
        self.DateOfBirth_entry = tk.Entry(window, width=21)
        self.DateOfBirth_entry.place(x=165, y=185)

        self.Gender_label = tk.Label(window, text="Gender", font=('Times New Roman', 8), bg="#E4E1E1")
        self.Gender_label.place(x=298, y=165)
        self.Gender_entry = tk.Entry(window, width=18)
        self.Gender_entry.place(x=298, y=185)

        self.Nationality_label = tk.Label(window, text="Nationality", font=('Times New Roman', 8), bg="#E4E1E1")
        self.Nationality_label.place(x=415, y=165)
        self.Nationality_entry = tk.Entry(window, width=10)
        self.Nationality_entry.place(x=415, y=185)

        self.CivilStatus_label = tk.Label(window, text="Civil Status", font=('Times New Roman', 8), bg="#E4E1E1")
        self.CivilStatus_label.place(x=480, y=165)
        self.CivilStatus_entry = tk.Entry(window, width=14)
        self.CivilStatus_entry.place(x=485, y=185)

        self.Department_label = tk.Label(window, text="Department", font=('Times New Roman', 8), bg="#E4E1E1")
        self.Department_label.place(x=50, y=265)
        self.Department_entry = tk.Entry(window, width=38)
        self.Department_entry.place(x=50, y=285)

        self.EmployeeStatus_label = tk.Label(window, text="Employee Status", font=('Times New Roman', 8), bg="#E4E1E1")
        self.EmployeeStatus_label.place(x=50, y=310)
        self.EmployeeStatus_entry = tk.Entry(window, width=46)
        self.EmployeeStatus_entry.place(x=50, y=330)

        self.Designation_label = tk.Label(window, text="Designation", font=('Times New Roman', 8), bg="#E4E1E1")
        self.Designation_label.place(x=295, y=265)
        self.Designation_entry = tk.Entry(window, width=25)
        self.Designation_entry.place(x=295, y=285)

        self.QualifiedStatus_label = tk.Label(window, text="Qualified Dept Status", font=('Times New Roman', 8),
                                              bg="#E4E1E1")
        self.QualifiedStatus_label.place(x=450, y=265)
        self.QualifiedStatus_entry = tk.Entry(window, width=18)
        self.QualifiedStatus_entry.place(x=455, y=285)

        self.Paydate_label = tk.Label(window, text="Pay date", font=('Times New Roman', 8), bg="#E4E1E1")
        self.Paydate_label.place(x=345, y=310)
        self.Paydate_entry = tk.Entry(window, width=15)
        self.Paydate_entry.place(x=345, y=330)

        self.EmployeeNumber_label = tk.Label(window, text="Employee Number", font=('Times New Roman', 8), bg="#E4E1E1")
        self.EmployeeNumber_label.place(x=445, y=310)
        self.EmployeeNumber_entry = tk.Entry(window, width=20)
        self.EmployeeNumber_entry.place(x=445, y=330)

        self.ContactInfo_label = tk.Label(window, text="Contact Info", font=('Times New Roman', 10, 'bold'))
        self.ContactInfo_label.place(x=40, y=375)
        self.ContactNo_label = tk.Label(window, text="Contact No.", font=('Times New Roman', 8), bg="#E4E1E1")
        self.ContactNo_label.place(x=45, y=410)
        self.ContactNo_entry = tk.Entry(window, width=35)
        self.ContactNo_entry.place(x=45, y=430)

        self.Email_label = tk.Label(window, text="Email", font=('Times New Roman', 8), bg="#E4E1E1")
        self.Email_label.place(x=265, y=410)
        self.Email_entry = tk.Entry(window, width=50)
        self.Email_entry.place(x=265, y=430)

        self.Other_label = tk.Label(window, text="Other(Social Media)", font=('Times New Roman', 8), bg="#E4E1E1")
        self.Other_label.place(x=45, y=465)
        self.Other_entry = tk.Entry(window, width=35)
        self.Other_entry.place(x=45, y=485)

        self.SocMed_label = tk.Label(window, text="Social Media Account ID/ No.", font=('Times New Roman', 8),
                                     bg="#E4E1E1")
        self.SocMed_label.place(x=265, y=465)
        self.SocMed_entry = tk.Entry(window, width=50)
        self.SocMed_entry.place(x=265, y=485)

        self.Address_label = tk.Label(window, text="Address", font=('Times New Roman', 10, 'bold'))
        self.Address_label.place(x=40, y=525)
        self.AddressLine1_label = tk.Label(window, text="Address Line 1", font=('Times New Roman', 8), bg="#E4E1E1")
        self.AddressLine1_label.place(x=45, y=555)
        self.AddressLine1_entry = tk.Entry(window, width=87)
        self.AddressLine1_entry.place(x=45, y=575)

        self.AddressLine2_entry = tk.Entry(window, width=70)
        self.AddressLine2_entry.place(x=45, y=615)

        self.CityMunicipality_label = tk.Label(window, text="City/Municipality", font=('Times New Roman', 8),
                                               bg="#E4E1E1")
        self.CityMunicipality_label.place(x=45, y=635)
        self.CityMunicipality_entry = tk.Entry(window, width=43)
        self.CityMunicipality_entry.place(x=45, y=655)

        self.StateProvince_label = tk.Label(window, text="State/Province", font=('Times New Roman', 8), bg="#E4E1E1")
        self.StateProvince_label.place(x=310, y=635)
        self.StateProvince_entry = tk.Entry(window, width=43)
        self.StateProvince_entry.place(x=310, y=655)

        self.Country_label = tk.Label(window, text="Country", font=('Times New Roman', 8), bg="#E4E1E1")
        self.Country_label.place(x=45, y=675)
        self.Country_entry = tk.Entry(window, width=43)
        self.Country_entry.place(x=45, y=695)

        self.ZipCode_label = tk.Label(window, text="Zip Code", font=('Times New Roman', 8), bg="#E4E1E1")
        self.ZipCode_label.place(x=310, y=675)
        self.ZipCode_entry = tk.Entry(window, width=20)
        self.ZipCode_entry.place(x=310, y=695)

        self.PicturePath_label = tk.Label(window, text="Picture Path", font=('Times New Roman', 8), bg="#E4E1E1")
        self.PicturePath_label.place(x=45, y=715)
        self.PicturePath_entry = tk.Entry(window, width=87)
        self.PicturePath_entry.place(x=45, y=735)

        # Save and Cancel Buttons
        self.Save_button = tk.Button(window, text="Save", bg="white", width=10, fg="black", command=self.save_data)
        self.Save_button.place(x=250, y=760)
        self.Cancel_button = tk.Button(window, text="Cancel", bg="white", width=10, fg="black")
        self.Cancel_button.place(x=340, y=760)

    # Command for Saving data to SQL
    def save_data(self):
        save_data_query = (
            "INSERT INTO personal_db (first_name, middle_name, last_name, suffix, DOB, gender, nationality, civil_status, "
            "department, employee_status, designation, qualified_status, paydate, employee_num, contact_num, email, other, soc_med, "
            "address1, address2, city_muni, state_prov, country, zip, pic_path) "
            "VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)")
        con.execute(save_data_query, (self.FirstN_entry.get(), self.MiddleN_entry.get(), self.LastN_entry.get(),
                                      self.Suffix_entry.get(), self.DateOfBirth_entry.get(), self.Gender_entry.get(),
                                      self.Nationality_entry.get(), self.CivilStatus_entry.get(),
                                      self.Department_entry.get(),
                                      self.EmployeeStatus_entry.get(), self.Designation_entry.get(),
                                      self.QualifiedStatus_entry.get(),
                                      self.Paydate_entry.get(), self.EmployeeNumber_entry.get(),
                                      self.ContactNo_entry.get(),
                                      self.Email_entry.get(), self.Other_entry.get(), self.SocMed_entry.get(),
                                      self.AddressLine1_entry.get(),
                                      self.AddressLine2_entry.get(), self.CityMunicipality_entry.get(),
                                      self.StateProvince_entry.get(),
                                      self.Country_entry.get(), self.ZipCode_entry.get(), self.PicturePath_entry.get()))
        con.commit()
        con.close()
        print("data saved")
        tk.messagebox.showwarning(title="Data Saved", message="Data has been saved to database.")




# Initialize the application
empapp = EmployeeInfo(window)
window.mainloop()
