import sqlite3



Scripts = {
    "Create":[
        '''
        CREATE TABLE IF NOT EXISTS users(
        
            name TEXT NOT NULL,    
            password INT NOT NULL,
            status TEXT NOT NULL

        );
        ''',

        '''
        CREATE TABLE IF NOT EXISTS quiz(
        
            id INT PRIMARY KEY NOT NULL,
            name TEXT NOT NULL    

        );
        ''',

        '''
        CREATE TABLE IF NOT EXISTS questions(
        
            id INT PRIMARY KEY NOT NULL,
            quiz TEXT NOT NULL,    
            questions TEXT NOT NULL
        );
        '''
    ],

    "AddUser":'''
        INSERT INTO users(name, password, status)

                VALUES (?, ?, 'user');
    ''',

    "Select":'''
        SELECT * FROM users WHERE name = ?;
    ''',

    "AddAdmin":'''
        INSERT INTO users(name, password, status)

                VALUES (?, ?, 'anmin');
    '''
}


def AddUser(name, password):
    conn = sqlite3.connect("app.db")

    cursor = conn.cursor()

    cursor.execute(Scripts["Select"], (name,))

    check_name = cursor.fetchall()

    cursor.execute("SELECT * FROM users")

    if check_name:
        return False
    
    cursor.execute(Scripts["AddUser"], (name, password))
    conn.commit()
    
    conn.close()
    return True

def CheckPassword(name, password):
    conn = sqlite3.connect("app.db")

    cursor = conn.cursor()

    cursor.execute(Scripts["Select"], (name,))
    check_user = cursor.fetchall()
    conn.close()

    if not check_user:
        return False, False, False
    elif str(check_user[0][1]) == str(password):
        return True, True, check_user[0][2]
    else:
        return True, False, False

if __name__ == "__main__":
    conn = sqlite3.connect("app.db")

    cursor = conn.cursor()
    for i in Scripts["Create"]:
        cursor.execute(i)
    
    