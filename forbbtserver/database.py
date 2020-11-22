from mysql.connector import connect


def connect_to_database():
    con = connect(user='root', password='', database='bbt')
    cursor = con.cursor()

    return con, cursor
