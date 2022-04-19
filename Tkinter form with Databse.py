from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
import sqlite3


root = Tk()
root.geometry("412x717")
root.resizable(width=False, height=False)
root.configure(bg="white")


FirstName = StringVar()
LastName = StringVar()
Email = StringVar()
tkvar = StringVar(root)
add1 = StringVar()
add2 = StringVar()
countryvar = StringVar(root)
city = StringVar()
state = StringVar()
pin = StringVar()
pno = StringVar()
hobby = StringVar()
comname = StringVar()
jobtitle = StringVar()
howlong = StringVar()
rn1 = StringVar()
rp1 = StringVar()
rn2 = StringVar()
rp2 = StringVar()


def sub():
    FirstName_db = FirstName.get()
    LastName_db = LastName.get()
    Email_db = Email.get()
    grad_db = tkvar.get()
    add1_db = add1.get()
    add2_db = add2.get()
    country_db = countryvar.get()
    city_db = city.get()
    state_db = state.get()
    pin_db = pin.get()
    pno_db = pno.get()
    hobby_db = hobby.get()
    comname_db = comname.get()
    jobtitle_db = jobtitle.get()
    howlong_db = howlong.get()
    rn1_db = rn1.get()
    rp1_db = rp1.get()
    rn2_db = rn2.get()
    rp2_db = rp2.get()
    conn = sqlite3.connect("Form.db")
    with conn:
        cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS details(FirstName TEXT, LastName TEXT, Email TEXT, Education TEXT, Address1 TEXT, Address2 TEXT, Country TEXT, City TEXT, State TEXT, ZipCode TEXT, PhoneNumber TEXT, Hobbies TEXT, CompanyName TEXT, JobTitle TEXT, How_long_were_you_here TEXT, r1_name TEXT, r1_PhoneNo TEXT, r2_name TEXT, r2_PhoneNo TEXT) ')
    cursor.execute('INSERT INTO details(FirstName, LastName, Email, Education, Address1, Address2, Country, City, State, ZipCode, PhoneNumber, Hobbies, CompanyName, JobTitle, How_long_were_you_here, r1_name, r1_PhoneNo, r2_name, r2_PhoneNo) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                   (FirstName_db, LastName_db, Email_db, grad_db, add1_db, add2_db, country_db, city_db, state_db, pin_db, pno_db, hobby_db, comname_db, jobtitle_db, howlong_db, rn1_db, rp1_db, rn2_db, rp2_db,))
    conn.commit()

    for row in cursor.execute('SELECT * FROM details '):
        print(row)
        
    root.destroy()


red_bar = Label(root, text="", bg="dark red")
font_title = tkFont.Font(family="Times New Roman", size=18, weight="bold")
job_application = Label(root, text="Job Application",
                        font=font_title, bg="white")
sub_title = tkFont.Font(family="Arial", size=11, weight="bold")
personal_information = Label(
    root, text="Personal Information", font=sub_title, fg="dark red", bg="white")
name = Label(root, text="Name ", bg="white")
email = Label(root, text="Email ", bg="white")
education = Label(root, text="Education ", bg="white")
resume = Label(root, text="Resume", bg="white")
address = Label(root, text="Address", bg="white")
phone_number = Label(root, text="Phone Number", bg="white")
hobbies = Label(root, text="What are your hobbies?", bg="white")
frame_text = tkFont.Font(size=5)
firstname_label = LabelFrame(
    root, text="First Name", font=frame_text, bg="white")
lastname_label = LabelFrame(root, text="Last Name",
                            font=frame_text, bg="white")
first_name = Entry(firstname_label, width=23, borderwidth=1,
                   bg="white", textvar=FirstName)
last_name = Entry(lastname_label, width=21, borderwidth=1,
                  bg="white", textvar=LastName)
email_entry = Entry(root, width=44, borderwidth=1, bg="white", textvar=Email)
email_entry.insert(0, "user@example.com")


choices = ["10th pass", "12th pass", "diploma", "UnderGrad", "PostGrad"]
tkvar.set("please select")
education_entry = OptionMenu(root, tkvar, *choices)

resume_entry = Entry(root, width=20, borderwidth=1, bg="white")


def upload(event=None):
    filename = filedialog.askopenfile()
    resume_entry.insert(0, filename)


upload_button = Button(root, text="Choose file",
                       command=upload, width=19, bg="white")

address1_frame = LabelFrame(root, text="Address 1",
                            font=frame_text, bg="white")
address1_entry = Entry(address1_frame, width=45,
                       borderwidth=1, bg="white", textvar=add1)
address2_frame = LabelFrame(root, text="Address 2",
                            font=frame_text, bg="white")
address2_entry = Entry(address2_frame, width=45,
                       borderwidth=1, bg="white", textvar=add2)


country = ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia",
           "Australia", "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium",
           "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei", "Bulgaria",
           "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", "Central African Republic", "Chad",
           "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the Kinshasa",
           "Congo, Republic of the Brazzaville", "Costa Rica", "Cote d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czechia",
           "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador",
           "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini (formerly Swaziland)", "Ethiopia", "Fiji", "Finland",
           "France", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", "Guinea",
           "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq",
           "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kosovo",
           "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein",
           "Lithuania", "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
           "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco",
           "Mozambique", "Myanmar (formerly Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", "Niger", "Nigeria",
           "North Korea", "North Macedonia (formerly Macedonia)", "Norway", "Oman", "Pakistan", "Palau", "Palestine",
           "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania",
           "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
           "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles",
           "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa",
           "South Korea", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden", "Switzerland",
           "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Timor-Leste", "Togo", "Tonga",
           "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine",
           "United Arab Emirates (UAE)", "United Kingdom (UK)", "United States of America (USA)", "Uruguay",
           "Uzbekistan", "Vanuatu", "Vatican City (Holy See)", "Venezuela", "Vietnam", "Yemen", "Zambia",
           "Zimbabwe"]
countryvar.set("   Select Country   ")
country_entry = OptionMenu(root, countryvar, *country)

city_frame = LabelFrame(root, text="City", width=15,
                        font=frame_text, bg="white")
city_entry = Entry(city_frame, width=15, borderwidth=1,
                   bg="white", textvar=city)

state_frame = LabelFrame(root, text="state", width=15,
                         font=frame_text, bg="white")
state_entry = Entry(state_frame, width=15, borderwidth=1,
                    bg="white", textvar=state)

zip_frame = LabelFrame(root, text="Zip Cose", width=15,
                       font=frame_text, bg="white")
zip_entry = Entry(zip_frame, width=15, borderwidth=1, bg="white", textvar=pin)

phonenumber_entry = Entry(
    root, width=38, borderwidth=1, bg="white", textvar=pno)
hobbies_entry = Entry(root, width=66, borderwidth=2, bg="white", textvar=hobby)

red_bar.grid(row=0, column=1, sticky=E+W, columnspan=10)
job_application.grid(row=1, column=1, columnspan=20)
personal_information.grid(row=2, column=1, columnspan=2, sticky=W)
name.grid(row=3, column=1, sticky=W)
email.grid(row=4, column=1, sticky=W)
education.grid(row=5, column=1, sticky=W)
resume.grid(row=6, column=1, sticky=W)
address.grid(row=7, column=1, sticky=W)
phone_number.grid(row=11, column=1, sticky=W)
hobbies.grid(row=12, column=1, sticky=W)

first_name.grid(row=3, column=2, padx=1, pady=1, columnspan=2)
last_name.grid(row=3, column=4, padx=1, pady=1, columnspan=2)
firstname_label.grid(row=3, column=2, padx=1, pady=1, sticky=W)
lastname_label.grid(row=3, column=4, padx=1, pady=1, sticky=W)
email_entry.grid(row=4, column=2, columnspan=5, padx=2, pady=2, sticky=W)
education_entry.grid(row=5, column=2, columnspan=5, pady=2, sticky=W)
resume_entry.grid(row=6, column=4, columnspan=5, sticky=W)
upload_button.grid(row=6, column=2, padx=2, pady=2, sticky=W)
address1_frame.grid(row=7, column=2, columnspan=5, padx=2, pady=2, sticky=W)
address2_frame.grid(row=8, column=2, columnspan=5, padx=2, pady=2, sticky=W)
address1_entry.grid(row=7, column=2, columnspan=5, padx=2, pady=2, sticky=W)
address2_entry.grid(row=8, column=2, columnspan=5, padx=2, pady=2, sticky=W)
country_entry.grid(row=9, column=2, columnspan=5, pady=2, sticky=W)
zip_frame.grid(row=9, column=3, columnspan=5, pady=2, sticky=W)
zip_entry.grid(row=9, column=3, columnspan=5, pady=2, sticky=W)
city_frame.grid(row=10, column=2, columnspan=2, padx=2, pady=2, sticky=W)
city_entry.grid(row=10, column=2, columnspan=2, padx=2, pady=2, sticky=W)
state_frame.grid(row=10, column=3, columnspan=2, padx=2, pady=2, sticky=W)
state_entry.grid(row=10, column=3, columnspan=2, padx=2, pady=2, sticky=W)
phonenumber_entry.grid(row=11, column=2, columnspan=4,
                       padx=2, pady=2, sticky=W)
hobbies_entry.grid(row=13, column=1, columnspan=7, padx=2, pady=2, stick=W)


employment_detail = Label(
    root, text="Previous/ Current Employment Details", font=sub_title, fg="dark red", bg="white")

company_name = Label(root, text="Company Title", bg="white")
companyname_entry = Entry(root, width=44, borderwidth=1,
                          bg="white", textvar=comname)

job_title = Label(root, text="Job Title ", bg="white")
jobtitle_entry = Entry(root, width=44, borderwidth=1,
                       bg="white", textvar=jobtitle)

how_long = Label(root, text="How long were you\nhere?", bg="white")
howlong_entry = Entry(root, width=44, borderwidth=1,
                      bg="white", textvar=howlong)

employment_detail.grid(row=14, column=1, columnspan=7,
                       padx=2, pady=5, sticky=W)

company_name.grid(row=15, column=1, sticky=W)
companyname_entry.grid(row=15, column=2, columnspan=7, sticky=W)

job_title.grid(row=16, column=1, sticky=W)
jobtitle_entry.grid(row=16, column=2, columnspan=7, sticky=W)

how_long.grid(row=17, column=1, sticky=W)
howlong_entry.grid(row=17, column=2, columnspan=7, sticky=W)


reference_1 = Label(root, text="Reference #1",
                    font=sub_title, fg="dark red", bg="white")
rname_1 = Label(root, text="Name", bg="white")
rname1_entry = Entry(root, width=44, borderwidth=1, bg="white", textvar=rn1)
rphone_1 = Label(root, text="Phone", bg="white")
rphone1_entry = Entry(root, width=44, borderwidth=1, bg="white", textvar=rp1)

reference_1.grid(row=18, column=1, columnspan=7, padx=2, pady=5, sticky=W)
rname_1.grid(row=19, column=1, sticky=W)
rname1_entry.grid(row=19, column=2, columnspan=7, sticky=W)
rphone_1.grid(row=20, column=1, sticky=W)
rphone1_entry.grid(row=20, column=2, columnspan=7, sticky=W)


reference_2 = Label(root, text="Reference #2",
                    font=sub_title, fg="dark red", bg="white")
rname_2 = Label(root, text="Name", bg="white")
rname2_entry = Entry(root, width=44, borderwidth=1, bg="white", textvar=rn2)
rphone_2 = Label(root, text="Phone", bg="white")
rphone2_entry = Entry(root, width=44, borderwidth=1, bg="white", textvar=rp2)

reference_2.grid(row=21, column=1, columnspan=7, padx=2, pady=5, sticky=W)
rname_2.grid(row=22, column=1, sticky=W)
rname2_entry.grid(row=22, column=2, columnspan=7, sticky=W)
rphone_2.grid(row=23, column=1, sticky=W)
rphone2_entry.grid(row=23, column=2, columnspan=7, sticky=W)


apply = Button(root, text="Apply", width=12,
               borderwidth=1, fg="white", bg="dark red", command=sub)
apply.grid(row=24, column=2, padx=5, pady=5)


root.mainloop()
