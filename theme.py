import tkinter as tk

PRIMARY = "#2e7d32"
PRIMARY_DARK = "#1b5e20"
BG = "#f4f7f4"
CARD_BG = "#ffffff"
TEXT_GRAY = "#666666"
BORDER = "#c8d6c8"

FONT_FAMILY = "Segoe UI"
FONT_HEADING = (FONT_FAMILY, 22, "bold")
FONT_SUBHEADING = (FONT_FAMILY, 15, "bold")
FONT_BODY = (FONT_FAMILY, 11)
FONT_BODY_BOLD = (FONT_FAMILY, 11, "bold")
FONT_SMALL = (FONT_FAMILY, 10)
FONT_BUTTON = (FONT_FAMILY, 11)
FONT_NAV = (FONT_FAMILY, 11)
FONT_NAV_BOLD = (FONT_FAMILY, 11, "bold")
FONT_LOGO = (FONT_FAMILY, 14, "bold")

def build_navbar(parent, controller, active_page):
    from home import HomePage
    from booking import BookingPage
    from reservations import ReservationsPage

    navbar = tk.Frame(parent, bg=PRIMARY, height=55)
    navbar.pack(fill="x", side="top")

    tk.Label(navbar, text="✈ FlySky Reservations", bg=PRIMARY, fg="white",
             font=FONT_LOGO).pack(side="left", padx=20, pady=14)

    links = [("Home", HomePage), ("Book Flight", BookingPage), ("View Reservations", ReservationsPage)]
    for text, page in reversed(links):
        is_active = (text == active_page)
        link = tk.Label(navbar, text=text, bg=PRIMARY, cursor="hand2",
                         fg="#c8e6c9" if is_active else "white",
                         font=FONT_NAV_BOLD if is_active else FONT_NAV)
        link.pack(side="right", padx=15, pady=14)
        link.bind("<Button-1>", lambda e, p=page: controller.show_frame(p))