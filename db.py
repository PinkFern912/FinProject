# -*- coding: utf-8 -*-
import psycopg2
import os
from dotenv import load_dotenv

# завантажуємо змінні з .env
load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )


# Додавання витрати
def add_expense(category, amount, date):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO expenses (category, amount, date) VALUES (%s, %s, %s)",
        (category, amount, date)
    )
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Витрата додана:", category, amount, date)

# Отримати всі витрати
def get_expenses():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses ORDER BY date DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# Отримати баланс
def get_balance():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT total FROM balance ORDER BY id DESC LIMIT 1")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return result[0] if result else 0.0

# Тестовий запуск
if __name__ == "__main__":
    # Перевірка з'єднання
    try:
        conn = get_connection()
        print("✅ Підключення успішне!")
        conn.close()
    except Exception as e:
        print("❌ Помилка:", e)

    # Додавання прикладу витрати
    add_expense("Food", 250.50, "2026-06-15")

    # Вивід усіх витрат
    print(get_expenses())

    # Вивід балансу
    print("Баланс:", get_balance())
