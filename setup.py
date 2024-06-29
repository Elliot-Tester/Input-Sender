import tkinter as tk
from tkinter import ttk

def write_to_file(file_path, text):
    try:
        with open(file_path, 'w') as file:
            file.write(text)
        print(f"Successfully wrote to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def submit():
    vc_id = vc_id_entry.get()
    sender_token = sender_token_entry.get()
    receiver_token = receiver_token_entry.get()
    write_to_file("vc_id.py", f"vc_id = {vc_id} # Setup Complete")
    write_to_file("sender_token.py", f"token=\"{sender_token}\"")
    write_to_file("receiver_token.py", f"token=\"{receiver_token}\"")
# Create main window
root = tk.Tk()
root.title("Setup")

# Create labels and entry boxes
vc_id_label = ttk.Label(root, text="VC ID:")
vc_id_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

vc_id_entry = ttk.Entry(root, width=40)
vc_id_entry.grid(row=0, column=1, padx=10, pady=10)

sender_token_label = ttk.Label(root, text="Sender Token:")
sender_token_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

sender_token_entry = ttk.Entry(root, width=40)
sender_token_entry.grid(row=1, column=1, padx=10, pady=10)

receiver_token_label = ttk.Label(root, text="Receiver Token:")
receiver_token_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

receiver_token_entry = ttk.Entry(root, width=40)
receiver_token_entry.grid(row=2, column=1, padx=10, pady=10)

# Submit button
submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, columnspan=2, pady=10)

# Start GUI
root.mainloop()
