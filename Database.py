#!/usr/bin/python3-32
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog
from shutil import copyfile
import sqlite3
import json
import random
import datetime
import os


class DatabaseUI():
    """class GUI data base"""
    def __init__(self, parent):
        self.parent = parent
        self.folder_1 = os.getcwd()
        self.filedb_name = 'db_test.sqlite'
        self.tree_header = ['named', 'type', 'number', 'date', 'place', 'service', 'date_serv', 'date_repair', 'description', 'id']
        self.img0 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\opendb.png')
        self.img1 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\add.png')
        self.img2 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\trash.png')
        self.img3 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\edit.png')
        self.img4 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\settings.png')
        self.img5 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\info.png')
        self.img6 = tk.PhotoImage(file=f'{self.folder_1}\\icon\\exit.png')

        with open(f'{self.folder_1}\\setting_test.json','r', encoding='utf-8') as file_json:
            self.setting_json = json.load(file_json)

        self.name_col1 = self.setting_json['name_col1']
        self.name_col2 = self.setting_json['name_col2']
        self.name_col3 = self.setting_json['name_col3']
        self.name_col4 = self.setting_json['name_col4']
        self.name_col5 = self.setting_json['name_col5']
        self.name_col6 = self.setting_json['name_col6']
        self.name_col7 = self.setting_json['name_col7']
        self.name_col8 = self.setting_json['name_col8']
        self.name_col9 = self.setting_json['name_col9']
        self.name_tab1 = self.setting_json['name_tab1']
        self.name_tab2 = self.setting_json['name_tab2']
        self.name_tab3 = self.setting_json['name_tab3']
        self.name_tab4 = self.setting_json['name_tab4']
        self.name_place = self.setting_json['name_place']
        self.name_service = self.setting_json['name_service']

        self.level = 0
        self.named = tk.StringVar()
        self.type = tk.StringVar()
        self.number = tk.StringVar()
        self.date = tk.StringVar()
        self.place = tk.StringVar()
        self.service = tk.StringVar()
        self.date_serv = tk.StringVar()
        self.date_repair = tk.StringVar()
        self.description = tk.StringVar()
        self.main_id = tk.StringVar()
        self.today = datetime.datetime.today()
        self.data_today = self.today.strftime('%d.%m.%Y,%H.%M.%S')
        self.table_db = 'equipment'
        self.widget_frame()
        self.widget_button()
        self.widget_tree()
        self.read_db(self.table_db)
        self.widget_combobox()
        self.tree_bind()
        parent.title('Database')
        parent.geometry('1200x800')
        parent.protocol("WM_DELETE_WINDOW", self.on_closing)   # tray menu
        parent.trayMenu = None

        main_menu = tk.Menu(parent)
        parent.config(menu=main_menu)
        file_menu = tk.Menu(main_menu, tearoff=False)
        file_menu.add_command(label='Новая запись', command=self.win_add)
        file_menu.add_separator()
        file_menu.add_command(label='Закрыть', command=parent.quit)

        file_setting = tk.Menu(main_menu, tearoff=False)
        file_setting.add_command(label='Настройки', command = self.setting_win)
        file_setting.add_command(label='Backup DB', command=self.backup)

        main_menu.add_cascade(label='Файл', menu=file_menu)
        main_menu.add_cascade(label='Настройки', menu=file_setting)

    def backup(self):
        """Create backup .sqlite"""
        copyfile(f'{self.folder_1}\\{self.filedb_name}', f'{self.folder_1}\\backup\\{self.filedb_name}')
        self.statusbar.config(text="Backup done")

    def connect_db(self, file_name):
        """connect with file .sqlite"""
        self.connectdb = sqlite3.connect(f'{self.folder_1}\\{file_name}')
        self.cursor = self.connectdb.cursor()

    def open_db(self):
        """Open file .sqlite"""
        file_select = filedialog.askopenfilenames(parent=self.parent, initialdir=f'{self.folder_1}\\',
            initialfile='', filetypes=[("sqlite", "*.sqlite"),("All files", "*")])
        try:
            self.filedb_name = file_select[0].split('/')[3]
            self.read_db(self.table_db)
        except IndexError:
            pass

    def setting_win(self):
        """window setting programm"""
        top = tk.Toplevel(self.parent, bg='alice blue')
        top.geometry('550x400')
        top.resizable(0, 0)
        top.title('Настройки')

        top_1 = tk.Frame(top, bg='alice blue', height=400, relief="raise")
        top_1.pack(side='top', fill='x')

        lf1 = tk.LabelFrame(top_1, text='Название столбцов', width=200, height=300, bg='alice blue')
        lf1.place(x=5, y=5)
        lf2 = tk.LabelFrame(top_1, text='Название таблиц', width=330, height=300, bg='alice blue')
        lf2.place(x=205, y=5)

        tree_col1 = tk.Entry(lf1, font='10')
        tree_col1.place(x=5,y=5)
        tree_col2 = tk.Entry(lf1, font='10')
        tree_col2.place(x=5,y=35)
        tree_col3 = tk.Entry(lf1, font='10')
        tree_col3.place(x=5,y=65)
        tree_col4 = tk.Entry(lf1, font='10')
        tree_col4.place(x=5,y=95)
        tree_col5 = tk.Entry(lf1, font='10')
        tree_col5.place(x=5,y=125)
        tree_col6 = tk.Entry(lf1, font='10')
        tree_col6.place(x=5,y=155)
        tree_col7 = tk.Entry(lf1, font='10')
        tree_col7.place(x=5,y=185)
        tree_col8 = tk.Entry(lf1, font='10')
        tree_col8.place(x=5,y=215)
        tree_col9 = tk.Entry(lf1, font='10')
        tree_col9.place(x=5,y=245)
        tree_tab1= tk.Entry(lf2,width=35,font='10')
        tree_tab1.place(x=5,y=5)
        tree_tab2= tk.Entry(lf2,width=35, font='10')
        tree_tab2.place(x=5,y=35)
        tree_tab3= tk.Entry(lf2,width=35, font='10')
        tree_tab3.place(x=5,y=65)
        tree_tab4= tk.Entry(lf2,width=35, font='10')
        tree_tab4.place(x=5,y=95)

        tree_col1.insert(0, self.name_col1)
        tree_col2.insert(0, self.name_col2)
        tree_col3.insert(0, self.name_col3)
        tree_col4.insert(0, self.name_col4)
        tree_col5.insert(0, self.name_col5)
        tree_col6.insert(0, self.name_col6)
        tree_col7.insert(0, self.name_col7)
        tree_col8.insert(0, self.name_col8)
        tree_col9.insert(0, self.name_col9)
        tree_tab1.insert(0, self.name_tab1)
        tree_tab2.insert(0, self.name_tab2)
        tree_tab3.insert(0, self.name_tab3)
        tree_tab4.insert(0, self.name_tab4)

        def set_ok():
            self.setting_json['name_col1'] = tree_col1.get()
            self.setting_json['name_col2'] = tree_col2.get()
            self.setting_json['name_col3'] = tree_col3.get()
            self.setting_json['name_col4'] = tree_col4.get()
            self.setting_json['name_col5'] = tree_col5.get()
            self.setting_json['name_col6'] = tree_col6.get()
            self.setting_json['name_col7'] = tree_col7.get()
            self.setting_json['name_col8'] = tree_col8.get()
            self.setting_json['name_col9'] = tree_col9.get()
            self.setting_json['name_tab1'] = tree_tab1.get()
            self.setting_json['name_tab2'] = tree_tab2.get()
            self.setting_json['name_tab3'] = tree_tab3.get()
            self.setting_json['name_tab4'] = tree_tab4.get()

            with open(f'{self.folder_1}\\setting.json', 'w', encoding='utf-8') as file_json:
                json.dump(self.setting_json, file_json, ensure_ascii=False, indent=4, sort_keys=True)

            self.parent.destroy()
            os.system(f'{self.folder_1}\\DatabaseKIA.py')

        butok = tk.Button(top_1, text='OK', width=10, command=set_ok)
        butok.place(x=230,y=330)
        butok.configure(bg="#6699CC", fg='white', highlightbackground="#0CD9E8", highlightcolor="#0DFFCC",font=("Times New Roman", 15, "bold"))

    def about_win(self):
        """window about programm"""
        top = tk.Toplevel(self.parent, bg='alice blue')
        top.geometry('310x280')
        top.resizable(0, 0)
        top.title('О программе')

        text1 = ('Data Base v1.02\rDate: 2022-08-01\rAutor: g1enden, I T L ©')
        text2 = (f'Состав базы данных:\r{self.name_tab1}\r{self.name_tab2}\r{self.name_tab3}\r{self.name_tab4}')

        top_1 = tk.Frame(top, bg='alice blue', height=60, relief="raise")
        top_1.pack(side='top', fill='x')
        top_2 = tk.Frame(top, bg='alice blue', height=200, relief="raise")
        top_2.pack(side='top', fill='x')

        autor = tk.Label(top_1, bg='alice blue', text=text1)
        autor.place(x=60,y=10)
        support = tk.Label(top_2, bg='alice blue', text=text2, font='10')
        support.place(x=5,y=5)
        butok = tk.Button(top_2, text='OK', width=10, command=top.destroy)
        butok.place(x=90,y=150)
        butok.configure(bg="#6699CC", fg='white', highlightbackground="#0CD9E8", highlightcolor="#0DFFCC",font=("Times New Roman", 15, "bold"))

    def on_closing(self):
        """transfer in tray menu"""
        if not self.parent.trayMenu:
            selection = tkMessageBox.askyesnocancel("ВНИМАНИЕ!", "Закрыть программу?\nДа: Закрыть\nНет: Свернуть в системный трей")
            if selection:
                self.parent.destroy()
            elif selection is False:
                self.parent.withdraw()
                self.parent.tk.call('package', 'require', 'Winico')
                icon = self.parent.tk.call('winico', 'createfrom', f'{self.folder_1}\\icon\\icon.ico')
                self.parent.tk.call('winico', 'taskbar', 'add', icon,
                            '-callback', (self.parent.register(self.menu_tray), '%m', '%x', '%y'),
                            '-pos', 0,
                            '-text', 'Database-KIA')

                self.parent.trayMenu = tk.Menu(self.parent, tearoff=False)
                self.parent.trayMenu.add_command(label="Открыть", command=self.parent.deiconify)
                cascademenu = tk.Menu(self.parent, tearoff=False)
                cascademenu.add_command(label="Casacde one", command=lambda :print("You could define it by yourroot"))
                cascademenu.add_command(label="Cascade two")
                self.parent.trayMenu.add_cascade(label="Другое", menu=cascademenu)
                self.parent.trayMenu.add_separator()
                self.parent.trayMenu.add_command(label="Закрыть", command=self.parent.destroy)
            else:
                pass
        else:
            self.parent.withdraw()

    def menu_tray(self, event, x, y):
        """event press in trey menu"""
        if event == 'WM_RBUTTONDOWN':
            self.parent.trayMenu.tk_popup(x, y)
        if event == 'WM_LBUTTONDOWN':
            self.parent.deiconify()

    def widget_frame(self):
        """main window"""
        self.frame_panel = tk.Frame(self.parent)
        self.frame_panel.pack(side='top', fill='x')
        self.frame_bottom = tk.Frame(self.parent)
        self.frame_bottom.pack(side='bottom', fill='x')
        self.frame_left = tk.Frame(self.parent, width=270, height=300)
        self.frame_left.propagate(False)
        self.frame_left.pack(side='left', fill='y')
        frame_top = tk.Frame(self.parent, width=600, height=100)
        frame_top.pack(side='top', fill='x')
        self.frame_combo_top = tk.Frame(frame_top, bg="deepskyblue3", width=600, height=100, bd=1, relief="raise")
        self.frame_combo_top.pack(side='top', fill='x')
        self.frame_tree_top = tk.Frame(frame_top, bg="deepskyblue3", width=600, height=100, bd=1, relief="raise")
        self.frame_tree_top.pack(side='top', fill='x')
        self.statusbar = tk.Label(self.frame_bottom, width=143, fg="white", bg="deepskyblue3", font=("Arial", 10, "bold"), anchor='w')
        self.statusbar.pack(side='left')
        statusbar_1 = tk.Label(self.frame_bottom, width=100, text="I T L ©", fg="white", bg="deepskyblue3", font=("Arial", 10, "bold"), anchor='e')
        statusbar_1.pack(side='right', fill='x')

    def widget_tree(self):
        """widget treeview left and top"""
        self.tree_left = ttk.Treeview(self.frame_left, show='tree', selectmode='browse')
        fr_y1 = tk.Frame(self.frame_left)
        fr_y1.pack(side='right', fill='y')
        tk.Label(fr_y1, borderwidth=1, relief='raised', font='Arial 8').pack(side='bottom', fill='x')
        sb_y1 = tk.Scrollbar(fr_y1, orient='vertical', command=self.tree_left.yview)
        sb_y1.pack(expand='yes', fill='y')
        fr_x1 = tk.Frame(self.frame_left)
        fr_x1.pack(side='bottom', fill='x')
        sb_x1 = tk.Scrollbar(fr_x1, orient='horizontal', command=self.tree_left.xview)
        sb_x1.pack(expand='yes', fill='x')
        self.tree_left.heading('#0', text='Dep', anchor='w')
        self.tree_left.insert('', tk.END, text=self.name_tab1, iid=0, open=False)
        self.tree_left.insert('', tk.END, text=self.name_tab2, iid=1, open=False)
        self.tree_left.insert('', tk.END, text=self.name_tab3, iid=2, open=False)
        self.tree_left.insert('', tk.END, text=self.name_tab4, iid=3, open=False)
        self.tree_left.column('#0', width=250)
        self.tree_left.configure(yscrollcommand=sb_y1.set, xscrollcommand=sb_x1.set)
        self.tree_left.pack(fill='both', expand='yes')

        self.tree_top = ttk.Treeview(self.frame_tree_top, columns=self.tree_header[0:6], height=400)
        fr_y2 = tk.Frame(self.frame_tree_top)
        fr_y2.pack(side='right', fill='y')
        tk.Label(fr_y2, borderwidth=1, relief='raised', font='Arial 8').pack(side='bottom', fill='x')
        sb_y2 = tk.Scrollbar(fr_y2, orient='vertical', command=self.tree_top.yview)
        sb_y2.pack(side='right', fill='y')
        sb_x2 = tk.Scrollbar(self.frame_tree_top, orient='horizontal', command=self.tree_top.xview)
        sb_x2.pack(side='bottom', fill='x')
        self.tree_top.heading('#0', text='№', anchor='w')
        self.tree_top.heading('named', text=self.name_col1, anchor='w')
        self.tree_top.heading('type', text=self.name_col2, anchor='w')
        self.tree_top.heading('number', text=self.name_col3, anchor='w')
        self.tree_top.heading('date', text=self.name_col4, anchor='w')
        self.tree_top.heading('place', text=self.name_col5, anchor='w')
        self.tree_top.heading('service', text=self.name_col6, anchor='w')
        self.tree_top.column('#0', stretch=False, minwidth=40, width=40)
        self.tree_top.column('named', width=50)
        self.tree_top.column('type', width=50)
        self.tree_top.column('number', width=50)
        self.tree_top.column('date', width=50)
        self.tree_top.column('place', width=50)
        self.tree_top.column('service', width=50)
        self.tree_top.configure(yscrollcommand=sb_y2.set, xscrollcommand=sb_x2.set)
        self.tree_top.pack(fill='both', expand='yes')

    def tree_bind(self):
        """widget treeview event"""
        self.tree_top.bind("<Double-1>", self.select_item_tree_top)
        self.tree_top.bind("<Return>", self.select_item_tree_top)
        self.tree_left.bind("<Return>", self.select_item_tree_left)
        self.tree_left.bind("<Double-1>", self.select_item_tree_left)

        for col in self.tree_header[0:6]:
            self.tree_top.heading(col, command=lambda c=col: tree, anchor='w')
            self.tree_top.column(col, width=140, anchor='w')

    def widget_button(self):
        """panel button"""
        btn_opendb = tk.Button(self.frame_panel, image=self.img0, command=self.open_db)
        btn_opendb.pack(side='left', fill='x')
        btn_add = tk.Button(self.frame_panel, image=self.img1, command=self.win_add)
        btn_add.pack(side='left', fill='x')
        btn_del = tk.Button(self.frame_panel, image=self.img2, command=self.delete_write)
        btn_del.pack(side='left', fill='x')
        btn_edit = tk.Button(self.frame_panel, image=self.img3, command=lambda: self.select_item_tree_top("<Return>"))
        btn_edit.pack(side='left', fill='x')
        btn_sett = tk.Button(self.frame_panel, image=self.img4, command=self.setting_win)
        btn_sett.pack(side='left', fill='x')
        btn_info = tk.Button(self.frame_panel, image=self.img5, command=self.about_win)
        btn_info.pack(side='left', fill='x')
        btn_exit = tk.Button(self.frame_panel, image=self.img6, command=self.parent.quit)
        btn_exit.pack(side='left', fill='x')

    def widget_combobox(self):
        """comboboxs"""
        self.filters = []
        frame_y = tk.Frame(self.frame_combo_top)
        frame_y.pack(side='right', fill='x')
        tk.Label(self.frame_combo_top, borderwidth=1, text='           ', relief='raised', font="Arial 8").pack(side='left', fill='x')
        for col in self.tree_header[0:6]:
            name = f'combo_{col}'
            self.filters.append(name)
            setattr(self.frame_combo_top, name, ttk.Combobox(self.frame_combo_top, values=[''] + sorted(set(x[col] for x in self.list_fet)), state="readonly"))
            getattr(self.frame_combo_top, name).pack(side="left", expand=True, fill='x')
            getattr(self.frame_combo_top, name).bind('<<ComboboxSelected>>', self.select_from_filters)
        tk.Label(frame_y, borderwidth=1, text='     ', relief='raised', font="Arial 8").pack(side='left', fill='x')

    def select_from_filters(self, event=None):
        """filter treeview"""
        self.tree_top.delete(*self.tree_top.get_children())
        all_filter = lambda x: all(x[f.split('_')[-1]] == getattr(self.frame_combo_top, f).get() or getattr(self.frame_combo_top, f).get() == '' for f in self.filters)
        var1 = 0
        for row in self.list_fet:
            if all_filter(row):
                if (len(row) - var1) % 2 == 0:
                    self.tree_top.insert('', index=var1, text=var1+1, values=list(row.values()), tags=('oddrow',))
                    self.tree_top.tag_configure('oddrow', background='alice blue')
                else:
                    self.tree_top.insert('', index=var1, text=var1+1, values=list(row.values()), tags=('evenrow',))
                    self.tree_top.tag_configure('evenrow', background='mint cream')
                var1 += 1

    def update_combobox(self):
        """event update combbox"""
        for col in self.tree_header[0:6]:
            name = f'combo_{col}'
            getattr(self.frame_combo_top, name).configure(values=[''] + sorted(set(x[col] for x in self.list_fet)))

    def database(self):
        """connect with datebase and create cursor"""
        self.connect_db(self.filedb_name)
        self.cursor.execute("CREATE TABLE IF NOT EXISTS brp (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, named TEXT, type TEXT, number TEXT, date TEXT, place TEXT, service TEXT, date_serv TEXT, date_repair TEXT, description TEXT, id TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS equipment (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, named TEXT, type TEXT, number TEXT, date TEXT, place TEXT, service TEXT, date_serv TEXT, date_repair TEXT, description TEXT, id TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS measuring (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, named TEXT,type TEXT, number TEXT, date TEXT, place TEXT, service TEXT, date_serv TEXT, date_repair TEXT, description TEXT, id TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS certification (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, named TEXT,type TEXT, number TEXT, date TEXT, place TEXT, service TEXT, date_serv TEXT, date_repair TEXT, description TEXT, id TEXT)")
        #self.cursor.close()

    def read_db(self, name_table):
        """load datebase in ui"""
        self.list_fet = []
        self.dict_fet = {}
        self.tree_top.delete(*self.tree_top.get_children())
        self.database()
        self.cursor.execute(f"SELECT * FROM {name_table} ORDER BY type ASC")
        fetch = self.cursor.fetchall()
        self.cursor.execute(f"SELECT name FROM sqLite_master WHERE type='table' AND name='{name_table}'")
        self.table_name = self.cursor.fetchall()

        for i2, data in enumerate(fetch):
            if (len(fetch) - i2) % 2 == 0:
                self.tree_top.insert('', index=i2, text=i2+1, values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]), tags=('oddrow',))
                self.tree_top.tag_configure('oddrow', background='mint cream')
            else:
                self.tree_top.insert('', index=i2, text=i2+1, values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]), tags=('evenrow',))
                self.tree_top.tag_configure('evenrow', background='alice blue')

            self.main_id.set(random.random())

            for j, item_j in enumerate(self.tree_header):
                self.dict_fet[self.tree_header[j]] = fetch[i2][j]

            self.list_fet.append(self.dict_fet.copy())

        self.statusbar.config(text=f"Connect: {self.filedb_name}")
        #self.cursor.close()
        #self.conn.close()

    def create_write(self):
        """save new writing in datebase"""
        if self.named.get() == "" or self.type.get() == "":# or self.number.get() == "" or self.date.get() == "" or self.place.get() == "" or self.service.get() == "":
            self.statusbar.config(text="Пожалуйста, заполните поля!", fg="red")
        else:
            self.database()
            self.cursor.execute(f"INSERT INTO {self.table_name[0][0]} (named,type,number,date,place,service,date_serv,date_repair,description,id) VALUES(?,?,?,?,?,?,?,?,?,?)", (self.named.get(),self.type.get(),self.number.get(),self.date.get(),self.place.get(),self.service.get(),self.date_serv.get(),self.date_repair.get(),self.description.get(),self.main_id.get()))
            self.connectdb.commit()
            self.named.set("")
            self.type.set("")
            self.number.set("")
            self.date.set("")
            self.place.set("")
            self.service.set("")
            self.date_serv.set("")
            self.date_repair.set("")
            self.description.set("")
            self.main_id.set("")
            #self.cursor.close()
            self.read_db(self.table_db)
            self.update_combobox()
            self.statusbar.config(text="Данные внесены!")

    def delete_write(self):
        """delete writing from datebase"""
        try:
            selected_item_0 = self.tree_top.selection()[0]
            type = self.tree_top.item(self.tree_top.selection())['values'][1]
            number = self.tree_top.item(self.tree_top.selection())['values'][2]
            delet = tkMessageBox.askquestion('Сообщение', f'Удалить {type} №{number}?')
            if delet == 'yes':
                self.cursor.execute(f"DELETE FROM {self.table_name[0][0]} WHERE number = ?",(number,))
                #self.cursor.close()
                self.connectdb.commit()
                self.tree_top.delete(self.tree_top.selection()[0])
            self.read_db(self.table_db)
            self.update_combobox()
        except IndexError:
            pass

    def SetEntryText(self, txtObject, value):
        txtObject.delete(0, tk.END)
        txtObject.insert(0, value)

    def select_item_tree_top(self, event):
        """window see element current table"""
        curitem = self.tree_top.focus()
        sel_root = tk.Toplevel(self.parent, bg='alice blue')
        sel_root.geometry('850x500')
        sel_root.resizable(0, 0)
        sel_root.wm_title(f"{self.tree_top.item(curitem)['values'][1]} зав.№{self.tree_top.item(curitem)['values'][2]}")

        self.connect_db(self.filedb_name)
        eqe = self.cursor.execute(f'SELECT * FROM {self.table_name[0][0]} WHERE id = ?',(self.tree_top.item(curitem)['values'][9],)).fetchall()
        #self.cursor.close()

        Left_n = tk.Frame(sel_root, bg='alice blue', width=600, height=500)
        Left_n.pack(side='left', fill='y')
        Right_n = tk.Frame(sel_root, bg='alice blue', width=600, height=500)
        Right_n.pack(side='left', fill='y')

        lbl_list1 = tk.Label(Left_n, text="", bg='alice blue', font=("Arial", 10, "bold"))
        lbl_list1.grid(row=0, column=0)

        lbl_id = tk.Label(Left_n, text="ID", bg='alice blue')
        lbl_id.grid(row=1, column=0)
        self.ent_id = tk.Entry(Left_n, width=25, font=("Arial", 10, "bold"))
        self.SetEntryText(self.ent_id,self.tree_top.item(curitem)['values'][9])
        self.ent_id.grid(row=1, column=1)

        lbl_named = tk.Label(Left_n, text=self.name_col1, bg='alice blue')
        lbl_named.grid(row=2, column=0)
        self.ent_named = tk.Entry(Left_n, width=25, font=("Arial", 10, "bold"))
        self.SetEntryText(self.ent_named,self.tree_top.item(curitem)['values'][0])
        self.ent_named.grid(row=2, column=1)

        lbl_type = tk.Label(Left_n, text=self.name_col2, bg='alice blue')
        lbl_type.grid(row=3, column=0)
        self.ent_type = tk.Entry(Left_n, width=25, font=("Arial", 10, "bold"))
        self.SetEntryText(self.ent_type,self.tree_top.item(curitem)['values'][1])
        self.ent_type.grid(row=3, column=1)

        lbl_numb = tk.Label(Left_n, text=self.name_col3, bg='alice blue')
        lbl_numb.grid(row=4, column=0)
        self.ent_numb = tk.Entry(Left_n, width=25, font=("Arial", 10, "bold"))
        self.SetEntryText(self.ent_numb,self.tree_top.item(curitem)['values'][2])
        self.ent_numb.grid(row=4, column=1)

        lbl_data = tk.Label(Left_n, text=self.name_col4, bg='alice blue')
        lbl_data.grid(row=5, column=0)
        self.ent_data = tk.Entry(Left_n, width=25, font=("Arial", 10, "bold"))
        self.SetEntryText(self.ent_data,self.tree_top.item(curitem)['values'][3])
        self.ent_data.grid(row=5, column=1)

        lbl_place = tk.Label(Left_n, text=self.name_col5, bg='alice blue')
        lbl_place.grid(row=6, column=0)
        self.ent_place = tk.Entry(Left_n, width=25, font=("Arial", 10, "bold"))
        self.SetEntryText(self.ent_place,self.tree_top.item(curitem)['values'][4])
        self.ent_place.grid(row=6, column=1)

        lbl_serv = tk.Label(Left_n, text=self.name_col6, bg='alice blue')
        lbl_serv.grid(row=7, column=0)
        self.ent_serv = tk.Entry(Left_n, width=25, font=("Arial", 10, "bold"))
        self.SetEntryText(self.ent_serv,self.tree_top.item(curitem)['values'][5])
        self.ent_serv.grid(row=7, column=1)

        lbl_disc = tk.Label(Left_n, text="Примечание:", bg='alice blue')
        lbl_disc.grid(row=8, column=0)
        self.ent_disc = tk.Text(Left_n, width=15, font=("Arial", 10, "bold"))
        self.ent_disc.insert(tk.INSERT, eqe[0][8])
        self.ent_disc.place(x=10, y=190, width=290, height=85)

        save_btn = tk.Button(Left_n, text="Сохранить", command=self.save_detail)
        save_btn.configure(bg="#6699CC", fg='white', highlightbackground="#0CD9E8", highlightcolor="#0DFFCC",font=("Times New Roman", 15, "bold"))
        save_btn.place(x=100, y=450)

        lbl_list = tk.Label(Right_n, text="Данные оборудования", bg='alice blue', font=("Arial", 10, "bold"))
        lbl_list.pack(side='top')
        scrollbary = tk.Scrollbar(Right_n, orient='vertical')
        scrollbary.pack(side='right', fill='y')
        tree_sel = ttk.Treeview(Right_n, columns=self.tree_header[1:3]+self.tree_header[6:8], selectmode="extended", height=500, yscrollcommand=scrollbary.set)
        scrollbary.config(command=tree_sel.yview)
        tree_sel.heading('#0', text="№", anchor='w')
        tree_sel.heading('type', text=self.name_col2, anchor='w')
        tree_sel.heading('number', text=self.name_col3, anchor='w')
        tree_sel.heading('date_serv', text=self.name_col8, anchor='w')
        tree_sel.heading('date_repair', text=self.name_col9, anchor='w')
        tree_sel.column('#0', stretch=False, minwidth=20, width=30)
        tree_sel.column('type', width=80)
        tree_sel.column('number', width=160)
        tree_sel.column('date_serv', width=150)
        tree_sel.column('date_repair', width=150)
        tree_sel.pack(fill='both', expand='yes')
        tree_sel.insert('', index=0, text=1, values=(self.tree_top.item(curitem)['values'][1],self.tree_top.item(curitem)['values'][2],self.tree_top.item(curitem)['values'][3]))

    def save_detail(self):
        """save detail in database"""
        id = self.ent_id.get()
        named = self.ent_named.get()
        type = self.ent_type.get()
        number = self.ent_numb.get()
        date = self.ent_data.get()
        place = self.ent_place.get()
        service = self.ent_serv.get()
        description = self.ent_disc.get("1.0", tk.END)
        self.connect_db(self.filedb_name)
        self.cursor.execute(f'UPDATE {self.table_name[0][0]} SET named=?,type=?,number=?,date=?,place=?,service=?,description=?,id=? WHERE id=?',(named,type,number,date,place,service,description,id,id,))
        #self.cursor.close()
        self.connectdb.commit()
        self.read_db(self.table_db)
        self.update_combobox()

    def select_item_tree_left(self, event):
        """select table datebase"""
        self.cur_table = self.tree_left.focus()
        if self.cur_table == '0':
            self.table_db = 'equipment'
        elif self.cur_table == '1':
            self.table_db = 'brp'
        elif self.cur_table == '2':
            self.table_db = 'measuring'
        elif self.cur_table == '3':
            self.table_db = 'certification'
        self.read_db(self.table_db)
        self.update_combobox()

    def win_add(self):
        """window add element in current table datebase"""
        add_root = tk.Toplevel(self.parent, bg='alice blue')
        add_root.geometry('500x350')
        add_root.resizable(0, 0)
        add_root.title('Добавление записи')

        lbl_win_named = tk.Label(add_root, bg='alice blue', text=self.name_col1, font=('arial 15'), bd=10)
        lbl_win_named.grid(row=0, stick="e")
        lbl_win_type = tk.Label(add_root, bg='alice blue', text=self.name_col2, font=('arial 15'), bd=10)
        lbl_win_type.grid(row=1, stick="e")
        lbl_win_number = tk.Label(add_root, bg='alice blue', text=self.name_col3, font=('arial 15'), bd=10)
        lbl_win_number.grid(row=2, stick="e")
        lbl_win_date = tk.Label(add_root, bg='alice blue', text=self.name_col4, font=('arial 15'), bd=10)
        lbl_win_date.grid(row=3, stick="e")
        lbl_win_place = tk.Label(add_root, bg='alice blue', text=self.name_col5, font=('arial 15'), bd=10)
        lbl_win_place.grid(row=4, stick="e")
        lbl_win_service = tk.Label(add_root, bg='alice blue', text=self.name_col6, font=('arial 15'), bd=10)
        lbl_win_service.grid(row=5, stick="e")

        ent_win_named = tk.Entry(add_root, textvariable=self.named, width=23)
        ent_win_named.grid(row=0, column=1)
        ent_win_type = tk.Entry(add_root, textvariable=self.type, width=23)
        ent_win_type.grid(row=1, column=1)
        ent_win_number = tk.Entry(add_root, textvariable=self.number, width=23)
        ent_win_number.grid(row=2, column=1)
        ent_win_date = tk.Entry(add_root, textvariable=self.date, width=23)
        ent_win_date.grid(row=3, column=1)
        combo_place = ttk.Combobox(add_root, textvariable=self.place, value=self.name_place, height=4, width=20)
        combo_place.grid(row=4, column=1)
        combo_service = ttk.Combobox(add_root, textvariable=self.service, value=self.name_service, state='readonly', height=4, width=20)
        combo_service.grid(row=5, column=1)

        try:
            curitem = self.tree_top.focus()
            named = self.tree_top.item(curitem)['values'][0]
            type = self.tree_top.item(curitem)['values'][1]
            self.SetEntryText(ent_win_named, named)
            self.SetEntryText(ent_win_type, type)
        except IndexError:
            pass

        btn_win_add = tk.Button(add_root, text='Добавить запись', command=self.create_write)
        btn_win_add.configure(bg="#6699CC", fg='white', highlightbackground="#0CD9E8", highlightcolor="#0DFFCC",font=("Times New Roman", 15, "bold"))
        btn_win_add.grid(row=6, column=1, stick="e")


root = tk.Tk()
root.event_add('<<Paste>>', '<Control-igrave>')
root.event_add("<<Copy>>", "<Control-ntilde>")
my_gui = DatabaseUI(root)
root.mainloop()
