import pypyodbc
import azurecred

class AzureDB:

  dsn='DRIVER='+azurecred.AZDBDRIVER+';Server=tcp:'+azurecred.AZDBSERVER+',1433;Database='+azurecred.AZDBNAME+';UID='+azurecred.AZDBUSER+';PWD='+ azurecred.AZDBPW+';Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

  def __init__(self):
    self.conn = pypyodbc.connect(self.dsn)
    self.cursor = self.conn.cursor()

  def finalize(self):
    if self.conn:
      self.conn.close()

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.finalize()

  def __enter__(self):
    return self

  def azureGetData(self):
    try:
      self.cursor.execute("SELECT name,text from data")
      data = self.cursor.fetchall()
      return data
    except pypyodbc.DatabaseError as exception:
      print('Failed to execute query')
      print(exception)
      exit (1)
  
  def azureTest(self, name, text):
    print(name, text)

  def azureAddData(self, name, text):
    sql = '''INSERT INTO data (name, text) VALUES (?, ?)'''
    val = (name, text)
    self.cursor.execute(sql, val)
    self.conn.commit()

  def azureDeleteData(self, text):
    sql = "DELETE FROM data WHERE text = ?"
    val = [text]
    self.cursor.execute(sql, val)
    self.conn.commit()

#zakomentowana funkcja dodająca do bazy
#def azureAddData(self):
#  self.cursor.execute("INSERT into data (name, text) values ('Adam', 'Ta stronka jest okropna...')")
#  self.conn.commit()
#zakomentowana funkcja usuwająca rekord z bazy gdzie name = Adam
#def azureDeleteData(self):
#self.cursor.execute("DELETE FROM data WHERE name = 'Adam'")
#self.conn.commit()
