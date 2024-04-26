import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkhtmlview import HTMLLabel
from tkinter import messagebox
import re

# Database connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1410",
    database="Quriousinnovate"
)
mycursor = mydb.cursor()

# Check if the table already exists, if not create it
mycursor.execute("CREATE TABLE IF NOT EXISTS student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), class VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS contact_form (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), description TEXT)")
def login(username, password):
    if not username or not password:
        messagebox.showerror("Error", "Username and password cannot be empty.")
        
        return
    
    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    val = (username, password)
    mycursor.execute(sql, val)
    user = mycursor.fetchone()
    if user:
        messagebox.showinfo("Success", "Login Successful!")
        # Additional action after successful login can be added here
    else:
        messagebox.showerror("Error", "Invalid username or password.")
def signup(username, password):
    if not username or not password:
        messagebox.showerror("Error", "Username and password cannot be empty.")
    return
    
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    val = (username, password)
    mycursor.execute(sql, val)
    mydb.commit()
    messagebox.showinfo("Success", "Sign up Successful!")

def open_login_window():
    login_window = tk.Toplevel(root)
    login_window.title("Login")

    login_frame = tk.Frame(login_window, padx=20, pady=20, bg="#2c3e50")  # Dark background color
    login_frame.pack(expand=True)

    username_label = tk.Label(login_frame, text="Username:", bg="#2c3e50", fg="white")  # White text color
    username_label.grid(row=0, column=0, sticky="w")
    username_icon = tk.Label(login_frame, text="👤", bg="#2c3e50", fg="white")  # User icon
    username_icon.grid(row=0, column=1, padx=5)
    username_entry = tk.Entry(login_frame, width=30)
    username_entry.grid(row=0, column=2, padx=5, pady=5)

    password_label = tk.Label(login_frame, text="Password:", bg="#2c3e50", fg="white")  # White text color
    password_label.grid(row=1, column=0, sticky="w")
    password_icon = tk.Label(login_frame, text="🔒", bg="#2c3e50", fg="white")  # Lock icon
    password_icon.grid(row=1, column=1, padx=5)
    password_entry = tk.Entry(login_frame, width=30, show="*")
    password_entry.grid(row=1, column=2, padx=5, pady=5)

    login_button = tk.Button(login_frame, text="Login", command=lambda: login(username_entry.get(), password_entry.get()), bg="#e67e22", fg="white", bd=0, relief=tk.FLAT)  # Orange button color
    login_button.grid(row=2, column=0, columnspan=3, pady=10, sticky="we")
    login_button.bind("<Enter>", lambda event: login_button.config(bg="#d35400"))  # Darker shade on hover
    login_button.bind("<Leave>", lambda event: login_button.config(bg="#e67e22"))

    signup_button = tk.Button(login_frame, text="Sign Up", command=open_signup_window, bg="#3498db", fg="white", bd=0, relief=tk.FLAT)  # Blue button color
    signup_button.grid(row=3, column=0, columnspan=3, pady=10, sticky="we")
    signup_button.bind("<Enter>", lambda event: signup_button.config(bg="#2980b9"))  # Darker shade on hover
    signup_button.bind("<Leave>", lambda event: signup_button.config(bg="#3498db"))

def open_signup_window():
    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")

    signup_frame = tk.Frame(signup_window, padx=20, pady=20, bg="#2c3e50")  # Dark background color
    signup_frame.pack(expand=True)

    username_label = tk.Label(signup_frame, text="Username:", bg="#2c3e50", fg="white")  # White text color
    username_label.grid(row=0, column=0, sticky="w")
    username_icon = tk.Label(signup_frame, text="👤", bg="#2c3e50", fg="white")  # User icon
    username_icon.grid(row=0, column=1, padx=5)
    username_entry = tk.Entry(signup_frame, width=30)
    username_entry.grid(row=0, column=2, padx=5, pady=5)

    password_label = tk.Label(signup_frame, text="Password:", bg="#2c3e50", fg="white")  # White text color
    password_label.grid(row=1, column=0, sticky="w")
    password_icon = tk.Label(signup_frame, text="🔒", bg="#2c3e50", fg="white")  # Lock icon
    password_icon.grid(row=1, column=1, padx=5)
    password_entry = tk.Entry(signup_frame, width=30, show="*")
    password_entry.grid(row=1, column=2, padx=5, pady=5)

    signup_button = tk.Button(signup_frame, text="Sign Up", command=lambda: signup(username_entry.get(), password_entry.get()), bg="#2ecc71", fg="white", bd=0, relief=tk.FLAT)  # Green button color
    signup_button.grid(row=2, column=0, columnspan=3, pady=10, sticky="we")
    signup_button.bind("<Enter>", lambda event: signup_button.config(bg="#27ae60"))  # Darker shade on hover
    signup_button.bind("<Leave>", lambda event: signup_button.config(bg="#2ecc71"))

    login_button = tk.Button(signup_frame, text="Login", command=open_login_window, bg="#17a2b8", fg="white", bd=0, relief=tk.FLAT)  # Blue button color
    login_button.grid(row=3, column=0, columnspan=3, pady=10, sticky="we")
    login_button.bind("<Enter>", lambda event: login_button.config(bg="#2980b9"))  # Darker shade on hover
    login_button.bind("<Leave>", lambda event: login_button.config(bg="#3498db"))


# # Main window
# root = tk.Tk()
# root.title("Login / Sign Up")

# Function to submit form data to the database
def submit_form(name, email, selected_class):
    if not name or not email or not selected_class:
        messagebox.showerror("Error", "name and email cannot be empty.")
        return
    sql = "INSERT INTO student (name, email, class) VALUES (%s, %s, %s)"
    val = (name, email, selected_class)
    mycursor.execute(sql, val)
    mydb.commit()  
    messagebox.showinfo("Success", "Your class booking has been submitted successfully!")


def open_contact_window():
    contact_window = tk.Toplevel(root)
    contact_window.title("Contact Us☎")
    contact_window.geometry("600x400")  # Setting a fixed window size

    # Set light gray background color
    contact_window.configure(bg="#f2f2f2")

    contact_page_frame = tk.Frame(contact_window, padx=20, pady=20, bg="#f2f2f2")
    contact_page_frame.pack()

    # Title
    contact_title_label = tk.Label(contact_page_frame, text="Contact Us", font=("Arial", 18, "bold"), bg="#f2f2f2", fg="#17a2b8")
    contact_title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # Name Entry with icon
    name_label = tk.Label(contact_page_frame, text="Your Name:", font=("Arial", 12,"bold"), bg="#f2f2f2", fg="#17a2b8")
    name_label.grid(row=1, column=0, sticky="w", pady=5)
    name_icon = tk.Label(contact_page_frame, text="👤", font=("Arial", 12,"bold"), bg="#f2f2f2", fg="#17a2b8")
    name_icon.grid(row=1, column=1, sticky="e", pady=5)
    name_entry = tk.Entry(contact_page_frame, width=30, font=("Arial", 12,"bold"))
    name_entry.grid(row=1, column=2, padx=10, pady=5)

    # Email Entry with icon
    email_label = tk.Label(contact_page_frame, text="Your Email:", font=("Arial", 12,"bold"), bg="#f2f2f2", fg="#17a2b8")
    email_label.grid(row=2, column=0, sticky="w", pady=5)
    email_icon = tk.Label(contact_page_frame, text="📧", font=("Arial", 12,"bold"), bg="#f2f2f2", fg="#17a2b8")
    email_icon.grid(row=2, column=1, sticky="e", pady=5)
    email_entry = tk.Entry(contact_page_frame, width=30, font=("Arial", 12,"bold"))
    email_entry.grid(row=2, column=2, padx=10, pady=5)

    # Description Box with icon
    description_label = tk.Label(contact_page_frame, text="Description:", font=("Arial", 12,"bold"), bg="#f2f2f2", fg="#17a2b8")
    description_label.grid(row=3, column=0, sticky="nw", pady=5)
    description_icon = tk.Label(contact_page_frame, text="📝", font=("Arial", 12,"bold"), bg="#f2f2f2", fg="#17a2b8")
    description_icon.grid(row=3, column=1, sticky="e", pady=5)
    description_text = tk.Text(contact_page_frame, width=30, height=5, font=("Arial", 12,"bold"))
    description_text.grid(row=3, column=2, padx=10, pady=5)

    # Submit Button
    submit_button = tk.Button(contact_page_frame, text="Submit", command=lambda: submit_contact_form(name_entry.get(), email_entry.get(), description_text.get("1.0", "end-1c")), bg="#17a2b8", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=0)
    submit_button.grid(row=4, column=0, columnspan=3, pady=(20, 0), padx=10, sticky="ew")

    # Add subtle shadow effect when buttons are hovered over
    submit_button.bind("<Enter>", lambda event: submit_button.config(bg="#17a2b8"))
    submit_button.bind("<Leave>", lambda event: submit_button.config(bg="#17a2b8"))

    # Center-align the form on the screen
    contact_window.update_idletasks()
    width = contact_window.winfo_width()
    height = contact_window.winfo_height()
    x_offset = (contact_window.winfo_screenwidth() - width) // 2
    y_offset = (contact_window.winfo_screenheight() - height) // 2
    contact_window.geometry(f"+{x_offset}+{y_offset}")

    # Center-align the form on the screen
    contact_window.update_idletasks()
    width = contact_window.winfo_width()
    height = contact_window.winfo_height()
    x_offset = (contact_window.winfo_screenwidth() - width) // 2
    y_offset = (contact_window.winfo_screenheight() - height) // 2
    contact_window.geometry(f"+{x_offset}+{y_offset}")



def validate_email(email):

    pattern = r'^[\w-]+(\.[\w-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,})$'
    return re.match(pattern, email)
def validate_mobile(mobile):
    
    pattern = r'^\d{10}$' 
    return re.match(pattern, mobile)

# Function to submit contact form data to the database
# Function to submit contact form data to the database
def submit_contact_form(name, email, description):
   
    if not name or not email:
        messagebox.showerror("Error", "Invalid email format. Please enter a valid email address.")
        return
    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format. Please enter a valid email address.")
        return
    # Insert data into the contact_form table
    sql = "INSERT INTO contact_form (name, email, description) VALUES (%s, %s, %s)"
    val = (name, email, description)
    mycursor.execute(sql, val)
    mydb.commit()  
    messagebox.showinfo("Success", "Your contact form has been submitted successfully!")
    
    print("Contact form submitted successfully!")

    
    print("Contact form submitted successfully!")
def open_class_window():
    class_window = tk.Toplevel(root)
    class_window.title("Book A Seat For Your Child")
    class_window.geometry("400x300")  # Setting a fixed window size

    # Set light background color
    class_window.configure(bg="#f5f5f5")

    form_frame = tk.Frame(class_window, bg="#f5f5f5")
    form_frame.pack(pady=20)

    title_label = tk.Label(form_frame, text="Book A Seat For Your Child", font=("Arial", 16, "bold"), bg="#f5f5f5",fg="#17a2b8")
    title_label.grid(row=0, column=0, columnspan=2, pady=(0, 10), sticky="n")

    name_label = tk.Label(form_frame, text="👤 Child's Name:", font=("Arial", 12, "bold"), bg="#f5f5f5",fg="#17a2b8")
    name_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
    name_entry = tk.Entry(form_frame, font=("Arial", 12))
    name_entry.grid(row=1, column=1, padx=5, pady=5)

    email_label = tk.Label(form_frame, text="📞 Your Contact:", font=("Arial", 12, "bold"), bg="#f5f5f5",fg="#17a2b8")
    email_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')
    email_entry = tk.Entry(form_frame, font=("Arial", 12))
    email_entry.grid(row=2, column=1, padx=5, pady=5)

    class_label = tk.Label(form_frame, text="📅 Select A Class:", font=("Arial", 12, "bold"), bg="#f5f5f5",fg="#17a2b8")
    class_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')
    class_var = tk.StringVar()
    class_dropdown = ttk.Combobox(form_frame, textvariable=class_var, font=("Arial", 12))
    class_dropdown['values'] = ('Class 5', 'Class 6', 'Class 7', 'Class 8', 'Class 9')
    class_dropdown.grid(row=3, column=1, padx=5, pady=5)

    # Book Now button with soft blue color and rounded corners
    submit_button = tk.Button(form_frame, text="Book Now", command=lambda: submit_form(name_entry.get(), email_entry.get(), class_var.get()),
                              bg="#17a2b8", fg="white", font=("Arial", 12, "bold"), relief="raised", bd=0)
    submit_button.grid(row=4, column=0, columnspan=2, pady=(20, 0), padx=10, sticky="ew")
    
    # Add subtle shadow effect when buttons are hovered over
    submit_button.bind("<Enter>", lambda event: submit_button.config(bg="#17a2b8"))
    submit_button.bind("<Leave>", lambda event: submit_button.config(bg="#17a2b8"))

    # Center-align the form on the screen
    class_window.update_idletasks()
    width = class_window.winfo_width()
    height = class_window.winfo_height()
    x_offset = (class_window.winfo_screenwidth() - width) // 2
    y_offset = (class_window.winfo_screenheight() - height) // 2
    class_window.geometry(f"+{x_offset}+{y_offset}")



# Function to open the about window
def open_about_window():
    about_window = tk.Toplevel(root)
    about_window.title("About Qurious")
    
    # Title
    title_label = tk.Label(about_window, text="Explore", font=("Arial", 18, "bold"), fg="#17a2b8")
    title_label.pack(pady=(10, 5))

    # Description
    description_label = tk.Label(about_window, text="Over 15000+ Careers, At one place, With Qurious", font=("Arial", 12), fg="#333")
    description_label.pack(pady=(5, 10))

    # Benefits
    benefits_frame = tk.Frame(about_window)
    benefits_frame.pack()

    benefits_title_label = tk.Label(benefits_frame, text="Why Choose Qurious?", font=("Arial", 14, "bold"), fg="#17a2b8")
    benefits_title_label.pack(anchor="w", padx=10, pady=(10, 5))

    benefits_list = [
        "Personalized guidance from expert counselors",
        "Interactive workshops and activities",
        "Career exploration tools and resources",
        "Proven track record of success"
    ]

    for benefit in benefits_list:
        benefit_label = tk.Label(benefits_frame, text=f"\u2022 {benefit}", font=("Arial", 12), fg="#333")
        benefit_label.pack(anchor="w", padx=20, pady=5)

# Function to open the "Learn More" window
def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Learn More")
     # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the geometry of the window to fill the entire screen
    new_window.geometry(f"{screen_width}x{screen_height}")


    # Use HTMLLabel to display HTML content with basic CSS styling
    html_label = HTMLLabel(new_window, html="""
    <html>
    <body style="font-family: Arial, sans-serif; background-color: #f2f2f2; padding: 20px;">
    <h1 style="color: #17a2b8;">Welcome to Qurious, where exploration is the greatest treasure 🌟</h1>
    <p style="color: #333;">We believe in the power of "अन्वेषणं महोदधेः परमं धनं" (Anveṣaṇaṁ mahodadheḥ paramaṁ dhanaṁ), which translates to "Exploration is the greatest treasure of the vast ocean." Our mission is to guide students in discovering their passions and potential career paths 🚀. We offer a wide range of career exploration activities designed to ignite curiosity 🔍, inspire creativity, and foster a deeper understanding of various industries and professions.</p>
   <h1 style="color: #17a2b8;">Beyond Conventional Career Guidance</h1>
    <p style="color: #333;">At Qurious, we go beyond conventional methods of career guidance. We offer innovative programs that encourage students to think outside the box and explore unconventional career paths. Our career exploration activities are not just about exploration - they're about discovering a world, a calling, a purpose. We believe that every individual has unique talents and interests waiting to be uncovered, and it's our mission to help students uncover them..</p>
     <h1 style="color: #17a2b8;">The Journey is the Destination</h1>
    <p style="color: #333;">We're passionate about our vision at Qurious, where we believe that exploration is the greatest treasure. Our dedication to guiding students towards discovering their passions and potential career paths is at the core of everything we do. If you're inspired by our commitment to igniting curiosity, fostering creativity, and empowering students, we'd love to hear from you! Whether you're eager to learn more about our programs or simply want to connect with our team, don't hesitate to reach out. Your journey towards a fulfilling future starts here. Get in touch with us today and let's embark on this exciting adventure together!

.</p>
   
    </body>
    </html>
    """)
    html_label.pack(fill="both", expand=True)

# Main window
root = tk.Tk()
root.title("Qurious Academic Platform")

# Prominent Call to Action (CTA)
cta_frame = tk.Frame(root, bg="#17a2b8")
cta_frame.pack(fill="x", padx=20, pady=20)

cta_label = tk.Label(cta_frame, text="Join Our Exploration Journey Today!", font=("Arial", 20), fg="white", bg="#17a2b8")
cta_label.pack()

cta_button = tk.Button(cta_frame, text="Explore Now", command=open_new_window, bg="#ffffff", fg="#17a2b8", font=("Arial", 14))
cta_button.pack(pady=10)


# Navbar
navbar_frame = ttk.Frame(root)
navbar_frame.pack(fill="x")

home_button = ttk.Button(navbar_frame, text="Home")
home_button.pack(side="left", padx=10)

about_button = ttk.Button(navbar_frame, text="About", command=open_about_window)
about_button.pack(side="left", padx=10)

classes_button = ttk.Button(navbar_frame, text="Classes", command=open_class_window)
classes_button.pack(side="left", padx=10)

contact_button = ttk.Button(navbar_frame, text="Contact", command=open_contact_window)
contact_button.pack(side="left", padx=10)

join_class_button = ttk.Button(navbar_frame, text="Join Class",command=open_login_window)
join_class_button.pack(side="left", padx=10)


# Content Frame
content_frame = tk.Frame(root)
content_frame.pack(fill="both", expand=True)

left_frame = tk.Frame(content_frame, bg="white", padx=20, pady=20)
left_frame.pack(side="left", fill="both", expand=True)

right_frame = tk.Frame(content_frame, bg="#f2f2f2", padx=20, pady=20)
right_frame.pack(side="right", fill="both", expand=True)

title_label = tk.Label(left_frame, text="Beyond Textbook : From Qurious to Victorious", font=("Arial", 24), bg="white", fg="#17a2b8", padx=10, pady=10)
title_label.pack()

# Enhanced description with bullet points
description_label = tk.Label(left_frame, text="""In a world where 80% of the jobs of 2030 do not yet exist,
and where it is difficult to anticipate what skills will be essential tomorrow, we believe in being agile and continuously learning.
At Qurious, we embrace this challenge by shaping inquisitive minds, eager to explore beyond textbooks. Our mission is to prepare students for a victorious future.
- Personalized guidance from expert counselors
- Interactive workshops and activities
- Access to career exploration tools and resources
- Proven track record of success""", bg="white", padx=10, pady=10, justify="left")
description_label.pack()

# Learn More button
learn_more_button = tk.Button(left_frame, text="Learn More", command=open_new_window, bg="#17a2b8", fg="white", font=("Arial", 14))
learn_more_button.pack(pady=10, padx=10, anchor="w")

image = tk.PhotoImage(file="Student_blue.png")  
image_label = tk.Label(left_frame, image=image, bg="#f2f2f2")
image_label.pack(expand=True)

root.mainloop()