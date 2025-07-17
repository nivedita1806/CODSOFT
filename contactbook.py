import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []  # Global list to store contacts

# Add Contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showwarning("Missing Info", "Name and phone are required!")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    update_contact_list()
    clear_entries()

# View Contacts
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Search Contact
def search_contact():
    keyword = search_entry.get().strip().lower()
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            contact_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# Delete Contact
def delete_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        del contacts[index]
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("No Selection", "Please select a contact to delete.")

# Update Contact
def update_contact():
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        contact['name'] = name_entry.get().strip()
        contact['phone'] = phone_entry.get().strip()
        contact['email'] = email_entry.get().strip()
        contact['address'] = address_entry.get().strip()
        update_contact_list()
        clear_entries()
    else:
        messagebox.showwarning("No Selection", "Select a contact to update.")

# Fill entries when selecting a contact
def on_select(event):
    selected = contact_listbox.curselection()
    if selected:
        index = selected[0]
        contact = contacts[index]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, contact['name'])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact['phone'])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, contact['email'])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, contact['address'])

# Clear input fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x600")
root.configure(bg="#f7faff")

tk.Label(root, text="Contact Book", font=("Arial", 18, "bold"), bg="#f7faff").pack(pady=10)

# Input Fields
frame = tk.Frame(root, bg="#f7faff")
frame.pack(pady=5)

tk.Label(frame, text="Name:", bg="#f7faff").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(frame, width=40)
name_entry.grid(row=0, column=1, pady=2)

tk.Label(frame, text="Phone:", bg="#f7faff").grid(row=1, column=0, sticky="w")
phone_entry = tk.Entry(frame, width=40)
phone_entry.grid(row=1, column=1, pady=2)

tk.Label(frame, text="Email:", bg="#f7faff").grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(frame, width=40)
email_entry.grid(row=2, column=1, pady=2)

tk.Label(frame, text="Address:", bg="#f7faff").grid(row=3, column=0, sticky="w")
address_entry = tk.Entry(frame, width=40)
address_entry.grid(row=3, column=1, pady=2)

# Buttons
button_frame = tk.Frame(root, bg="#f7faff")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add", width=10, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update", width=10, command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete", width=10, command=delete_contact).grid(row=0, column=2, padx=5)

# Search
tk.Label(root, text="Search by Name or Phone:", bg="#f7faff").pack(pady=5)
search_entry = tk.Entry(root, width=40)
search_entry.pack()
tk.Button(root, text="Search", command=search_contact).pack(pady=5)

# Contact List Display
contact_listbox = tk.Listbox(root, width=60, height=10)
contact_listbox.pack(pady=10)
contact_listbox.bind('<<ListboxSelect>>', on_select)

# Show All Button
tk.Button(root, text="Show All Contacts", command=update_contact_list).pack(pady=5)

root.mainloop()
