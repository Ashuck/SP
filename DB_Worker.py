import sqlite3

class Worker():
    def __init__(self):

        self.conn = sqlite3.connect("SP.db")
        self.cursor = self.conn.cursor()


    def create_table_answers(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS answers
                        (request text, 
                        answer text, 
                        theme text)
                    """)
        self.conn.commit()
    

    def add_answers(self, data):
        self.cursor.executemany("INSERT INTO answers VALUES (?,?,?)", data)
        self.conn.commit()
    

    def get_themes(self):
        self.cursor.execute("SELECT DISTINCT theme FROM answers")
        return self.cursor.fetchall()

    
    def get_answers(self, theme):
        self.cursor.execute(f"SELECT request, answer FROM answers WHERE theme='{theme}'")
        return self.cursor.fetchall()


