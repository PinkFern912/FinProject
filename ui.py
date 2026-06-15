# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem,
    QStackedWidget
)
from PyQt5.QtCore import QDate, QTimer
from db import add_expense, get_expenses, get_balance

class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Фінансовий проєкт")
        self.resize(800, 500)

        # === Бокове меню ===
        self.menu_layout = QVBoxLayout()
        self.btn_add = QPushButton("Додати витрату")
        self.btn_view = QPushButton("Переглянути витрати")
        self.btn_balance = QPushButton("Баланс")
        self.btn_stats = QPushButton("Статистика")

        self.menu_layout.addWidget(self.btn_add)
        self.menu_layout.addWidget(self.btn_view)
        self.menu_layout.addWidget(self.btn_balance)
        self.menu_layout.addWidget(self.btn_stats)
        self.menu_layout.addStretch()

        # === Сторінки (canvas) ===
        self.pages = QStackedWidget()

        # Сторінка додавання витрати
        self.page_add = QWidget()
        add_layout = QVBoxLayout()
        self.category_input = QLineEdit()
        self.amount_input = QLineEdit()
        self.date_input = QLineEdit()
        self.date_input.setText(QDate.currentDate().toString("yyyy-MM-dd"))
        self.save_button = QPushButton("Зберегти витрату")
        self.save_button.clicked.connect(self.save_expense)
        add_layout.addWidget(QLabel("Категорія:"))
        add_layout.addWidget(self.category_input)
        add_layout.addWidget(QLabel("Сума:"))
        add_layout.addWidget(self.amount_input)
        add_layout.addWidget(QLabel("Дата:"))
        add_layout.addWidget(self.date_input)
        add_layout.addWidget(self.save_button)
        self.page_add.setLayout(add_layout)

        # Сторінка перегляду витрат
        self.page_view = QWidget()
        view_layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Категорія", "Сума", "Дата"])
        view_layout.addWidget(self.table)
        self.page_view.setLayout(view_layout)

        # Сторінка балансу
        self.page_balance = QWidget()
        balance_layout = QVBoxLayout()
        self.balance_label = QLabel("Баланс: 0.00")
        balance_layout.addWidget(self.balance_label)
        self.page_balance.setLayout(balance_layout)

        # Сторінка статистики
        self.page_stats = QWidget()
        stats_layout = QVBoxLayout()
        self.stats_label = QLabel("Статистика буде тут")
        stats_layout.addWidget(self.stats_label)
        self.page_stats.setLayout(stats_layout)

        # Додаємо сторінки у QStackedWidget
        self.pages.addWidget(self.page_add)
        self.pages.addWidget(self.page_view)
        self.pages.addWidget(self.page_balance)
        self.pages.addWidget(self.page_stats)

        # === Основний Layout ===
        main_layout = QHBoxLayout()
        main_layout.addLayout(self.menu_layout, 1)
        main_layout.addWidget(self.pages, 4)
        self.setLayout(main_layout)

        # === Прив'язка кнопок до сторінок ===
        self.btn_add.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_add))
        self.btn_view.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_view))
        self.btn_balance.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_balance))
        self.btn_stats.clicked.connect(lambda: self.pages.setCurrentWidget(self.page_stats))

        # Таймер для автооновлення
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.auto_update)
        self.timer.start(3000)

    def save_expense(self):
        try:
            category = self.category_input.text()
            amount = float(self.amount_input.text())
            date = self.date_input.text()
            add_expense(category, amount, date)
            QMessageBox.information(self, "Успіх", "Витрата збережена!")
            self.show_expenses()
        except Exception as e:
            QMessageBox.critical(self, "Помилка", str(e))

    def show_expenses(self):
        data = get_expenses()
        self.table.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def show_balance(self):
        balance = get_balance()
        self.balance_label.setText(f"Баланс: {balance}")

    def show_statistics(self):
        data = get_expenses()
        total_expenses = sum([row[2] for row in data]) if data else 0
        self.stats_label.setText(f"Загальні витрати: {total_expenses}")

    def auto_update(self):
        self.show_expenses()
        self.show_balance()
        self.show_statistics()

def run_app():
    app = QApplication(sys.argv)
    window = ExpenseApp()
    window.show()
    sys.exit(app.exec_())
