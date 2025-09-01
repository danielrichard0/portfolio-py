from aplikasi import db_connect
from aplikasi.models.response import responseJSON

def get_user_data(email):
    connection = db_connect()
    res = {}
    try:
        cursor = connection.cursor()
        sql = '''SELECT email, password, name, id from portfolio_tracker.users where email = %s'''
        cursor.execute(sql, (email,))
        data = cursor.fetchall()
        res = responseJSON(200, 'T', 'success', data)
        print(data)
    except Exception as error:
        res = responseJSON(400, 'F', 'Error', [])
    finally:
        if(connection):
            cursor.close()
            connection.close()
    return res                
