import sqlite3

class BotDB:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    # проверка есть ли пользователь в бд
    def user_exists(self, user_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return bool(len(result.fetchall()))

    # берем id пользователя по user_id
    def get_user_id(self, user_id):
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    # добавление пользователя в бд
    def add_user(self, user_id):
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    # добавление сообщения от пользователя
    def add_msg(self, user_id, msg):
        with self.conn:
            return self.cursor.execute("INSERT INTO `users_msgs` (`msg`, `user_id`) VALUES (?, ?)", (msg, user_id,))

    # добавление файлов в бд
    def add_id_file(self, user_id, file_id):
        with self.conn:
            return self.cursor.execute("INSERT INTO `files` (`user_id`, `file_id`) VALUES(?, ?)", (user_id, file_id,))


    # закрытие соединения с бд
    def close(self):
        self.connection.close()