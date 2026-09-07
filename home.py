import tkinter as tk
from booking import BookingPage
from reservations import ReservationsPage
import theme

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg=theme.BG)
        self.controller = controller
        theme.build_navbar(self, controller, "Home")

        tk.Label(self, text="Welcome to FlySky Reservations", bg=theme.BG,
                 fg=theme.PRIMARY_DARK, font=theme.FONT_HEADING).pack(pady=(35, 5), anchor="center")
        tk.Label(self, text="Book your flights and manage your reservations.",
                 bg=theme.BG, fg=theme.TEXT_GRAY, font=theme.FONT_BODY).pack(pady=(0, 30), anchor="center")

        cards = tk.Frame(self, bg=theme.BG)
        cards.pack(anchor="center")
        self.build_card(cards, 0, "Book a Flight",
                         "Reserve your next flight with your details.",
                         "Book Flight", lambda: controller.show_frame(BookingPage))
        self.build_card(cards, 1, "View Reservations",
                         "Manage, edit, or cancel existing reservations.",
                         "View Reservations", lambda: controller.show_frame(ReservationsPage))

    def build_card(self, parent, column, title, description, button_text, command):
        card = tk.Frame(parent, bg=theme.CARD_BG, highlightbackground=theme.BORDER,
                         highlightthickness=1, padx=25, pady=25)
        card.grid(row=0, column=column, padx=15)
        tk.Label(card, text=title, bg=theme.CARD_BG, fg=theme.PRIMARY_DARK,
                 font=theme.FONT_SUBHEADING).pack(pady=(0, 8))
        tk.Label(card, text=description, bg=theme.CARD_BG, fg=theme.TEXT_GRAY,
                 font=theme.FONT_BODY, wraplength=200, justify="center").pack(pady=(0, 15))
        tk.Button(card, text=button_text, bg=theme.PRIMARY, fg="white",
                  activebackground=theme.PRIMARY_DARK, relief="flat",
                  font=theme.FONT_BUTTON, width=18, command=command).pack()