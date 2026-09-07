import tkinter as tk
from database import create_table
from home import HomePage
from booking import BookingPage
from reservations import ReservationsPage
from edit_reservation import EditReservationPage

class FlightApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flight Reservation App")
        self.geometry("900x600")
        self.minsize(700, 450)

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for PageClass in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            frame = PageClass(container, self)
            self.frames[PageClass] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        if hasattr(frame, "refresh"):
            frame.refresh()
        frame.tkraise()

if __name__ == "__main__":
    create_table()
    app = FlightApp()
    app.mainloop()