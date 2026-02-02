# Topshiriq jadvalga foydalanuvchi tomonidan kurs qo'shish(SQL)

import sqlite3

conn = sqlite3.connect("school.db")
cur = conn.cursor()

def add_course():
    title = input("Kurs nomini kiriting>>")
    price = int(input("Kurs narxini kiriting:>>"))
    start_time = input("Boshlanish vaqti:>>")
    end_time = input("Tugash vaqti:>>")
    cur.execute("INSERT INTO course(title, price, statr_time, end_time) VALUES (?, ?, ?, ?)", (title, price, start_time, end_time))
    conn.commit()
    print("Kurs qo`shildi")
    
def get_courses():
    cur.execut("SELECT * FROM course ORDER by id ASC")
    courses = cur.fetchall()
    for info in course:
        print(info)
        
add_course()
get_courses()