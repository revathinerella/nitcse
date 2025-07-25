import tkinter as tk
from tkinter import ttk

def generate_invitation():
    groom = groom_name.get()
    bride = bride_name.get()
    date = wedding_date.get()
    time = wedding_time.get()
    venue = wedding_venue.get()

    invitation_text.set(
        f"You're Invited!\n\n"
        f"{groom} & {bride}\n"
        f"Request the honour of your presence\n"
        f"On {date} at {time}\n"
        f"Venue: {venue}\n\n"
        f"We look forward to celebrating with you!"
    )

app = tk.Tk()
app.title("Wedding Invitation Generator")
app.geometry("500x600")


groom_name = tk.StringVar()
bride_name = tk.StringVar()
wedding_date = tk.StringVar()
wedding_time = tk.StringVar()
wedding_venue = tk.StringVar()
invitation_text = tk.StringVar()

title_label = ttk.Label(app, text="Wedding Invitation Generator", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

ttk.Label(app, text="Groom's Name").pack(pady=5)
ttk.Entry(app, textvariable=groom_name).pack()

ttk.Label(app, text="Bride's Name").pack(pady=5)
ttk.Entry(app, textvariable=bride_name).pack()

ttk.Label(app, text="Wedding Date").pack(pady=5)
ttk.Entry(app, textvariable=wedding_date).pack()

ttk.Label(app, text="Wedding Time").pack(pady=5)
ttk.Entry(app, textvariable=wedding_time).pack()

ttk.Label(app, text="Venue").pack(pady=5)
ttk.Entry(app, textvariable=wedding_venue).pack()

ttk.Button(app, text="Generate Invitation", command=generate_invitation).pack(pady=20)

invitation_label = ttk.Label(app, textvariable=invitation_text, wraplength=400, justify="center", font=("Serif", 12))
invitation_label.pack(pady=20)

app.mainloop()
