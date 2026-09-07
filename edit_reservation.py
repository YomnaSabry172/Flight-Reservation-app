import tkinter as tk
from tkinter import messagebox
import database
import theme

class EditReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=theme.BG)
        self.controller = controller
        self.current_id = None
        theme.build_navbar(self, controller, "Edit Reservation")

        tk.Label(self, text="Edit Reservation", bg=theme.BG, fg=theme.PRIMARY_DARK,
                 font=theme.FONT_HEADING).pack(pady=(30, 20), anchor="center")

        card = tk.Frame(self, bg=theme.CARD_BG, highlightbackground=theme.BORDER,
                         highlightthickness=1, padx=35, pady=30)
        card.pack()

        labels = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        self.entries = {}
        for i, label in enumerate(labels):
            tk.Label(card, text=label, bg=theme.CARD_BG, font=theme.FONT_BODY_BOLD
                     ).grid(row=i, column=0, sticky="w", pady=(10, 2))
            entry = tk.Entry(card, width=40, relief="solid", borderwidth=1, font=theme.FONT_BODY)
            entry.grid(row=i, column=1, pady=(10, 2), padx=(15, 0))
            self.entries[label] = entry

        btns = tk.Frame(card, bg=theme.CARD_BG)
        btns.grid(row=len(labels), column=1, sticky="e", pady=(20, 0))
        tk.Button(btns, text="Cancel", relief="solid", borderwidth=1,
                  font=theme.FONT_BUTTON, command=self.go_back).pack(side="left", padx=5)
        tk.Button(btns, text="Update", bg=theme.PRIMARY, fg="white",
                  relief="flat", font=theme.FONT_BUTTON, command=self.update).pack(side="left")

    def load(self, reservation_id):
        self.current_id = reservation_id
        row = database.get_reservation(reservation_id)
        fields = ["Name", "Flight Number", "Departure", "Destination", "Date", "Seat Number"]
        for field, value in zip(fields, row[1:]):
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, value)

    def update(self):
        values = [self.entries[label].get() for label in self.entries]
        if not all(values):
            messagebox.showerror("Error", "All fields are required.")
            return
        database.update_reservation(self.current_id, *values)
        messagebox.showinfo("Success", "Reservation updated.")
        self.go_back()

    def go_back(self):
        from reservations import ReservationsPage
        self.controller.show_frame(ReservationsPage)