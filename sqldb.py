import sqlite3 as sqldb
from people_gen import People
class Database:

  def __init__(self,table):
    connect = sqldb.connect('contact.db',check_same_thread=False)
    connect.row_factory = sqldb.Row
    connect.isolation_level = None
    self.db = connect.cursor()
    self.table = table
 
  def create_table(self):
    sql = f"CREATE TABLE IF NOT EXISTS `{self.table}` (`id` INTEGER PRIMARY KEY, `name` VARCHAR(25), `surname` VARCHAR(30), `email` VARCHAR(50), `phone` VARCHAR(30), `slug` VARCHAR(8), `address` VARCHAR(100), `twitter` VARCHAR(500))"
    self.db.execute(sql)
    
  def insert(self,dict_data):
    cols = "`, `".join(list(dict_data.keys()))
    vals = "', '".join(list(dict_data.values()))
    sql = f"INSERT INTO `{self.table}` (`{cols}`) VALUES ('{vals}')"
    self.db.execute(sql)

  def select_all(self):
    sql = f"SELECT * FROM `{self.table}`"
    data = self.db.execute(sql).fetchall()
    return [dict(x) for x in data]
  
  def select_by_id(self,id):
    sql = f"SELECT * FROM `{self.table}` WHERE `id` = {id}"
    data = self.db.execute(sql).fetchone()
    return dict(data) if data else False
  
  def select_by_cols(self,dict_data):
    [(col,val)] = list(dict_data.items())
    sql = f"SELECT * FROM `{self.table}` WHERE `{col}` = '{val}'"
    data = self.db.execute(sql).fetchall()
    return [dict(x) for x in data] 
  
  def delete(self,id):
    sql = f"DELETE FROM `{self.table}` WHERE `id` = {id}"
    deleted = self.select_by_id(id)
    self.db.execute(sql)
    return deleted
  
  def update(self,dict_data,id):
    col_and_val = ', '.join([f"`{col}` = '{val}'" for col,val in dict_data.items()])
    sql = f"UPDATE `{self.table}` SET {col_and_val} WHERE `id` = {id}"
    self.db.execute(sql)
    # print(sql)
  
  def show_records(self):
    data = self.select_all()
    result = []
    for x in data:
      tmp = []
      for key,val in x.items():
        tmp.append(f"{key}:{val}")
      result.append('\n'.join(tmp))
    return f"{self.table.upper()}\n=======\n"+'\n------\n'.join(result)

datas = Database('phonebook')
# datas.create_table()
# person = People(50)
# for x in person.people:
#   datas.insert(x)
# print(datas.show_records())


