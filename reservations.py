import tkinter as tk
from tkinter import ttk, messagebox
import database
import theme

class ReservationsPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=theme.BG)
        self.controller = controller
        theme.build_navbar(self, controller, "View Reservations")

        top = tk.Frame(self, bg=theme.BG)
        top.pack(fill="x", padx=40, pady=(25, 10))
        tk.Label(top, text="Your Reservations", bg=theme.BG, fg=theme.PRIMARY_DARK,
                 font=theme.FONT_HEADING).pack(side="left")
        tk.Button(top, text="Book New Flight", bg=theme.PRIMARY, fg="white",
                  relief="flat", font=theme.FONT_BUTTON, command=self.go_booking).pack(side="right")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background=theme.PRIMARY, foreground="white",
                         font=theme.FONT_BODY_BOLD)
        style.configure("Treeview", font=theme.FONT_BODY, rowheight=28)

        columns = ("id", "name", "flight_number", "departure", "destination", "date", "seat_number")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col.replace("_", " ").title())
        self.tree.pack(fill="both", expand=True, padx=40, pady=10)

        btn_frame = tk.Frame(self, bg=theme.BG)
        btn_frame.pack(pady=8)
        tk.Button(btn_frame, text="Edit Selected", font=theme.FONT_BUTTON,
                  command=self.edit_selected).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Delete Selected", font=theme.FONT_BUTTON,
                  command=self.delete_selected).pack(side="left", padx=5)

    def refresh(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for reservation in database.get_all_reservations():
            self.tree.insert("", "end", values=reservation)

    def get_selected_id(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("No selection", "Select a reservation first.")
            return None
        return self.tree.item(selected[0])["values"][0]

    def edit_selected(self):
        reservation_id = self.get_selected_id()
        if reservation_id is None:
            return
        from edit_reservation import EditReservationPage
        page = self.controller.frames[EditReservationPage]
        page.load(reservation_id)
        self.controller.show_frame(EditReservationPage)

    def delete_selected(self):
        reservation_id = self.get_selected_id()
        if reservation_id is None:
            return
        if messagebox.askyesno("Confirm", "Delete this reservation?"):
            database.delete_reservation(reservation_id)
            self.refresh()

    def go_booking(self):
        from booking import BookingPage
        self.controller.show_frame(BookingPage)