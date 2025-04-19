from doctest import debug

from flask import Flask, render_template, request  # type: ignore

app = Flask(__name__)

# 首頁，顯示一個按鈕導向 /borrow
@app.route('/')
def index():
    return render_template('index.html')

# 顯示借書表單
@app.route('/borrow', methods=['GET'])
def borrow_form():
    return render_template('borrow_form.html')

# 接收表單資料
@app.route('/borrow', methods=['POST'])
def borrow_submit():
    user_id = request.form.get('user_id')
    book_id = request.form.get('book_id')
    borrow_date = request.form.get('borrow_date')
    return_date = request.form.get('return_date')

    # 這裡可以寫入資料庫或檔案紀錄
    print(f"使用者 {user_id} 借了書籍 {book_id}，從 {borrow_date} 到 {return_date}")

    return f"借書成功！使用者 {user_id} 借了書 {book_id}，請在 {return_date} 前歸還。"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
