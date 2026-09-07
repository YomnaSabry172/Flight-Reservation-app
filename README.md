# ✈️ Flight Reservation App

A simple desktop application for managing flight reservations, built with **Python**, **Tkinter** (GUI), and **SQLite** (database). Book, view, edit, and delete flight reservations through a clean, easy-to-use interface — all data is saved locally and persists between sessions.

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Option 1: Run the Standalone .exe](#option-1-run-the-standalone-exe-windows-only)
  - [Option 2: Run from Source](#option-2-run-from-source)
- [How to Use the App](#-how-to-use-the-app)
- [Database](#-database)
- [Building Your Own .exe](#-building-your-own-exe)
- [License](#-license)

---

## ✨ Features

-  **Book a Flight** — enter passenger name, flight number, departure, destination, date, and seat number
-  **View Reservations** — see every booked reservation in a clean table view
-  **Edit Reservations** — update any existing reservation's details
-  **Delete Reservations** — remove a reservation with a confirmation prompt
-  **Persistent Storage** — all data is saved locally in an SQLite database, so it's still there next time you open the app
-  **Themed UI** — consistent green color scheme, custom fonts, and a navigation bar across every page

---


## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python** | Core programming language |
| **Tkinter** | GUI framework (built into Python — no install needed) |
| **SQLite** (`sqlite3`) | Local database (built into Python — no install needed) |
| **PyInstaller** | Packages the app into a standalone Windows `.exe` |

---

## 📁 Project Structure

```
Flight-Reservation-app/
├── main.py               # App entry point — creates the window, handles page navigation
├── database.py           # All SQLite logic — connect, create table, CRUD functions
├── theme.py               # Shared colors, fonts, and the reusable navigation bar
├── home.py                # Home page — welcome screen with navigation cards
├── booking.py              # Book a Flight page — form to create a new reservation
├── reservations.py         # View Reservations page — table + edit/delete actions
├── edit_reservation.py     # Edit Reservation page — pre-filled form to update a reservation
├── requirements.txt        # Python dependencies
├── .gitignore              # Files/folders excluded from version control
└── README.md                # You are here
```

---

## 🚀 Getting Started

### Option 1: Run the Standalone `.exe` (Windows only)

No Python installation required.

1. Go to the [**Releases**](../../releases) page of this repository
2. Download the latest `main.exe`
3. Double-click to run

That's it — the app will create its own `flights.db` file next to the `.exe` on first launch.

### Option 2: Run from Source

**Requirements:** Python 3.10+ (Tkinter and SQLite come built-in with Python — nothing extra to install for these two)

```bash
# 1. Clone the repository
git clone https://github.com/YomnaSabry172/Flight-Reservation-app.git
cd Flight-Reservation-app

# 2. (Recommended) Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python main.py
```

---

## 🧭 How to Use the App

1. **Home Page** — choose between "Book a Flight" or "View Reservations"
2. **Book a Flight** — fill in all six fields (Name, Flight Number, Departure, Destination, Date, Seat Number) and click **Book Flight**
3. **View Reservations** — every saved reservation appears in the table:
   - Select a row → click **Edit Selected** to modify it
   - Select a row → click **Delete Selected** to remove it (a confirmation popup will appear first)
4. **Edit Reservation** — the form pre-fills with the selected reservation's current data; update any field and click **Update**

---

## 🗄️ Database

The app uses a single SQLite database file, `flights.db`, automatically created on first run in the same folder as the app. It contains one table:

**`reservations`**

| Column | Type | Description |
|--------|------|--------------|
| `id` | INTEGER (Primary Key, Auto Increment) | Unique reservation ID |
| `name` | TEXT | Passenger name |
| `flight_number` | TEXT | Flight number |
| `departure` | TEXT | Departure location |
| `destination` | TEXT | Destination location |
| `date` | TEXT | Flight date |
| `seat_number` | TEXT | Seat number |

> `flights.db` is excluded from version control via `.gitignore` — each user/installation generates their own fresh copy.

---

## 📦 Building Your Own `.exe`

If you'd like to build the executable yourself instead of downloading it from Releases:

```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

The finished executable will be created at `dist/main.exe`.

**Flag reference:**
- `--onefile` — bundles everything into a single `.exe` file
- `--windowed` — suppresses the background console window, so only the Tkinter GUI appears


---

## 📄 License

This project was created as part of the **Sprints Program**. Feel free to fork and build on it for learning purposes.

---

<p align="center">Built with 🐍 Python + Tkinter + SQLite</p>
