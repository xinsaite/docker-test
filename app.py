from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# 顯示借書表單
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/borrow', methods=['GET'])
def borrow_form():
    return render_template('borrow_form.html')

@app.route('/borrow', methods=['POST'])
def borrow_submit():
    user_id = request.form.get('user_id')
    book_id = request.form.get('book_id')
    borrow_date = request.form.get('borrow_date')
    return_date = request.form.get('return_date')

    # 寫入 SQLite
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO borrow_records (user_id, book_id, borrow_date, return_date)
        VALUES (?, ?, ?, ?)
    ''', (user_id, book_id, borrow_date, return_date))
    conn.commit()
    conn.close()

    # 顯示成功頁，並在 borrow_success.html 中設定 3 秒後跳回首頁
    return render_template('borrow_success.html', user_id=user_id, book_id=book_id, return_date=return_date)

# ✅ 顯示所有借書紀錄
@app.route('/records')
def view_records():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM borrow_records')
    records = cursor.fetchall()
    conn.close()
    return render_template('records.html', records=records)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
