import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk, Text, PhotoImage, messagebox
from tkinter import messagebox, Text
import  tkinter.messagebox
from tkinter import BOTH, END, LEFT
import os
from PIL import Image,ImageTk
import random
import speech_recognition as sr
from get_disease import *
from findsynonym import *
from get_medicine import *
from get_prescription import *
from create_prescription import *
from tkinter import scrolledtext
import sqlite3
count=0
age=""
name=""
medstr=""
diagnose=""
class gui:

    def __init__(self,conn,create):
        self.conn=conn
        self.create=create

    def loginregisteraboutscreen(self):
        global screen
        screen = Tk()
        screen.geometry("1200x750")
        screen.title("CURE AI")
        screen.configure(bg='lightblue')
        screen.iconphoto(False, tk.PhotoImage(file='assets/images/abc1.png'))

        Label(text="CURE AI", fg='white', bg="darkblue", width="300", height="2", font=("orbitron", 15, 'bold')).pack()
        Label(text="", bg='lightblue').pack()

        img = ImageTk.PhotoImage(Image.open("assets/images/abc1.png"))
        panel = Label(screen, image=img, bg='lightblue')
        panel.pack()

        def gotologin():
            screen.destroy()
            self.create.execute('SELECT * FROM userSignUp')
            z = self.create.fetchall()
            print(z)
            # self.conn.close()
            self.login(z)

        def gotoregister():
            screen.destroy()
            self.register()
        photo1 = PhotoImage(file="assets/images/login_final.png")
        photoimage1 = photo1.subsample(2, 2)
        Button(command=gotologin, bg='lightblue', activebackground='lightblue', relief=FLAT, image=photoimage1).pack(pady=5)

        Label(text="", bg='lightblue', ).pack()

        photo2 = PhotoImage(file="assets/images/register_final.png")
        photoimage2 = photo2.subsample(2, 2)
        Button(command=gotoregister, bg='lightblue', activebackground='lightblue', relief=FLAT, image=photoimage2).pack(
            pady=5)

        Label(text="", bg='lightblue').pack()


        photo3 = PhotoImage(file="assets/images/about_final.png")
        photoimage3 = photo3.subsample(2, 2)
        Button(command=self.create_cureai_window, bg='lightblue', activebackground='lightblue', relief=FLAT, image=photoimage3).pack(pady=5)

        #creating object




        screen.mainloop()
        # screen.destroy()

    def register(self):
        global screen1
        global password_entry
        global username_entry
        global rand
        screen1 = Tk()
        screen1.title("Register")
        screen1.geometry("1200x800")
        screen1.configure(bg='lightblue')
        screen1.iconphoto(False, tk.PhotoImage(file='assets/images/abc1.png'))

        photo = PhotoImage(file="assets/images/login_person.png")
        label = Label(screen1, image=photo, bg='lightblue')
        label.image = photo
        label.pack(pady=5)

        global password
        global name

        global aadharno
        global password_entry
        global name_entry
        global aadharno_entry

        password = StringVar()
        aadharno = StringVar()
        name = StringVar()

        Label(screen1, text="Please enter details below to register", bg='lightblue', font=("orbitron", 10)).pack()

        Label(screen1, text="", bg='lightblue').pack()
        Label(screen1, text="Name", font=("orbitron", 10), bg='lightblue').pack()
        name_entry = Entry(screen1, font=("orbitron", 10), textvariable=name)
        name_entry.pack()

        Label(screen1, text="AADHAAR No.", font=("orbitron", 10), bg='lightblue').pack()
        aadharno_entry = Entry(screen1, font=("orbitron", 11),textvariable=aadharno).pack()
        # username_entry = Entry(screen1, textvariable = username)
        # username_entry.pack()

        Label(screen1, text="Pin", font=("orbitron", 10), bg='lightblue').pack()
        password_entry = Entry(screen1, font=("orbitron", 10), textvariable=password)
        password_entry.config(fg='black', show='●')
        password_entry.pack()

        Label(screen1, text="", bg='lightblue').pack()

        def addUserToDataBase():

            global fullname
            fullname = name.get()
            global adno
            adno = aadharno.get()
            global password1
            password1 = password.get()


            if len(fullname) == 0 and len(adno) == 0 and len(password1) == 0 :
                error = Label(text="You haven't enter any field...Please Enter all the fields", fg='black', bg='white')
                error.place(relx=0.37, rely=0.7)

            elif len(name.get()) == 0 or len(aadharno.get()) == 0 or len(password.get()) == 0 :
                error = Label(text="Please Enter all the fields", fg='black', bg='white')
                error.place(relx=0.37, rely=0.7)

            elif len(aadharno.get()) == 0 and len(password.get()) == 0:
                error = Label(text="AADHARNO and PIN can't be empty", fg='black', bg='white')
                error.place(relx=0.37, rely=0.7)

            elif len(aadharno.get()) == 0 and len(password.get()) != 0:
                error = Label(text="AADHARNO can't be empty", fg='black', bg='white')
                error.place(relx=0.37, rely=0.7)

            elif len(aadharno.get()) != 0 and len(password.get()) == 0:
                error = Label(text="PIN can't be empty", fg='black', bg='white')
                error.place(relx=0.37, rely=0.7)

            else:
                messagebox.showinfo("SUCCESS", "SIGNUP SUCCESSFUL")

                self.create.execute("INSERT INTO userSignUp VALUES (?,?,?)", (fullname, adno, password1))
                self.conn.commit()
                self.create.execute('SELECT * FROM userSignUp')
                z = self.create.fetchall()
                print(z)
                # self.conn.close()
                # self.login(z)
                screen1.destroy()
                self.loginregisteraboutscreen()


        img1 = PhotoImage(file="assets/images/register_final.png")
        photoimage1 = img1.subsample(3, 3)
        img1Btn = Button(screen1, command=addUserToDataBase, image=photoimage1, bg='lightblue',
                         activebackground='lightblue', relief=FLAT)
        img1Btn.image = photoimage1
        img1Btn.pack()

        screen1.mainloop()

    ################## LOGIN DISPLAY SCREEN #################################
    def login(self,logdata):
        # screen.destroy()
        global screen2
        screen2 = Tk()
        screen2.title("Login")
        screen2.geometry("1200x800")
        screen2.configure(bg='lightblue')
        screen2.iconphoto(False, tk.PhotoImage(file='assets/images/abc1.png'))

        Label(text="CURE AI.", fg='white', bg="darkblue", width="300", height="2",
              font=("orbitron", 15, 'bold')).pack()
        Label(text="", bg='lightblue').pack()

        photo = PhotoImage(file="assets/images/login_person.png")
        label = Label(screen2, image=photo, bg='lightblue')
        label.image = photo
        label.pack(pady=5)

        Label(screen2, text="Please enter details below to login", bg='lightblue', font=("orbitron", 10)).pack()
        Label(screen2, text="", bg='lightblue').pack()

        # global username_verify
        # global password_verify
        # global name_verify
        # global age_verify

        name_verify=StringVar()
        username_verify = StringVar()
        password_verify = StringVar()
        age_verify=StringVar()

        # global username_entry1
        # global password_entry1
        # global age1
        # global name_entry


        Label(screen2, text="Name.", bg='lightblue', font=("orbitron", 10)).pack()
        name_entry = Entry(screen2, font=("orbitron", 10), textvariable=name_verify)
        name_entry.pack()

        Label(screen2, text="AADHAAR No.", bg='lightblue', font=("orbitron", 10)).pack()
        username_entry1 = Entry(screen2, font=("orbitron", 10), textvariable=username_verify)
        username_entry1.pack()

        Label(screen2, text="Age.", bg='lightblue', font=("orbitron", 10)).pack()
        age1 = Entry(screen2, font=("orbitron", 10), textvariable=age_verify)
        age1.pack()

        Label(screen2, text="Pin", bg='lightblue', font=("orbitron", 10)).pack()
        password_entry1 = Entry(screen2, font=("orbitron", 10), textvariable=password_verify)
        password_entry1.config(fg='black', show='●')
        password_entry1.pack()

        Label(screen2, text="", bg='lightblue').pack()

        def check():
            for a, b, c in logdata:
                if b == username_verify.get() and c == password_verify.get():
                    global name
                    global age

                    name = name_verify.get()
                    age =age_verify.get()


                    self.symptoms()
                    break
                    # screen2.destroy()
            else:
                messagebox.showerror("ERROR", "LOGIN FAILED")


        img1 = PhotoImage(file="assets/images/login_final.png")
        photoimage1 = img1.subsample(3, 3)
        img1Btn = Button(screen2, command=check, image=photoimage1, bg='lightblue', activebackground='lightblue',
                         relief=FLAT)
        img1Btn.image = photoimage1
        img1Btn.pack()

        screen2.mainloop()

    def create_cureai_window(self):
        # root = tk.Tk()
        root=Toplevel(screen)
        root.title("CURE AI. - Healthcare Solutions")
        root.geometry("1200x750")
        root.configure(bg="lightblue")
        screen.iconphoto(False, tk.PhotoImage(file='assets/images/abc1.png'))

        # Label(text="C.U.R.E  A.I.", fg='white', bg="darkblue", width="300", height="2",
        #       font=("orbitron", 15, 'bold')).pack()
        # Label(text="", bg='lightblue').pack()
        # Organization Details
        org_frame = tk.Frame(root, bg="lightblue")
        org_frame.pack(pady=10)

        tk.Label(org_frame, text="Organization Details", font=("Helvetica", 16, "bold"), bg="lightblue").grid(row=0,
                                                                                                              column=0,
                                                                                                              sticky="w",
                                                                                                              padx=10,
                                                                                                              pady=5)

        details = [
            ("Organization Name:", "CURE Artificial Intelligence Solutions"),
            ("Address:", "Block A, Pune"),
            ("Phone:", "9999999999"),
            ("Email:", "support@cureai.com")
        ]

        for i, (label_text, value) in enumerate(details):
            tk.Label(org_frame, text=label_text, bg="lightblue").grid(row=i + 1, column=0, sticky="w", padx=10)
            tk.Label(org_frame, text=value, bg="lightblue").grid(row=i + 1, column=1, sticky="w", padx=10)

        # About C.U.R.E A.I.
        about_frame = tk.Frame(root, bg="lightblue")
        about_frame.pack(pady=10)

        tk.Label(about_frame, text="About CURE AI", font=("Helvetica", 16, "bold"), bg="lightblue").grid(row=0,
                                                                                                              column=0,
                                                                                                              sticky="w",
                                                                                                              padx=10,
                                                                                                              pady=5)

        about_text = "CURE AI is a leading provider of artificial intelligence solutions in healthcare. " \
                     "We are committed to revolutionizing the way healthcare is delivered, using cutting-edge technology " \
                     "to enhance patient care and streamline medical processes."

        tk.Label(about_frame, text=about_text, bg="lightblue").grid(row=1, column=0, columnspan=2, sticky="w", padx=10)

        # Our Services
        services_frame = tk.Frame(root, bg="lightblue")
        services_frame.pack(pady=10)

        tk.Label(services_frame, text="Our Services", font=("Helvetica", 16, "bold"), bg="lightblue").grid(row=0,
                                                                                                           column=0,
                                                                                                           sticky="w",
                                                                                                           padx=10,
                                                                                                           pady=5)

        services_list = [
            "Medical Diagnosis and Predictive Analytics",
            "Personalized Treatment Plans",
            "Healthcare Automation Solutions"
        ]

        for i, service in enumerate(services_list):
            tk.Label(services_frame, text="- " + service, bg="lightblue").grid(row=i + 1, column=0, sticky="w", padx=20)

        # Patient Information
        patient_frame = tk.Frame(root, bg="lightblue")
        patient_frame.pack(pady=10)

        # Contact Information
        contact_frame = tk.Frame(root, bg="lightblue")
        contact_frame.pack(pady=10)

        tk.Label(contact_frame, text="Contact Information", font=("Helvetica", 16, "bold"), bg="lightblue").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 sticky="w",
                                                                                                                 padx=10,
                                                                                                                 pady=5)

        tk.Label(contact_frame, text="For inquiries or support, please contact:", bg="lightblue").grid(row=1, column=0,
                                                                                                       columnspan=2,
                                                                                                       sticky="w",
                                                                                                       padx=20)
        tk.Label(contact_frame, text="Email: support@cureai.com", bg="lightblue").grid(row=2, column=0, columnspan=2,
                                                                                       sticky="w", padx=20)
        tk.Label(contact_frame, text="Phone: 9999999999", bg="lightblue").grid(row=3, column=0, columnspan=2,
                                                                               sticky="w", padx=20)

        # Visit Website
        website_frame = tk.Frame(root, bg="lightblue")
        website_frame.pack(pady=10)

        tk.Label(website_frame, text="Visit our website for more information:", bg="lightblue").grid(row=0, column=0,
                                                                                                     sticky="w",
                                                                                                     padx=10, pady=5)
        tk.Label(website_frame, text="www.cureai.com", font=("Helvetica", 12, "underline"), fg="blue", cursor="hand2",
                 bg="lightblue").grid(row=1, column=0, sticky="w", padx=20)

        # Closing Message
        tk.Label(root, text="Thank you for choosing CURE AI for your healthcare needs.", font=("Helvetica", 14),
                 bg="lightblue").pack(pady=10)

        # Close Button
        def close_window():
            root.destroy()

        close_button_frame = tk.Frame(root, bg="lightblue")
        close_button_frame.pack(pady=10)

        close_button_image = PhotoImage(
            file="assets/images/close.png")  # Replace with the actual path to your close button image
        close_button_image = close_button_image.subsample(2, 2)

        close_button = Button(root, command=close_window, bg='lightblue', activebackground='lightblue',
                              relief=FLAT, image=close_button_image)
        close_button.pack(pady=5)

        root.mainloop()

    def symptoms(self):
        screen2.destroy()
        global symptoms
        symptoms = tk.Tk()
        symptoms.geometry("1200x800")
        symptoms.title("CURE AI")
        symptoms.configure(bg='lightblue')
        symptoms.iconphoto(False, tk.PhotoImage(file='assets/images/abc1.png'))
        tk.Label(symptoms, text="CURE AI", fg='white', bg="darkblue", width="300", height="2",
                 font=("orbitron", 15, 'bold')).pack()
        tk.Label(symptoms, text="", bg='lightblue').pack()
        tk.Label(symptoms,
                 text="Please select symtoms from the drop down list and add using add symptoms button and then submit.",
                 fg='white', bg="darkblue", width="150", height="2", font=("orbitron", 13, 'bold')).pack()
        tk.Label(symptoms, text="", bg='lightblue', bd=10).pack()

        # Create a text box
        text_box = Text(symptoms, height=10, width=100)
        text_box.pack(padx=10, pady=10)

        # Create a dropdown list
        columns = [
            "itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing",
            "shivering", "chills", "joint_pain", "stomach_pain", "acidity",
            "ulcers_on_tongue", "muscle_wasting", "vomiting", "burning_micturition",
            "spotting_urination", "fatigue", "weight_gain", "anxiety",
            "cold_hands_and_feets", "mood_swings", "weight_loss", "restlessness",
            "lethargy", "patches_in_throat", "irregular_sugar_level", "cough",
            "high_fever", "sunken_eyes", "breathlessness", "sweating", "dehydration",
            "indigestion", "headache", "yellowish_skin", "dark_urine", "nausea",
            "loss_of_appetite", "pain_behind_the_eyes", "back_pain", "constipation",
            "abdominal_pain", "diarrhoea", "mild_fever", "yellow_urine",
            "yellowing_of_eyes", "acute_liver_failure", "fluid_overload",
            "swelling_of_stomach", "swelled_lymph_nodes", "malaise",
            "blurred_and_distorted_vision", "phlegm", "throat_irritation",
            "redness_of_eyes", "sinus_pressure", "runny_nose", "congestion",
            "chest_pain", "weakness_in_limbs", "fast_heart_rate",
            "pain_during_bowel_movements", "pain_in_anal_region", "bloody_stool",
            "irritation_in_anus", "neck_pain", "dizziness", "cramps", "bruising",
            "obesity", "swollen_legs", "swollen_blood_vessels",
            "puffy_face_and_eyes", "enlarged_thyroid", "brittle_nails",
            "swollen_extremities", "excessive_hunger", "extra_marital_contacts",
            "drying_and_tingling_lips", "slurred_speech", "knee_pain",
            "hip_joint_pain", "muscle_weakness", "stiff_neck", "swelling_joints",
            "movement_stiffness", "spinning_movements", "loss_of_balance",
            "unsteadiness", "weakness_of_one_body_side", "loss_of_smell",
            "bladder_discomfort", "foul_smell_of_urine", "continuous_feel_of_urine",
            "passage_of_gases", "internal_itching", "toxic_look_(typhos)", "depression",
            "irritability", "muscle_pain", "altered_sensorium",
            "red_spots_over_body", "belly_pain", "abnormal_menstruation",
            "dischromic_patches", "watering_from_eyes", "increased_appetite",
            "polyuria", "family_history", "mucoid_sputum", "rusty_sputum",
            "lack_of_concentration", "visual_disturbances",
            "receiving_blood_transfusion", "receiving_unsterile_injections", "coma",
            "stomach_bleeding", "distention_of_abdomen",
            "history_of_alcohol_consumption", "fluid_overload", "blood_in_sputum",
            "prominent_veins_on_calf", "palpitations", "painful_walking",
            "pus_filled_pimples", "blackheads", "scurring", "skin_peeling",
            "silver_like_dusting", "small_dents_in_nails", "inflammatory_nails",
            "blister", "red_sore_around_nose", "yellow_crust_ooze"
        ]

        selected_symptom = tk.StringVar()
        dropdown = ttk.Combobox(symptoms, values=columns, textvariable=selected_symptom)
        dropdown.set("Select a symptom")
        dropdown.pack(pady=10)

        # Create a button to add the selected symptom to the text box
        def add_symptom():
            selected_item = selected_symptom.get()
            if selected_item:
                current_text = text_box.get(1.0, tk.END).strip()
                if current_text:
                    current_text += "\n"
                text_box.delete(1.0, tk.END)
                text_box.insert(tk.END, current_text + selected_item)

        tk.Button(symptoms, text="Add Symptom", command=add_symptom, height=2, width=20, borderwidth=5,
                  bg="black", fg="white").pack(pady=10)

        def final():
            inp = text_box.get(1.0, "end")
            print(inp)
            self.get(inp)

        tk.Button(symptoms, text="Submit", command=final, height=2, width=20, borderwidth=5, bg="black",
                  fg="white").pack(
            pady=10)

        symptoms.mainloop()

    def get(self,inp):
        print(inp)
        words=inp.split()
        print(words)
        ins1=findmatrix()
        ins1.createdf()
        resultmatrix=ins1.predictionmatrix(words)
        print(resultmatrix)

        resultmatrix1=[]
        resultmatrix1.append([resultmatrix])
        ins2=disease_detector()
        ins2.createcsv()
        score=ins2.create_model(resultmatrix)
        # ins2.create_analytics(score)
        # print(score)
        global diagnose
        diagnose=score[0]
        # print(diagnose.strip())
        diagnose_list=[]
        ins3=get_disease_from_symptoms()
        ins3.createcsv()
        diagnose_list.append(diagnose.strip())
        illnesses=ins3.illness_mapping(diagnose_list)
        print(illnesses)
        medicine_data=[]
        for illness in illnesses:
            medicine_data = ins3.get_medicine(illness.lower())
        print(medicine_data)
        # medicinename=ins3.get_medicine(nameaccordingtodata.lower())
        instance = get_prescription_from_medicine()
        instance.createcsv()
        medicinename=""
        tabletname=""
        for i in medicine_data:
            str1=instance.prepare_prescription(i)
            if str1==None:
                # print(str1)
                continue
            if str!=None:
                # print(str1)
                medicinename+=i
                tabletname+=str1
                break

        ins5=create()
        global medstr
        medstr=ins5.method1(medicinename,tabletname)
        print(medstr)

        self.finalsymptoms(score)

    def finalsymptoms(self,score):
        symptoms.destroy()
        global screen12
        screen12=Tk()
        screen12.geometry("1200x800")
        screen12.title("CURE AI")
        screen12.configure(bg='lightblue')
        screen12.iconphoto(False, tk.PhotoImage(file='assets/images/abc1.png'))

        Label(screen12,text="CURE AI", fg='white', bg="darkblue", width="300", height="2",
              font=("orbitron", 35, 'bold')).pack()
        Label(screen12,text="", bg='lightblue').pack()


        wel = Label(screen12, text=f'You have been diagnosed with {score[0].upper()}', fg="red",bg="lightblue",
                    font=('Arial 22 bold'))
        wel.pack()
        df = pd.read_csv("assets/symptom_Description.csv")
        matching_rows = df[df['Disease'].str.contains(score[0])]

        if not matching_rows.empty:
            # Assuming there's only one row for "Drug Reaction", you can get the description
            description = matching_rows['Description'].iloc[0]
            text=description

        else:
            text=" "
        #
        # text_widget = Text(screen, wrap=tk.WORD, width=40, height=10,background="lightblue",borderwidth=0)
        # text_widget.insert(tk.END, text)
        # text_widget.place(x=600,y=400)
        text_widget = scrolledtext.ScrolledText(screen12, wrap=tk.WORD, width=40, height=10,background="lightblue",borderwidth=2,yscrollcommand=None)
        text_widget.insert(tk.END, text)
        text_widget.pack( fill='both')
        letsgo = Button(screen12, text="CONTINUE TO PRESCRIPTION", font="calibri 12",command=self.diagnose_report)
        letsgo.pack()
        screen12.mainloop()

    def write_prescription(self):
        try:
            global name
            print(name)
            global age
            print(age)
            output_path = f"Prescription files/{name}.txt"
            with open("assets/Presciption.txt", 'r') as template_file:
                # Read the template content
                template_content = template_file.read()

                # Replace placeholders with actual values
                template_content = template_content.replace('[FULL_NAME]',name)
                template_content = template_content.replace('[AGE]', age)
                template_content = template_content.replace('[PRESCRIPTION_DETAILS]', medstr)

                # Write the customized prescription to a new file
                with open(output_path, 'w') as output_file:
                    output_file.write(template_content)
                    print(f"Prescription written to {output_path}")
        except FileNotFoundError:
            print(f"File not found: ")
        except Exception as e:
            print(f"An error occurred: {e}")

    def diagnose_report(self):
        screen12.destroy()
        global name
        global age
        screen121 = Tk()
        screen121.geometry("1200x800")
        screen121.title("CURE AI")
        screen121.configure(bg='lightblue')
        screen121.iconphoto(False, tk.PhotoImage(file='assets/images/abc1.png'))

        Label(screen121,text="CURE AI", fg='white', bg="darkblue", width="300", height="2",
              font=("orbitron", 35, 'bold')).pack()
        Label(screen121,text="", bg='lightblue').pack()


        Label(screen121, text=f"Name {name}", fg="#101357", bg="lightblue",
              font=('Arial 14')).pack()

        Label(screen121, text=f"Age {age}", fg="#101357", bg="lightblue",
              font=('Arial 14')).pack()


        wel = Label(screen121, text=f'You have been diagnosed with {diagnose.upper()}', fg="red", bg="lightblue",
                    font=('Arial 22 bold'))
        wel.pack()

        Label(screen121, text='Prescription details', fg="#101357", bg="lightblue",
              font=('Arial 22 bold')).pack()

        Label(screen121, text=medstr, fg="#101357", bg="lightblue",
             font=('Arial 22 bold')).pack()

        def buttonaction():

            self.write_prescription()
            screen121.destroy()
            self.screenend()

        img1 = PhotoImage(file="assets/images/print.png")
        photoimage1 = img1.subsample(3, 3)
        img1Btn = Button(screen121, command=buttonaction, image=photoimage1, bg='lightblue', activebackground='lightblue',
                         relief=FLAT)
        img1Btn.image = photoimage1
        img1Btn.pack()

        screen121.mainloop()

    def screenend(self):
        global countdown
        # Creating the Tkinter window
        screen4 = Tk()
        screen4.geometry("1200x800")
        screen4.title("CURE AI")
        screen4.configure(bg='lightblue')
        screen4.iconphoto(False, tk.PhotoImage(file='assets/images/abc1.png'))

        Label(screen4, text="CURE AI", fg='white', bg="darkblue", width="300", height="2",
              font=("orbitron", 35, 'bold')).pack()
        Label(screen4, text="", bg='lightblue').pack()

        # Load the image with Pillow
        image_path = "assets/images/thankyou.png"  # Replace with the actual path to your image
        image_pil = Image.open(image_path)

        # Convert the image to a Tkinter-compatible format
        image_tk = ImageTk.PhotoImage(image_pil)

        # Create a Label widget to display the image
        image_label = Label(screen4, image=image_tk, bg='lightblue')
        image_label.pack()  # Set relative width and height to fill the entire window

        Label(screen4, text="Thank You Visit Again!", bg='lightblue', width="300", height="2",
              font=("orbitron", 35, 'bold')).pack()
        Label(screen4, text="", bg='lightblue').pack()

        def close_window():
            screen4.destroy()

        def update_countdown():
            global countdown
            countdown -= 1
            label.config(text="This window will close in {} seconds.".format(countdown))
            if countdown > 0:
                screen4.after(1000, update_countdown)
            else:
                close_window()

        # Timeout in seconds
        timeout_duration = 5
        countdown = timeout_duration

        # Create a Label widget
        label = Label(screen4, text="This window will close in {} seconds.".format(countdown), bg="lightblue")
        label.pack(pady=20)

        # Create a Button widget to close the window manually
        button = Button(screen4, text="Close Window", command=close_window)
        button.pack()

        # Set up the countdown timer
        screen4.after(1000, update_countdown)

        # Start the Tkinter event loop
        screen4.mainloop()


def main():

    conn = sqlite3.connect('USER.db')
    create = conn.cursor()
    create.execute(
        'CREATE TABLE IF NOT EXISTS userSignUp(FULLNAME text, AADHARNO text,PIN text)')
    obj=gui(conn,create)
    obj.loginregisteraboutscreen()
    # obj.symptoms()

if __name__ == '__main__':
    main()


