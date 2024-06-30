import sys
import tkinter as tk
from tkinter import messagebox
import subprocess

# Checks If Set Up
if not vars.setup
    tk.messagebox("Run setup.py", "Fill In The Info")
    os.system("python setup.py")
    sys.exit()

def trigger_sender():
    subprocess.run(["python", "sender.py"])
    sys.exit()

def trigger_receiver():
    subprocess.run(["python", "receiver.py"])
    sys.exit()
def on_select_role():
    role = role_var.get()
    if role == "Sender":
        trigger_sender()
    elif role == "Receiver":
        trigger_receiver()
    else:
        messagebox.showwarning("Selection Error", "Please select a role.")
    sys.exit()
# Create the main window
root = tk.Tk()
root.title("Role Selector")

# Create a StringVar to hold the selected role
role_var = tk.StringVar(value="")

# Create radio buttons for selecting the role
sender_rb = tk.Radiobutton(root, text="Sender", variable=role_var, value="Sender")
receiver_rb = tk.Radiobutton(root, text="Receiver", variable=role_var, value="Receiver")

# Create a button to trigger the selected role's script
trigger_button = tk.Button(root, text="Start", command=on_select_role)

# Pack the widgets
sender_rb.pack(anchor="w")
receiver_rb.pack(anchor="w")
trigger_button.pack()

# Run the application
root.mainloop()
