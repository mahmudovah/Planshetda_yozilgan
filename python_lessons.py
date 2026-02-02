print("Planshet termuxida yozilgan kodlar")

# SQL bilan ishlash

import sqlite3

conn = sqlite3.connect("school.db")
cur = conn.cursor()

def add_student():
    full_name = input("Ism kiriting>>")
    age = int(input("Yoshini kiriting:>>"))
    phone_number = input("Telefon raqamini kiriting:>>")
    cur.execute("INSERT INTO students(full_name, age, phone_number) VALUES (?, ?, ?)", (full_name, age, phone_number))
    conn.commit()
    print("O'quvchi qo`shildi")
    
def get_students():
    cur.execute("SELECT * FROM students ORDER by id DESC LIMIT 10")
    students = cur.fetchall()
    for student in students:
        print(student)
        
add_student()
get_students()