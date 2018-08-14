import db_connect as db_controller

#db_controller.DatabaseConnection()

#if __name__ == '__main__':
database_connection = db_controller.DatabaseConnection()
database_connection.show_table()