import sqlite3

class Sqliter:

    def __init__(self, database_file):
        """Connection database"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()


    def new_user(self, user_id, agent):
        """Add new user"""
        with self.connection:
            return self.cursor.execute("INSERT INTO main (user_id, agent) VALUES (?,?)",(user_id, agent))

    def check_user(self,user_id):
        """Check user subcription"""
        with self.connection:
            result = self.cursor.execute("SELECT id FROM main WHERE user_id = ?",(user_id,)).fetchall()
            return bool(len(result))

    def get_user(self,agent):
        """Get user info"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM main WHERE agent = ?", (agent,)).fetchall()
            return result

    def get_all_user(self):
        """Get all users"""
        with self.connection:
            result = self.cursor.execute("SELECT * FROM main").fetchall()
            return result

    def close(self):
        """Close connection"""
        self.connection.close()