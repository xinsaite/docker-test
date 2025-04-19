from flask import Flask, render_template, request, redirect, url_for
import sqlite3

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
    user_id = request.form['user_id']
    book_id = request.form['book_id']
    borrow_date = request.form['borrow_date']
    return_date = request.form['return_date']

    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO borrow_records (user_id, book_id, borrow_date, return_date)
        VALUES (?, ?, ?, ?)
    ''', (user_id, book_id, borrow_date, return_date))
    conn.commit()
    conn.close()

    return f"借書成功！使用者 {user_id} 借了書 {book_id}，請在 {return_date} 前歸還。"

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
