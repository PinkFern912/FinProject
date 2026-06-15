# FinProject

A financial project for managing personal expenses and balance using **PostgreSQL** and **PyQt5**.

---

## 📌 Changelog

### 16.06.2026
#### – Database Setup
- Initialized PostgreSQL database `finproject`.
- Added tables:
  - `expenses` (id, category, amount, date)
  - `balance` (id, total)

#### – Python Integration
- Configured `db.py` to work with PostgreSQL via `psycopg2`.
- Implemented functions:
  - `add_expense()` — add a new expense.
  - `get_expenses()` — retrieve expense list.
  - `get_balance()` — retrieve current balance.

#### – Interface (PyQt5)
- Created a basic window with form:
  - Fields: Category, Amount, Date.
  - Button: “Save expense”.
- Added a table to view expenses.
- Added a button to view balance.

#### – Auto Update
- Implemented `QTimer` for automatic data refresh every few seconds.
- Expense table and balance update without manual action.

#### – Sidebar Menu
- Added **sidebar navigation** with multiple canvases:
  - Add expense
  - View expenses
  - Balance
  - Statistics
- Used `QStackedWidget` for switching between pages.

#### – Security
- Moved credentials to `.env` file.
- Added `.gitignore` to exclude `.env` from GitHub.
- Used `python-dotenv` for configuration loading.

---

## 📌 Future Plans

### Analytics & Visualization
- Charts for expenses by category (matplotlib).
- Dynamic trend graphs (daily/weekly/monthly).
- Balance visualization and forecasting.

### Export & Integrations
- Export data to CSV, XLSX, PDF.
- Integration with Google Sheets.
- REST API for mobile/web clients.

### Extended Statistics
- Top expense categories with percentages.
- Average expenses per day/week/month.
- Period comparison and anomaly detection.

### User Features
- User authentication (login/password).
- Multiple profiles (family budget).
- Role management (admin, member).
- Currency and exchange rate settings.

### Interface
- Update design to **Cybertech style**.
- Dark/light theme support.
- Mobile screen adaptation.
- Sidebar with additional modules (income, investments).
- Drag‑and‑drop CSV import.

### Automation
- Auto balance update when adding expenses.
- Reminders for recurring payments.
- Budget planning with overspending alerts.
- Push notifications for important changes.

### Financial Services Integration
- Connect to banking APIs for transaction import.
- Sync with payment systems (PayPal, Revolut, Monobank).
- Investment portfolio module (stocks, crypto).
- Automatic currency rate updates.
