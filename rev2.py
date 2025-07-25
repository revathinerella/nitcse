import tkinter as tk
from tkinter import messagebox

def generate_invitation():
    name = entry_name.get()
    event = entry_event.get()
    date = entry_date.get()
    time = entry_time.get()
    venue = entry_venue.get()

    if not all([name, event, date, time, venue]):
        messagebox.showerror("Missing Information", "Please fill all fields.")
        return

    invitation_text.delete("1.0", tk.END)

    invitation = (
        f"\n👑 You Are Invited! 👑\n\n"
        f"Dear {name},\n\n"
        f"You are cordially invited to the {event}.\n\n"
        f"📅 Date: {date}\n"
        f"🕒 Time: {time}\n"
        f"📍 Venue: {venue}\n\n"
        f"We look forward to celebrating with you!\n"
        f"🎉🎊🎈"
    )

    invitation_text.insert(tk.END, invitation)

def clear_fields():
    for entry in entries:
        entry.delete(0, tk.END)
    invitation_text.delete("1.0", tk.END)

root = tk.Tk()
root.title("Colorful Invitation Generator")
root.geometry("600x600")
root.configure(bg="orange")

title_label =tk.Label(root,text=" Invitation Generator", font=("Comic Sans MS", 20, "bold"))

title_label.pack(pady=10)

form_frame = tk.Frame(root, bg="green")
form_frame.pack(pady=10)

labels = ["Recipient Name", "Event", "Date", "Time", "Venue"]
entries = []

for idx, label_text in enumerate(labels):
    label = tk.Label(form_frame, text=label_text, font=("Arial", 12, "bold"), bg="pink")
    label.grid(row=idx, column=0, sticky="e", pady=5, padx=5)
    entry = tk.Entry(form_frame, font=("Arial", 12), width=30)
    entry.grid(row=idx, column=1, pady=5)
    entries.append(entry)

entry_name, entry_event, entry_date, entry_time, entry_venue = entries

generate_btn = tk.Button(root,text="Generate Invitation",command=generate_invitation, font=("Arial", 12, "bold"), bg="red",fg="white",padx=10,pady=5)
generate_btn.pack(pady=5)

clear_btn = tk.Button(root,text="Clear",command=clear_fields,font=("Arial", 12, "bold"),bg="gray",fg="white",padx=10, pady=5)
clear_btn.pack(pady=5)

invitation_text = tk.Text(root,height=12,width=60,font=("Georgia", 12),bg="white",fg="black")
invitation_text.pack(pady=10)

root.mainloop()
