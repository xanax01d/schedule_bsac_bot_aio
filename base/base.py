import sqlite3
from configs.groups import dict1
from configs.admins import admin_ids
class BotDB:
    #подключаем базу и создаем нужные базы,если их нет 
    def __init__(self,base):
        self.con = sqlite3.connect(base)
        self.cur = self.con.cursor() 
        self.cur.execute("""CREATE TABLE IF NOT EXISTS user_status(
            user_id INTEGER PRIMARY KEY NOT NULL,
            user_fn TEXT,
            banned INTEGER NOT NULL
        )""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS users_group(
            user_id INTEGER PRIMARY KEY NOT NULL,
            user_group TEXT,
            username TEXT,
            user_fn TEXT,
            chat_id INTEGER
            )""")
        self.con.commit()  
    #добавляем пользователя
    def add_user(self,user_id,user_group,username,user_fn,chat_id):
        self.cur.execute("INSERT or REPLACE INTO 'users_group' VALUES (?,?,?,?,?)",(user_id,user_group,username,user_fn,chat_id,))
        return self.con.commit()
    #получаем расписание
    def get_schedule(self,user_id,day):
        self.cur.execute("SELECT user_group FROM users_group WHERE user_id =  ?",(user_id,))
        group_row = self.cur.fetchall()
        group = '' + group_row[0][0]
        table = dict1.get(group)
        self.cur.execute(f"SELECT sc FROM {table} WHERE day = ?",(day,))
        return self.cur.fetchall()[0][0]
    def close(self):
        self.con.close()
    def add_user_bans(self,user_id,user_ban_status,user_fn):
        self.cur.execute("INSERT OR REPLACE INTO user_status VALUES (?,?,?)",(user_id,user_fn,user_ban_status,))
        return self.con.commit()
    def check_ban(self,user_id):
        self.cur.execute("SELECT banned FROM user_status WHERE user_id = ?",(user_id,))
        return self.cur.fetchone()
    def give_ban(self,user_id):
        if user_id not in admin_ids:
            self.cur.execute("UPDATE user_status SET banned = 1 WHERE user_id = ? ",(user_id,))
            return self.con.commit()
    def unban(self,user_id):
        self.cur.execute("UPDATE user_status SET banned = 0 WHERE user_id = ? ",(user_id,))
        return self.con.commit()
    def get_banned_users(self):
        self.cur.execute("SELECT user_id FROM user_status WHERE banned = ?",(1,))
        result = [i[0] for i in (self.cur.fetchall())]
        return result
    def get_users(self):
        self.cur.execute("SELECT user_fn FROM user_status")
        result = [i[0] for i in (self.cur.fetchall())]
        return result
    def get_user_id_by_username(self,user_fn):
        self.cur.execute("SELECT user_id FROM user_status WHERE user_fn = ?",(user_fn,))
        return self.cur.fetchone()[0]
    def get_banned_user_fns(self):
        self.cur.execute("SELECT user_fn FROM user_status WHERE banned = ?",(1,))
        result = [i[0] for i in (self.cur.fetchall())]
        return result
    def get_users_ids(self):
        self.cur.execute("SELECT chat_id FROM users_group")
        result = [i[0] for i in (self.cur.fetchall())]
        return result
    def add_user_chat_id(self,user_id,chat_id):
        self.cur.execute("INSERT OR REPLACE INTO users_group(user_id,chat_id) VALUES(?,?)",(user_id,chat_id,))
        return self.con.commit()
    def check_chat_id(self,user_id):
        self.cur.execute("SELECT chat_id FROM users_group WHERE user_id = ?",(user_id,))
        data = self.cur.fetchone()
        if data is None:
            return False
        return data
    def clear_users_base(self):
        self.cur.execute("DROP TABLE IF EXISTS users_group")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS users_group(
            user_id INTEGER PRIMARY KEY NOT NULL,
            user_group TEXT,
            username TEXT,
            user_fn TEXT,
            chat_id INTEGER
            )""")
        self.con.commit()  
    def clear_ban_base(self):
        self.cur.execute("DROP TABLE IF EXISTS user_status")
        self.cur.execute("""CREATE TABLE IF NOT EXISTS user_status(
            user_id INTEGER PRIMARY KEY NOT NULL,
            user_fn TEXT,
            banned INTEGER NOT NULL
        )""")
        self.con.commit()