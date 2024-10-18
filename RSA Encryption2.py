import tkinter as tk
from tkinter import *
from tkinter import messagebox
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
        if e < 3 or e >= phi_n or math.gcd(e, phi_n) != 1 or math.gcd(e, n) != 1:
            messagebox.showerror("Error", "e is invalid. It should be coprime with phi(n) and n.")
            return

        # Check d
        if (d * e) % phi_n != 1:
            messagebox.showerror("Error", "d is incorrect. (d * e) % phi(n) should be 1.")
            return

        messagebox.showinfo("Success", "All inputs are valid!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

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
root.title("RSA Encryption")
root.geometry("1010x750")  # Set the window to exactly 1010x750 pixels
root.resizable (False, False)
root.config(bg="#0F3555")  # Background color to blue

#ASSETS
eimage = PhotoImage(file="Rectangle.png")
containerImage = PhotoImage(file="Container.png")
buttonImage = PhotoImage(file="Button.png")

# Add the "RSA" title along with credits text
credit_Text = "\tCreated by: \n@Omar Abdulrahman Al Mayouf\n@Fares Essa Al Duhailan\n@Abdulaziz Abdulrahman Al Khonefer \n@Abdulrahman Ibrahim Al Saadan"
lable_credits = Label(root, text=credit_Text, font=("Segoe UI", 12, "italic"), bg="#0F3555", fg="#B4B4B4", justify="left")
lable_credits.place(x=0,y=0)
label_title = tk.Label(root, text="RSA", font=("Segoe UI", 78, "bold italic"), bg="#0F3555", fg="white")
label_title.pack(pady=20)  # Add some padding for title

# Create a white container from the "Container.png" image
container = Label(root,image=containerImage, border=40, bg="#0F3555")
container.pack_propagate(False)  # Prevent the frame from resizing to its content
container.pack(pady=10)  # Center the container vertically


# For the next lines creating a set of input fields with placeholders inside and a button in the container


entrylabel = Label(container, image=eimage, border=0) # creating the label image for the entry
entrylabel.place(x=43,y=43/2) # placing the label on the container
entry_p = Entry(container,width=111,border=0,font=('bold',11), bg="#0F3555",fg="white") # creating the entry field itself on the label
entry_p.place(x=43+20,y=43/2+12) # placing the entry on the label
add_placeholder(entry_p, "Please enter a prime number p:  ") # adding the placeholder into the entry

entrylabel = Label(container, image=eimage, border=0)
entrylabel.place(x=43,y=43/2+65)
entry_q = Entry(container,width=111,border=0,font=('bold',11), bg="#0F3555",fg="white")
entry_q.place(x=43+20,y=43/2+65+12)
add_placeholder(entry_q, "Please enter a prime number q:  ")

entrylabel = Label(container, image=eimage, border=0)
entrylabel.place(x=43,y=43/2+65*2)
entry_n = Entry(container,width=111,border=0,font=('bold',11), bg="#0F3555",fg="white")
entry_n.place(x=43+20,y=43/2+65*2+12)
add_placeholder(entry_n, "Please enter (n):  ")

entrylabel = Label(container, image=eimage, border=0)
entrylabel.place(x=43,y=43/2+65*3)
entry_phi_n = Entry(container,width=111,border=0,font=('bold',11), bg="#0F3555",fg="white")
entry_phi_n.place(x=43+20,y=43/2+65*3+12)
add_placeholder(entry_phi_n, "Please enter phi(n):  ")

entrylabel = Label(container, image=eimage, border=0)
entrylabel.place(x=43,y=43/2+65*4)
entry_e = Entry(container,width=111,border=0,font=('bold',11), bg="#0F3555",fg="white")
entry_e.place(x=43+20,y=43/2+65*4+12)
add_placeholder(entry_e, "Please enter e:  ")

entrylabel = Label(container, image=eimage, border=0)
entrylabel.place(x=43,y=43/2+65*5)
entry_d = Entry(container,width=111,border=0,font=('bold',11), bg="#0F3555",fg="white")
entry_d.place(x=43+20,y=43/2+65*5+12)
add_placeholder(entry_d, "Please enter d:  ")

sumbitButton = Button(container, image=buttonImage, command=validate_inputs, border=0, background="white") # creating the button
sumbitButton.place(x=250,y=43/2+65*6) # placing the button


if __name__ == "__main__":
    root.mainloop()