import sqlite3

# 建立與資料庫的連線（如果沒有就會自動建立）
conn = sqlite3.connect('library.db')

# 建立 cursor 來執行 SQL 指令
cursor = conn.cursor()

# 建立資料表 borrow_records
cursor.execute('''
    CREATE TABLE IF NOT EXISTS borrow_records (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT NOT NULL,
        book_id TEXT NOT NULL,
        borrow_date TEXT NOT NULL,
        return_date TEXT NOT NULL
    )
''')

# 儲存變更並關閉連線
conn.commit()
conn.close()

print("✅ 資料庫和資料表建立完成！")
