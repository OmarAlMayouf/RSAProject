import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import math

# Define your functions
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

def validate_inputs():
    try:
        p = int(entry_p.get())
        q = int(entry_q.get())
        n = int(entry_n.get())
        phi_n = int(entry_phi_n.get())
        e = int(entry_e.get())
        d = int(entry_d.get())

        # Check prime numbers
        if not is_prime(p) or not is_prime(q):
            messagebox.showerror("Error", "Both p and q must be prime numbers.")
            return

        # Check n
        if n != p * q:
            messagebox.showerror("Error", "n is incorrect. It should be p * q.")
            return

        # Check phi(n)
        if phi_n != (p - 1) * (q - 1):
            messagebox.showerror("Error", "phi(n) is incorrect.")
            return

        # Check e
        if e < 2 or e >= phi_n or math.gcd(e, phi_n) != 1 or math.gcd(e, n) != 1:
            messagebox.showerror("Error", "e is invalid. It should be coprime with phi(n) and n.")
            return

        # Check d
        if (d * e) % phi_n != 1:
            messagebox.showerror("Error", "d is incorrect. (d * e) % phi(n) should be 1.")
            return

        messagebox.showinfo("Success", "All inputs are valid!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")


def encrypt_message():
    try:
        result.config(state=tk.NORMAL)  # Enable editing temporarily
        result.delete(1.0, tk.END)  # Clear the text box
        message = entry_message.get()
        p = int(entry_p2.get())
        q = int(entry_q2.get())
        n = int(entry_n2.get())
        phi_n = int(entry_phi_n2.get())
        e = int(entry_e2.get())
        # Check prime numbers
        if not is_prime(p) or not is_prime(q):
            result.configure(fg="red")
            result.insert(tk.END, "*Error, Both p and q must be prime numbers.")
            return

        # Check n
        if n != p * q:
            result.configure(fg="red")
            result.insert(tk.END, "*Error, n is incorrect. It should be p * q.")
            return

        # Check phi(n)
        if phi_n != (p - 1) * (q - 1):
            result.configure(fg="red")
            result.insert(tk.END, "*Error, phi(n) is incorrect.")
            return

        # Check e
        if e < 2 or e >= phi_n or math.gcd(e, phi_n) != 1 or math.gcd(e, n) != 1:
            result.configure(fg="red")
            result.insert(tk.END, "*Error, e is invalid. It should be coprime with phi(n) and n.")
            return

        # Convert the message to numbers and encrypt
        encrypted_message = [pow(ord(char), e, n) for char in message]
        
        result.configure(fg="#6D6D6D")
        result.insert(tk.END, f"Result: {encrypted_message}")
        result.config(state=tk.DISABLED)
    except Exception as ex:
        result.config(state=tk.NORMAL)  # Enable editing temporarily
        result.delete(1.0, tk.END)  # Clear the text box
        result.configure(fg="red")
        result.insert(tk.END, "*Error, Please enter valid inputs.")
        result.config(state=tk.DISABLED)

def decrypt_message():
    try:
        result2.config(state=tk.NORMAL)  # Enable editing temporarily
        result2.delete(1.0, tk.END)  # Clear the text box
        ciphertext = entry_cypher.get()
        p = int(entry_p3.get())
        q = int(entry_q3.get())
        n = int(entry_n3.get())
        phi_n = int(entry_phi_n3.get())
        e = int(entry_e3.get())
        d = int(entry_d2.get())
        # Check prime numbers
        if not is_prime(p) or not is_prime(q):
            result2.configure(fg="red")
            result2.insert(tk.END, "*Error, Both p and q must be prime numbers.")
            return

        # Check n
        if n != p * q:
            result2.configure(fg="red")
            result2.insert(tk.END, "*Error, n is incorrect. It should be p * q.")
            return

        # Check phi(n)
        if phi_n != (p - 1) * (q - 1):
            result2.configure(fg="red")
            result2.insert(tk.END, "*Error, phi(n) is incorrect.")
            return
        
        # Check e
        if e < 2 or e >= phi_n or math.gcd(e, phi_n) != 1 or math.gcd(e, n) != 1:
            result2.configure(fg="red")
            result2.insert(tk.END, "*Error, e is invalid. It should be coprime with phi(n) and n.")
            return
        # Check d
        if (d * e) % phi_n != 1:
            result2.configure(fg="red")
            result2.insert(tk.END, "*Error, d is incorrect. (d * e) % phi(n) should be 1.")
            return
        # Convert the ciphertext to numbers and decrypt
        encrypted_list = eval(ciphertext)
        decrypted_message = ''.join([chr(pow(char, d, n)) for char in encrypted_list])
        
        result2.configure(fg="#6D6D6D")
        result2.insert(tk.END, f"Result: {decrypted_message}")
        result2.config(state=tk.DISABLED)
    except Exception as ex:
        result2.config(state=tk.NORMAL)  # Enable editing temporarily
        result2.delete(1.0, tk.END)  # Clear the text box
        result2.configure(fg="red")
        result2.insert(tk.END, "*Error, Please enter valid inputs.")
        result2.config(state=tk.DISABLED)

# Placeholder behavior
def add_placeholder(entry, placeholder_text):
    placeholder_with_margin = ' ' * 3 + placeholder_text  # placeholder has a 30px margin to the left from the label itself
    entry.insert(0, placeholder_with_margin)
    entry.config(fg='white', font=("Segoe UI", 10, "bold"))  # Placeholder font style

    def on_focus_in(event):
        if entry.get().strip() == placeholder_with_margin.strip():
            entry.delete(0, tk.END) # starting from index 0 to the end of the string delete it
            entry.config(fg='white', font=("Segoe UI", 10, "bold"))

    def on_focus_out(event):
        if entry.get().strip() == '':
            entry.insert(0, placeholder_with_margin)
            entry.config(fg='white', font=("Segoe UI", 10, "bold"))

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


# Create the main window
root = Tk()
root.title("RSA")
root.iconbitmap("icon.ico")
root.geometry("800x700")  # Set the window size
root.resizable (False, False)
root.config(bg="#0F3555")  # Background color to blue

# IMAGE ASSETS
eimage = PhotoImage(file="Rectangle.png")
e2image = PhotoImage(file="RectangleBig.png")
containerImage = PhotoImage(file="Container.png")
containerImage2 = PhotoImage(file="Container2.png")
buttonImage = PhotoImage(file="Button.png")
buttonImage2 = PhotoImage(file="Button2.png")
buttonImage3 = PhotoImage(file="Button3.png")
mainImage = PhotoImage(file="mainImage.png")

# Add the credits text
credit_Text = "\n\tCreated by: \n@Omar Abdulrahman Al Mayouf\n@Fares Essa Al Duhailan\n@Abdulaziz Abdulrahman Al Khonefer \n@Abdulrahman Ibrahim Al Saadan"
lable_credits = Label(root, text=credit_Text, font=("Segoe UI", 11, "italic"), bg="#0F3555", fg="#B4B4B4", justify="left")
lable_credits.place(x=20, y=0)

# Add the "RSA" title
label_title = tk.Label(root, text="RSA", font=("Segoe UI", 65, "bold italic"), bg="#0F3555", fg="white")
label_title.pack(pady=10)  # Add some padding for title

# Create the main image(the security image) for the root
main_image = Label(root, image=mainImage, border=0)
main_image.place(x=600, y=30)

# Create a notebook and style them
style = ttk.Style()
style.theme_use('classic')
style.configure('TNotebook', background="#0F3555")

style.configure('TNotebook.Tab', background='#0f3555', foreground='white', font=('Segoe UI', 11, 'italic'), border=0)
style.map("TNotebook.Tab", background = [("selected", "#ffffff")], foreground = [("selected", "black")], font = [("selected", ('Segoe UI', 14, 'bold'))])

notebook = ttk.Notebook(root, style="TNotebook")
notebook.pack(pady=0, padx=0, fill="x")

# Create three tabs
tab1 = Frame(notebook, bg="#0F3555")
tab2 = Frame(notebook, bg="#0F3555")
tab3 = Frame(notebook, bg="#0F3555")

# Add the tabs to the notebook
notebook.add(tab1, text="Validate")
notebook.add(tab2, text="Encrypt")
notebook.add(tab3, text="Decrypt")

# Create a white container from the "Container.png" image for tab1
container1 = Label(tab1, image=containerImage, border=20, bg="#0F3555")
container1.pack_propagate(False)
container1.pack(pady=70)

# Create a white container from the "Container2.png" image for tab2
container2 = Label(tab2, image=containerImage2, border=20, bg="#0F3555")
container2.pack_propagate(False)
container2.pack(pady=10)

# Create a white container from the "Container2.png" image for tab3
container3 = Label(tab3, image=containerImage2, border=20, bg="#0F3555")
container3.pack_propagate(False)
container3.pack(pady=10)
############################################################################################################################################################
# For tab1 input fields with placeholders

#dummy entry
dummy = Entry(container1, bg="white", fg="white", border=0)
dummy.place(x=30, y=43/2)

entrylabel = Label(container1, image=eimage, border=0)
entrylabel.place(x=30, y=43/2)
entry_p = Entry(container1, width=87, border=0, font=('bold', 11), bg="#0F3555", fg="white")
entry_p.place(x=30+20, y=43/2+6)
add_placeholder(entry_p, "Please enter a prime number p:  ")

entrylabel = Label(container1, image=eimage, border=0)
entrylabel.place(x=30, y=43/2+45)
entry_q = Entry(container1, width=87, border=0, font=('bold', 11), bg="#0F3555", fg="white")
entry_q.place(x=30+20, y=43/2+45+6)
add_placeholder(entry_q, "Please enter a prime number q:  ")

entrylabel = Label(container1, image=eimage, border=0)
entrylabel.place(x=30, y=43/2+45*2)
entry_n = Entry(container1, width=87, border=0, font=('bold', 11), bg="#0F3555", fg="white")
entry_n.place(x=30+20, y=43/2+45*2+6)
add_placeholder(entry_n, "Please enter (n):  ")

entrylabel = Label(container1, image=eimage, border=0)
entrylabel.place(x=30, y=43/2+45*3)
entry_phi_n = Entry(container1, width=87, border=0, font=('bold', 11), bg="#0F3555", fg="white")
entry_phi_n.place(x=30+20, y=43/2+45*3+6)
add_placeholder(entry_phi_n, "Please enter phi(n):  ")

entrylabel = Label(container1, image=eimage, border=0)
entrylabel.place(x=30, y=43/2+45*4)
entry_e = Entry(container1, width=87, border=0, font=('bold', 11), bg="#0F3555", fg="white")
entry_e.place(x=30+20, y=43/2+45*4+6)
add_placeholder(entry_e, "Please enter e:  ")

entrylabel = Label(container1, image=eimage, border=0)
entrylabel.place(x=30, y=43/2+45*5)
entry_d = Entry(container1, width=87, border=0, font=('bold', 11), bg="#0F3555", fg="white")
entry_d.place(x=30+20, y=43/2+45*5+6)
add_placeholder(entry_d, "Please enter d:  ")

sumbitButton1 = Button(container1, image=buttonImage, command=validate_inputs, border=0, background="white")
sumbitButton1.place(x=220, y=43/2+45*6)
####################################################################################################################################################
# Similar layout for tab2 (almost same as tab1)

#dummy entry
dummy = Entry(container2, bg="white", fg="white", border=0)
dummy.place(x=30, y=43/2)

entrylabel = Label(container2, image=e2image, border=0, background="white")
entrylabel.place(x=30, y=43/2)
entry_message = Entry(container2, width=87, border=0, font=('bold', 11), bg="#0F3555", fg="white")
entry_message.place(x=30+20, y=43/2+12)
add_placeholder(entry_message, "Please enter a message:  ")

entrylabel = Label(container2, image=eimage, border=0)
entrylabel.place(x=30, y=43/2+120)
entry_p2 = Entry(container2, width=87, border=0, font=('bold', 11), bg="#0F3555", fg="white")
entry_p2.place(x=30+20, y=43/2+120+6)
add_placeholder(entry_p2, "Please enter a prime number p:  ")

entrylabel = Label(container2, image=eimage, border=0)
entrylabel.place(x=30,y=43/2+120+45)
entry_q2 = Entry(container2,width=87,border=0,font=('bold',11), bg="#0F3555",fg="white")
entry_q2.place(x=30+20,y=43/2+120+45+6)
add_placeholder(entry_q2, "Please enter a prime number q:  ")

entrylabel = Label(container2, image=eimage, border=0)
entrylabel.place(x=30,y=43/2+120+45*2)
entry_n2 = Entry(container2,width=87,border=0,font=('bold',11), bg="#0F3555",fg="white")
entry_n2.place(x=30+20,y=43/2+120+45*2+7)
add_placeholder(entry_n2, "Please enter (n):  ")

entrylabel = Label(container2, image=eimage, border=0)
entrylabel.place(x=30,y=43/2+120+45*3)
entry_phi_n2 = Entry(container2,width=87,border=0,font=('bold',11), bg="#0F3555",fg="white")
entry_phi_n2.place(x=30+20,y=43/2+120+45*3+6)
add_placeholder(entry_phi_n2, "Please enter phi(n):  ")

entrylabel = Label(container2, image=eimage, border=0)
entrylabel.place(x=30,y=43/2+120+45*4)
entry_e2 = Entry(container2,width=87,border=0,font=('bold',11), bg="#0F3555",fg="white")
entry_e2.place(x=30+20,y=43/2+120+45*4+6)
add_placeholder(entry_e2, "Please enter e:  ")

result = Text(container2, font=("Segoe UI", 11, 'bold'), bg="white", fg="#6D6D6D", width=72, height=2, border=0)
result.insert(tk.END, "Result: ")
result.config(state=tk.DISABLED)
result.place(x=30,y=43/2+120+45*5)

sumbitButton2 = Button(container2, image=buttonImage2, command=encrypt_message, border=0, background="white")
sumbitButton2.place(x=220, y=43/2+120+45*6)
####################################################################################################################################################
# Similar layout for tab3 (same as tab2)

#dummy entry
dummy = Entry(container3, bg="white", fg="white", border=0)
dummy.place(x=30, y=43/2)

entrylabel = Label(container3, image=e2image, border=0, background="white")
entrylabel.place(x=30, y=43/2)
entry_cypher = Entry(container3, width=87, border=0, font=('bold', 11), bg="#0F3555", fg="white")
entry_cypher.place(x=30+20, y=43/2+12)
add_placeholder(entry_cypher, "Please enter the cypher text:  ")

entrylabel = Label(container3, image=eimage, border=0)
entrylabel.place(x=30, y=43/2+120)
entry_p3 = Entry(container3, width=87, border=0, font=('bold', 11), bg="#0F3555", fg="white")
entry_p3.place(x=30+20, y=43/2+120+6)
add_placeholder(entry_p3, "Please enter a prime number p:  ")

entrylabel = Label(container3, image=eimage, border=0)
entrylabel.place(x=30,y=43/2+120+45)
entry_q3 = Entry(container3,width=87,border=0,font=('bold',11), bg="#0F3555",fg="white")
entry_q3.place(x=30+20,y=43/2+120+45+6)
add_placeholder(entry_q3, "Please enter a prime number q:  ")

entrylabel = Label(container3, image=eimage, border=0)
entrylabel.place(x=30,y=43/2+120+45*2)
entry_n3 = Entry(container3,width=87,border=0,font=('bold',11), bg="#0F3555",fg="white")
entry_n3.place(x=30+20,y=43/2+120+45*2+7)
add_placeholder(entry_n3, "Please enter (n):  ")

entrylabel = Label(container3, image=eimage, border=0)
entrylabel.place(x=30,y=43/2+120+45*3)
entry_phi_n3 = Entry(container3,width=87,border=0,font=('bold',11), bg="#0F3555",fg="white")
entry_phi_n3.place(x=30+20,y=43/2+120+45*3+6)
add_placeholder(entry_phi_n3, "Please enter phi(n):  ")

entrylabel = Label(container3, image=eimage, border=0)
entrylabel.place(x=30,y=43/2+120+45*4)
entry_e3 = Entry(container3,width=87,border=0,font=('bold',11), bg="#0F3555",fg="white")
entry_e3.place(x=30+20,y=43/2+120+45*4+6)
add_placeholder(entry_e3, "Please enter e:  ")

entrylabel = Label(container3, image=eimage, border=0)
entrylabel.place(x=30,y=43/2+120+45*5)
entry_d2 = Entry(container3,width=87,border=0,font=('bold',11), bg="#0F3555",fg="white")
entry_d2.place(x=30+20,y=43/2+120+45*5+6)
add_placeholder(entry_d2, "Please enter d:  ")

result2 = Text(container3, font=("Segoe UI", 11, 'bold'), bg="white", fg="#6D6D6D", width=47, height=2, border=0)
result2.insert(tk.END, "Result: ")
result2.config(state=tk.DISABLED)
result2.place(x=30,y=43/2+120+45*6)

sumbitButton2 = Button(container3, image=buttonImage3, command=decrypt_message, border=0, background="white")
sumbitButton2.place(x=450, y=43/2+120+45*6-5)
if __name__ == "__main__":
    root.mainloop()