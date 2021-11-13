import sqlite3, os
from pprint import pprint
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

master = tk.Tk()
path = os.getenv('APPDATA')

def op():
    path = 'C:\ViberNumber'
    os.startfile(path, 'open')
    
def normal_viwi(result):
    final=[]
    for i in result:
        if isinstance(i,tuple):
            final.extend(normal_viwi(i))
        else:
            final.append(i)

    return final
def get_info():
    try:
        data = str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + '.txt'
        if not os.path.exists("C:\ViberNumber"):
            os.makedirs("C:\ViberNumber") 
        con = sqlite3.connect(f'{path}/ViberPC/{number.get()}/viber.db')
        cur = con.cursor()
        cur.execute( f'SELECT "Number" FROM "Contact" WHERE "ContactID" IN (SELECT "ContactID" FROM "ChatRelation" WHERE "ChatID" = (SELECT "ChatID" FROM "ChatInfo" WHERE "Name" = "{group.get()}") )')
        result = cur.fetchall()
        for s in normal_viwi(result):
            with open(f"C:\ViberNumber\{data}", "a") as f:
               f.write(s + '\n')
        messagebox.showinfo(f"Успіх", f"Номери успішно збережено у C:\ViberNumber\{data}")
    except Exception as e:
        print("Не правильно введені дані")
        messagebox.showerror("ERROR", "Не правильно введені дані")

master.iconbitmap("icon.ico")
master.title("Парсинг номерів")
master.geometry('240x80')
master.eval('tk::PlaceWindow . center')
master.resizable(width=False, height=False)
tk.Label(master, 
         text="Номер телефону").grid(row=0)
tk.Label(master, 
         text="Назва групи").grid(row=1)

number = tk.Entry(master)
group = tk.Entry(master)

number.grid(row=0, column=1)
group.grid(row=1, column=1)

tk.Button(master, text="Відкрити папку", command=op).grid(row=3, 
                                                       column=0, 
                                                       sticky=tk.W, 
                                                       pady=4)

tk.Button(master, 
          text='Знайти', command=get_info).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)

    
tk.mainloop()